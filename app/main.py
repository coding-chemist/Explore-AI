import streamlit as st
from components.header import render_header
from core.config import app as appcfg
from services.assets import load_css
from services.assets import load_logo_base64

# prefer SVG data-URI as page icon when available
try:
    logo_icon = load_logo_base64()
except (FileNotFoundError, OSError):
    logo_icon = appcfg.page_icon

st.set_page_config(
    page_title=appcfg.app_name,
    page_icon=logo_icon,
    layout="wide",
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

page = st.query_params.get("page", "landing")
render_header()
if page == "landing":
    from Landing import render

    render()
else:
    st.write(":construction: Page not found")
