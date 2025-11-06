import streamlit as st
from core.config import app as appcfg
from services.assets import gif_src, load_template


def render():
    hero_html = load_template("partials/hero.html")
    hero_html = hero_html.replace("{{GIF_SRC}}", gif_src()).replace(
        "{{TAGLINE}}", appcfg.tagline
    )
    st.markdown(hero_html, unsafe_allow_html=True)
