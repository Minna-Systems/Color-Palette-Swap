"""Diabetes education webpage — swap color palettes in the sidebar."""

from __future__ import annotations

import base64
from pathlib import Path

import streamlit as st

from demo_page import render_palette_demo
from palettes import PALETTES
from sidebar import inject_sidebar_theme, render_palette_sidebar

st.set_page_config(
    page_title="Ketsu — diabetes",
    page_icon="🩸",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    "<style>"
    "footer {visibility:hidden;}"
    "header[data-testid='stHeader'] {background:transparent;}"
    ".block-container {padding-top:0; max-width:1200px; padding-left:1rem; padding-right:1rem;}"
    "</style>",
    unsafe_allow_html=True,
)


def _palette_image_data_uri(path: Path) -> str | None:
    if not path.exists():
        return None
    return "data:image/png;base64," + base64.b64encode(path.read_bytes()).decode()


def main() -> None:
    inject_sidebar_theme()

    with st.sidebar:
        st.header("Palette")
        by_name = {p["name"]: p for p in PALETTES}
        name = st.radio("Choose", list(by_name.keys()), label_visibility="collapsed")
        palette = by_name[name]
        uri = _palette_image_data_uri(palette["image"])
        if uri:
            st.image(uri, use_container_width=True)
        render_palette_sidebar(palette)

    render_palette_demo(palette)


if __name__ == "__main__":
    main()
