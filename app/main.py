import importlib

import streamlit as st
from components.header import render_header
from core.config import app as appcfg
from core.models import Page
from services.assets import load_css
from services.assets import load_logo_base64

# prefer SVG data-URI as page icon when available
logo_icon = load_logo_base64()

st.set_page_config(
    page_title=appcfg.app_name,
    page_icon=logo_icon,
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    f"<style>{load_css('main.css', 'landing.css')}</style>",
    unsafe_allow_html=True,
)

st.markdown(
    """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""",
    unsafe_allow_html=True,
)

# normalize query param (Streamlit returns lists for query params)
_page = st.query_params.get("page", [Page.landing.value])
if isinstance(_page, list):
    _page = _page[0] if _page else Page.landing.value

# coerce into the Page enum; fall back to landing for unknown values
try:
    page = Page(str(_page))
except ValueError:
    page = Page.landing

render_header()

# map Page enum values to module import paths. Use full package paths so
# imports work predictably whether the package is executed as a module or
# imported.
_route_map = {
    Page.landing: "Landing",
    Page.home: "Home",
    Page.ml: "pages.ml",
    Page.genai: "pages.genai",
    Page.agenticai: "pages.agenticai",
    Page.dl: "pages.dl",
}

module_name = _route_map.get(page)
if module_name:
    try:
        mod = importlib.import_module(module_name)
        render_fn = getattr(mod, "render", None)
        if callable(render_fn):
            render_fn()
        else:
            st.error(
                "Page module '{name}' does not expose a callable "
                "render()".format(name=module_name)
            )
    except Exception as exc:  # keep broad handling to avoid crashing the UI
        st.error(f"Failed to load page '{page.value}': {exc}")
else:
    st.write(":construction: Page not found")
