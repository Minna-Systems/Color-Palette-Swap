from __future__ import annotations

from pathlib import Path

ASSETS = Path(__file__).resolve().parent / "assets"

# Theme tokens mirror the Blocksy WordPress palette slots on minnasystems.com.
Theme = dict[str, str]

PALETTES: list[dict] = [
    {
        "id": "original-strip",
        "name": "Original Strip",
        "image": ASSETS / "IMG_0789-34e844b0-8bc3-4ce0-add2-23282ec67e55.png",
        "theme": {
            "c1": "#D92B3A",
            "c2": "#B8222F",
            "c3": "#535353",
            "c4": "#264573",
            "c5": "#E2E7ED",
            "c6": "#EDEFF2",
            "c7": "#F7F8F8",
            "c8": "#FFFFFF",
        },
        "colors": [
            {"name": "Drop Red", "hex": "#D92B3A"},
            {"name": "Royal Blue", "hex": "#3A5BE0"},
            {"name": "Cold Current", "hex": "#264573"},
            {"name": "Pearl Bay", "hex": "#7AC5CA"},
            {"name": "Wild Daffodil", "hex": "#F5DC6C"},
            {"name": "Fairytale", "hex": "#C893D9"},
        ],
    },
    {
        "id": "sky-ink",
        "name": "Sky & Ink",
        "image": ASSETS / "IMG_8068-bc3e8d68-e964-4441-a755-c0f9609467cb.png",
        "theme": {
            "c1": "#D92B3A",
            "c2": "#C42432",
            "c3": "#535353",
            "c4": "#1F2A5C",
            "c5": "#E2E7ED",
            "c6": "#EDEFF2",
            "c7": "#F7F8F8",
            "c8": "#FFFFFF",
            "accent": "#2F7BF0",
        },
        "primary": [
            {"name": "Drop Red", "hex": "#D92B3A"},
            {"name": "Sky Blue", "hex": "#2F7BF0"},
            {"name": "Ink Navy", "hex": "#1F2A5C"},
        ],
        "accent": [
            {"name": "Coin Gold", "hex": "#F7B731"},
            {"name": "Streak Orange", "hex": "#FF8A3D"},
            {"name": "In-Range Mint", "hex": "#3CCB8A"},
            {"name": "Cosmic Purple", "hex": "#7B5CD6"},
        ],
    },
    {
        "id": "cosmic-play",
        "name": "Cosmic Play",
        "image": ASSETS / "IMG_7010-bcc791a5-7ed8-4741-a9af-6042df286116.png",
        "theme": {
            "c1": "#6B4FD0",
            "c2": "#5A41B8",
            "c3": "#535353",
            "c4": "#2A1A5E",
            "c5": "#E2E7ED",
            "c6": "#EDEFF2",
            "c7": "#F7F8F8",
            "c8": "#FFFFFF",
            "accent": "#5FD8E6",
        },
        "primary": [
            {"name": "Drop Red", "hex": "#D92B3A"},
            {"name": "Cosmic Purple", "hex": "#6B4FD0"},
            {"name": "Deep Space", "hex": "#2A1A5E"},
        ],
        "accent": [
            {"name": "Leaderboard Cyan", "hex": "#5FD8E6"},
            {"name": "Coin Gold", "hex": "#F7B731"},
            {"name": "Bubblegum", "hex": "#FF7EB6"},
            {"name": "In-Range Mint", "hex": "#3CCB8A"},
        ],
    },
    {
        "id": "coastal-garden",
        "name": "Coastal Garden",
        "image": ASSETS / "IMG_5745-66824eff-6900-4279-bbf9-428e9441e301.png",
        "theme": {
            "c1": "#D8402E",
            "c2": "#C03828",
            "c3": "#535353",
            "c4": "#264573",
            "c5": "#E2E7ED",
            "c6": "#EDEFF2",
            "c7": "#F7F8F8",
            "c8": "#FFFFFF",
            "accent": "#7AC5CA",
        },
        "primary": [
            {"name": "Papaya Red", "hex": "#D8402E"},
            {"name": "Cold Current", "hex": "#264573"},
            {"name": "Wild Daffodil", "hex": "#F5DC6C"},
        ],
        "accent": [
            {"name": "Pearl Bay", "hex": "#7AC5CA"},
            {"name": "Fairytale", "hex": "#C893D9"},
            {"name": "Coral", "hex": "#F28B82"},
            {"name": "Leaf", "hex": "#7BC47F"},
        ],
    },
]

