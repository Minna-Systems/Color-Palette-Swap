"""Diabetes education webpage — swap color palettes in the sidebar."""

from __future__ import annotations

import base64
import random
from pathlib import Path

import streamlit as st

from demo_page import render_palette_demo
from palettes import PALETTES
from sidebar import inject_sidebar_theme, render_palette_sidebar
from theme import apply_order, page_swatches

st.set_page_config(
    page_title="Minna Palette",
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


def _swatch_count(palette: dict) -> int:
    primary, accent, _ = page_swatches(palette)
    return len(primary) + len(accent)


def _shuffle(count: int) -> list[int]:
    order = list(range(count))
    random.shuffle(order)
    if order == list(range(count)) and count > 1:
        order[0], order[1] = order[1], order[0]
    return order


def main() -> None:
    inject_sidebar_theme()

    with st.sidebar:
        st.header("Palette")
        by_name = {p["name"]: p for p in PALETTES}
        name = st.radio("Choose", list(by_name.keys()), label_visibility="collapsed")
        palette = by_name[name]
        count = _swatch_count(palette)
        if st.session_state.get("active_palette") != palette["id"]:
            st.session_state.active_palette = palette["id"]
            st.session_state.order = list(range(count))

        uri = _palette_image_data_uri(palette["image"])
        if uri:
            st.image(uri, use_container_width=True)

        shuffle_col, reset_col = st.columns(2)
        with shuffle_col:
            if st.button("Random", use_container_width=True):
                st.session_state.order = _shuffle(count)
        with reset_col:
            if st.button("Reset", use_container_width=True):
                st.session_state.order = list(range(count))

        primary, accent, neutrals = page_swatches(palette)
        primary, accent = apply_order(primary, accent, st.session_state.order)
        shuffled = st.session_state.order != list(range(count))
        render_palette_sidebar(primary, accent, shuffled)

    render_palette_demo(palette, primary, accent, neutrals)


if __name__ == "__main__":
    main()
