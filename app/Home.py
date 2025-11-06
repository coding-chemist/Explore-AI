import textwrap
from pathlib import Path

import streamlit as st
from services.assets import asset_data_uri


def _load_home_css():
    css_path = Path(__file__).parents[1] / "styles" / "home.css"
    try:
        css = css_path.read_text(encoding="utf-8")
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    except (OSError, FileNotFoundError):
        # fallback: nothing (main.css will still provide base styles)
        pass


def render():
    # top-right landing icon button (cyan circular background)
    home_anchor = (
        '<a href="?page=landing" class="xa-home-btn" '
        'title="Landing" target="_self">'
        '<svg class="xa-home-icon" viewBox="0 0 24 24" width="18" '
        'height="18" xmlns="http://www.w3.org/2000/svg" '
        'aria-hidden="true">'
        '<path d="M3 11.5L12 4l9 7.5V20a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 '
        '1-1-1V11.5z"/></svg></a>'
    )

    st.markdown(home_anchor, unsafe_allow_html=True)

    # inject page-specific css (kept separate from main.css)
    _load_home_css()

    # render header and lead with custom classes so we can style them from CSS
    st.markdown(
        '<h2 class="xa-topics-header">Topics</h2>', unsafe_allow_html=True
    )
    st.markdown(
        (
            '<p class="xa-topics-lead">'
            "Ready to learn and build? Pick a topic below to find hands-on "
            "guides, project ideas and clear explanations — everything you "
            "need "
            "to turn concepts into real, usable skills. Start small, build "
            "often, and ship something you’re proud of.</p>"
        ),
        unsafe_allow_html=True,
    )

    # Topics section (load from HTML partial for better organization)
    topics_path = (
        Path(__file__).parent / "templates" / "partials" / "home_topics.html"
    )
    try:
        topics_html = topics_path.read_text(encoding="utf-8")
        # Replace icon placeholders with base64 data URIs so icons render
        topics_html = topics_html.replace(
            "{{ICON_ML}}", asset_data_uri("icons/ML.png")
        )
        topics_html = topics_html.replace(
            "{{ICON_DL}}", asset_data_uri("icons/DL.png")
        )
        topics_html = topics_html.replace(
            "{{ICON_GEN}}", asset_data_uri("icons/GA.png")
        )
        topics_html = topics_html.replace(
            "{{ICON_AGENT}}", asset_data_uri("icons/AA.png")
        )

        st.markdown(topics_html, unsafe_allow_html=True)
    except (OSError, FileNotFoundError):
        # fallback: render a simplified inline version
        topics_html = textwrap.dedent(
            """
        <div class="xa-topics">
            <div class="xa-topic">
                <div class="xa-topic-inner">
                    <h3>Topics</h3>
                    <p>Unable to load topics partial.</p>
                </div>
            </div>
        </div>
        """
        )
        st.markdown(topics_html, unsafe_allow_html=True)
