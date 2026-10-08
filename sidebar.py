from __future__ import annotations

import streamlit as st


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


_PRIMARY_ROLES = ("Logo and Sign up", "Start playing", "Headlines")
_ACCENT_ROLES = ("Coins", "Streak", "Time in range", "This week")


def render_palette_sidebar(primary: list[dict], accent: list[dict], shuffled: bool) -> None:
    st.subheader("Primary")
    for role, item in zip(_PRIMARY_ROLES, primary):
        st.write(f"{role}")
        st.caption(f"{item['name']} · {item['hex']}")
    st.subheader("Accent")
    for i, item in enumerate(accent):
        role = _ACCENT_ROLES[i] if i < len(_ACCENT_ROLES) else f"Stat {i + 1}"
        st.write(role)
        st.caption(f"{item['name']} · {item['hex']}")
    if shuffled:
        st.caption("Roles are shuffled. Reset returns the palette defaults.")
