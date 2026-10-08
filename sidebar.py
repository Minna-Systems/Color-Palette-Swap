from __future__ import annotations

import streamlit as st

from theme import palette_color_groups


def inject_sidebar_theme() -> None:
    st.markdown(
        "<style>"
        "section[data-testid=stSidebar],section[data-testid=stSidebar]>div"
        "{background:#fff!important;}"
        "section[data-testid=stSidebar] h1,"
        "section[data-testid=stSidebar] h2,"
        "section[data-testid=stSidebar] p,"
        "section[data-testid=stSidebar] label,"
        "section[data-testid=stSidebar] .stRadio label p"
        "{color:#111!important;-webkit-text-fill-color:#111!important;}"
        "</style>",
        unsafe_allow_html=True,
    )


def render_palette_sidebar(palette: dict) -> None:
    primary, accent = palette_color_groups(palette)
    st.subheader("Primary")
    for item in primary:
        st.write(f"`{item['hex']}` · {item['name']}")
    st.subheader("Accent")
    for item in accent:
        st.write(f"`{item['hex']}` · {item['name']}")
    st.caption("Primary: logo, buttons, headlines, alerts. Accent: the stats inside the day card.")
