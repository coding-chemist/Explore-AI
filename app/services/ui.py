from typing import Union

import streamlit as st
from core.models import UIMessage


def render_under_construction(
    payload: Union[str, UIMessage],
) -> None:
    """Render a small "under construction" notice consistently.

    This centralizes the HTML/CSS so topic pages stay concise.
    """
    # accept either a simple title string (backwards compatible) or a
    # UIMessage Pydantic model for richer options.
    if isinstance(payload, UIMessage):
        title = payload.title
        message = payload.message
        back_href = payload.back_href
        back_label = payload.back_label
    else:
        title = payload
        message = None
        back_href = "?page=home"
        back_label = "Back to Topics"

    # map some known topic titles to the requested accent colors
    t = title.lower()
    if "machine" in t:
        header_color = "#f7308c"  # Machine Learning
    elif "deep" in t or "dl" in t:
        header_color = "#ccff00"  # Deep Learning
    elif "gen" in t or "generative" in t:
        header_color = "#ffeb3b"  # Generative AI
    elif "agent" in t:
        header_color = "#00d9ff"  # Agentic AI
    else:
        header_color = "var(--c-cyan)"

    # render a colored header so each topic page has its accent color
    st.markdown(
        (
            '<h2 style="color:'
            + header_color
            + ';margin-top:0">'
            + title
            + "</h2>"
        ),
        unsafe_allow_html=True,
    )
    msg = message or "This page is being prepared — check back soon."

    parts = []
    parts.append(
        '<div style="border:1px solid rgba(255,255,255,0.06);'
        'padding:18px;border-radius:10px;" '
        '"background:linear-gradient(180deg, rgba(255,255,255,0.01), '
        'rgba(255,255,255,0.02));">'
    )
    parts.append(
        '<h3 style="margin:0 0 8px 0; color:#E6E6E6">'
        "🚧 Under construction</h3>"
    )
    parts.append('<p style="margin:0;color:rgba(245,247,250,0.9)">')
    parts.append(msg)
    parts.append("</p>")
    parts.append("<br/>")
    parts.append('<p style="margin-top:10px">')
    parts.append('<a class="glow-on-hover" href="')
    parts.append(back_href)
    parts.append('" target="_self">')
    parts.append(back_label)
    parts.append("</a></p>")
    parts.append("</div>")

    html = "".join(parts)

    st.markdown(html, unsafe_allow_html=True)
