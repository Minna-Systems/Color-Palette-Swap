from __future__ import annotations

from typing import TypedDict


class SemanticColors(TypedDict):
    brand: str
    brand_name: str
    action: str
    action_name: str
    ink: str
    ink_name: str
    alert: str
    alert_name: str
    success: str
    success_name: str
    reward: str
    reward_name: str
    streak: str
    streak_name: str
    text: str
    surface: str
    card: str
    border: str


def palette_color_groups(palette: dict) -> tuple[list[dict], list[dict]]:
    if palette.get("primary"):
        return palette["primary"], palette["accent"]
    colors = palette.get("colors", [])
    mid = 3 if len(colors) >= 6 else max(1, len(colors) // 2)
    return colors[:mid], colors[mid:]


def flat_palette_colors(palette: dict) -> list[dict]:
    if palette.get("colors"):
        return list(palette["colors"])
    primary, accent = palette_color_groups(palette)
    return list(primary) + list(accent)


def page_swatches(palette: dict) -> tuple[list[dict], list[dict], dict[str, str]]:
    """Three primaries and every accent, in palette order. No colors dropped."""
    primary, accent = palette_color_groups(palette)
    t = palette["theme"]
    while len(primary) < 3:
        primary.append({"name": "Primary", "hex": t["c1"]})
    neutrals = {
        "text": t["c3"],
        "surface": t["c7"],
        "card": t["c8"],
        "border": t["c5"],
    }
    return primary[:3], list(accent), neutrals


def semantic_colors(palette: dict) -> SemanticColors:
    """Map palette swatches to website roles (brand, CTAs, type, app states)."""
    primary, accent = palette_color_groups(palette)
    t = palette["theme"]

    brand = primary[0] if primary else {"name": "Brand", "hex": t["c1"]}
    action = primary[1] if len(primary) > 1 else brand
    ink = primary[2] if len(primary) > 2 else {"name": "Ink", "hex": t["c4"]}

    # Accents: prefer named semantics when present; otherwise assign by order.
    by_name = {a["name"].lower(): a for a in accent}

    def pick(*keywords: str, default_idx: int) -> dict:
        for kw in keywords:
            for name, swatch in by_name.items():
                if kw in name:
                    return swatch
        if default_idx < len(accent):
            return accent[default_idx]
        return brand

    reward = pick("coin", "gold", "daffodil", default_idx=0)
    streak = pick("streak", "orange", "coral", default_idx=1)
    success = pick("mint", "leaf", "range", "bay", "pearl", default_idx=2)
    alert = pick("red", "drop", "papaya", default_idx=0)
    if alert["hex"] == brand["hex"] and len(accent) > 3:
        alert = pick("red", "drop", default_idx=3)

    # Low alert should read as brand red when brand is red-ish; else use brand for alerts
    if "red" in brand["name"].lower() or "papaya" in brand["name"].lower():
        alert = brand

    return SemanticColors(
        brand=brand["hex"],
        brand_name=brand["name"],
        action=action["hex"],
        action_name=action["name"],
        ink=ink["hex"],
        ink_name=ink["name"],
        alert=alert["hex"],
        alert_name=alert["name"],
        success=success["hex"],
        success_name=success["name"],
        reward=reward["hex"],
        reward_name=reward["name"],
        streak=streak["hex"],
        streak_name=streak["name"],
        text=t["c3"],
        surface=t["c7"],
        card=t["c8"],
        border=t["c5"],
    )


def text_on(hex_color: str) -> str:
    h = hex_color.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    y = (0.299 * r + 0.587 * g + 0.114 * b) / 255
    return "#111111" if y > 0.62 else "#ffffff"
