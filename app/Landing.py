import streamlit as st
from core.config import app as appcfg
from services.assets import asset_data_uri
from services.assets import gif_src
from services.assets import load_template


def render():
    hero_html = load_template("partials/hero.html")
    # inject icons as base64 data URIs so they render without needing
    # static files
    hero_html = hero_html.replace("{{GIF_SRC}}", gif_src()).replace(
        "{{TAGLINE}}", appcfg.tagline
    )
    # replace icon placeholders for headings (if present)
    hero_html = hero_html.replace("{{ICON_ML}}", asset_data_uri("icons/ML.png"))
    hero_html = hero_html.replace("{{ICON_DL}}", asset_data_uri("icons/DL.png"))
    hero_html = hero_html.replace(
        "{{ICON_GEN}}", asset_data_uri("icons/GA.png")
    )
    hero_html = hero_html.replace(
        "{{ICON_AGENT}}", asset_data_uri("icons/AA.png")
    )
    st.markdown(hero_html, unsafe_allow_html=True)
