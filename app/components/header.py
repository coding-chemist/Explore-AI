import streamlit as st
from services.assets import load_logo_base64


def render_header():
    logo = load_logo_base64()
    st.markdown(
        f"""
        <div class="xa-header">
            <img src="{logo}" alt="Explore‑AI" class="xa-logo"/>
            <div class="xa-brand">
                <h1>Explore‑AI</h1>
                <p class="muted">Mastering AI, end‑to‑end</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
