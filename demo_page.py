"""Product landing page. Primaries run chrome. Accents color real UI, not random words."""

from __future__ import annotations

import html

import streamlit as st

from theme import page_swatches, text_on

_METRICS = (
    ("+50", "coins today"),
    ("7", "day streak"),
    ("92%", "time in range"),
    ("Lv 4", "this week"),
)


def _page_html(primary: list[dict], accent: list[dict], n: dict[str, str]) -> str:
    p1, p2, p3 = (c["hex"] for c in primary)
    on_p1, on_p2, on_p3 = text_on(p1), text_on(p2), text_on(p3)
    accents = accent or [{"name": "Accent", "hex": p2}]

    metrics = []
    for i, swatch in enumerate(accents):
        value, label = _METRICS[i] if i < len(_METRICS) else ("—", swatch["name"])
        fg = text_on(swatch["hex"])
        metrics.append(
            f'<div class="metric" style="border-top:3px solid {swatch["hex"]};">'
            f'<div class="metric-value" style="color:{swatch["hex"]};">{html.escape(value)}</div>'
            f'<div class="metric-label">{html.escape(label)}</div></div>'
        )
    # The live glucose number stays in ink; accents are the surrounding stats.
    # First accent still colors the in-range fill on the chart.
    range_color = accents[0]["hex"]
    if len(accents) > 2:
        range_color = accents[2]["hex"]

    cols = len(accents)

    return f"""<style>
.site {{
  font-family: "Segoe UI", system-ui, -apple-system, sans-serif;
  background: {n["surface"]};
  color: {n["text"]};
  line-height: 1.55;
}}
.site * {{ box-sizing: border-box; }}
.wide {{ max-width: 1120px; margin: 0 auto; padding: 0 28px; }}
header.nav {{
  background: {n["card"]};
  border-bottom: 1px solid {n["border"]};
  position: sticky; top: 0; z-index: 2;
}}
header.nav .wide {{
  height: 72px; display: flex; align-items: center; justify-content: space-between; gap: 24px;
}}
.logo {{ margin: 0; font-weight: 800; font-size: 1.35rem; letter-spacing: -0.04em; color: {p1}; }}
nav ul {{ display: flex; gap: 28px; list-style: none; margin: 0; padding: 0; font-size: 0.95rem; }}
nav a {{ color: {n["text"]}; text-decoration: none; }}
nav a[aria-current="page"] {{ color: {p3}; font-weight: 650; }}
.btn {{
  font: inherit; font-weight: 650; font-size: 0.95rem;
  padding: 12px 20px; border-radius: 999px; border: 1.5px solid transparent; cursor: pointer;
}}
.btn-primary {{ background: {p2}; color: {on_p2}; }}
.btn-brand {{ background: {p1}; color: {on_p1}; }}
.btn-secondary {{ background: {n["card"]}; color: {p3}; border-color: {n["border"]}; }}
.btn-on-dark {{ background: {n["card"]}; color: {p3}; }}
.hero {{
  display: grid; grid-template-columns: 1.05fr 0.95fr; gap: 56px;
  align-items: center; padding: 72px 0 64px;
}}
@media (max-width: 860px) {{
  .hero, .steps {{ grid-template-columns: 1fr !important; }}
  nav {{ display: none; }}
}}
.eyebrow {{
  margin: 0 0 12px; font-size: 0.8rem; font-weight: 700;
  letter-spacing: 0.12em; text-transform: uppercase; color: {p1};
}}
h1 {{
  margin: 0 0 16px; font-size: clamp(2.4rem, 4.5vw, 3.5rem);
  line-height: 1.05; letter-spacing: -0.04em; font-weight: 750; color: {p3};
}}
.lede {{ margin: 0 0 28px; font-size: 1.12rem; max-width: 36rem; color: {n["text"]}; }}
.cta {{ display: flex; gap: 12px; flex-wrap: wrap; }}
.panel {{
  background: {n["card"]};
  border: 1px solid {n["border"]};
  border-radius: 24px;
  box-shadow: 0 18px 50px rgba(17, 24, 39, 0.08);
  padding: 22px;
}}
.panel-top {{ display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 4px; }}
.panel-top span {{ font-size: 0.8rem; color: {n["text"]}; }}
.glucose {{
  margin: 0; font-size: 3.2rem; letter-spacing: -0.05em; font-weight: 750; color: {p3}; line-height: 1;
}}
.glucose small {{ font-size: 1rem; font-weight: 600; letter-spacing: 0; margin-left: 4px; color: {n["text"]}; }}
.track {{
  margin: 16px 0 18px; height: 10px; border-radius: 99px; background: {n["border"]}; overflow: hidden;
}}
.track span {{ display: block; height: 100%; width: 68%; background: {range_color}; border-radius: 99px; }}
.metrics {{
  display: grid; grid-template-columns: repeat({cols}, 1fr); gap: 10px;
}}
.metric {{
  background: {n["surface"]}; border-radius: 14px; padding: 12px 12px 10px;
}}
.metric-value {{ font-size: 1.35rem; font-weight: 750; letter-spacing: -0.03em; }}
.metric-label {{ font-size: 0.75rem; color: {n["text"]}; margin-top: 2px; }}
.alert {{
  display: flex; align-items: center; justify-content: space-between; gap: 12px;
  margin-top: 14px; padding: 12px 14px; border-radius: 14px;
  background: {p1}14; color: {p3}; font-size: 0.92rem;
}}
.alert strong {{ color: {p1}; }}
section {{ padding: 28px 0 64px; }}
h2 {{
  margin: 0 0 8px; font-size: 2rem; letter-spacing: -0.03em; color: {p3}; font-weight: 750;
}}
.sub {{ margin: 0 0 28px; max-width: 36rem; }}
.steps {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px; }}
.step {{
  background: {n["card"]}; border: 1px solid {n["border"]}; border-radius: 18px; padding: 22px;
}}
.step b {{
  display: inline-flex; align-items: center; justify-content: center;
  width: 32px; height: 32px; border-radius: 999px;
  background: {p2}; color: {on_p2}; font-size: 0.85rem; margin-bottom: 14px;
}}
.step h3 {{ margin: 0 0 8px; font-size: 1.05rem; color: {p3}; }}
.step p {{ margin: 0; font-size: 0.95rem; }}
.band {{
  background: {p3}; color: {on_p3}; border-radius: 24px; padding: 40px 36px;
  display: flex; align-items: center; justify-content: space-between; gap: 24px; flex-wrap: wrap;
}}
.band h2 {{ color: {on_p3}; margin: 0 0 6px; }}
.band p {{ margin: 0; opacity: 0.85; }}
footer.foot {{
  border-top: 1px solid {n["border"]}; padding: 28px 0 40px;
  display: flex; justify-content: space-between; gap: 16px; flex-wrap: wrap;
  font-size: 0.9rem;
}}
footer.foot a {{ color: {n["text"]}; text-decoration: none; margin-left: 16px; }}
footer.foot strong {{ color: {p1}; }}
</style>
<div class="site">
<header class="nav">
  <div class="wide">
    <p class="logo">ketsu</p>
    <nav aria-label="Main">
      <ul>
        <li><a href="#" aria-current="page">Home</a></li>
        <li><a href="#">Families</a></li>
        <li><a href="#">Clinicians</a></li>
      </ul>
    </nav>
    <button type="button" class="btn btn-brand">Sign up</button>
  </div>
</header>

<main class="wide">
  <section class="hero">
    <div>
      <p class="eyebrow">Type 1, for kids and parents</p>
      <h1>Growing up with diabetes just got a little easier</h1>
      <p class="lede">Ketsu connects to a CGM and turns the day into something a child can follow: what changed, what to do next, and why it mattered.</p>
      <div class="cta">
        <button type="button" class="btn btn-primary">Start playing</button>
        <button type="button" class="btn btn-secondary">Meet the team</button>
      </div>
    </div>
    <div class="panel" aria-label="Sample day">
      <div class="panel-top"><strong style="color:{p3};">Today</strong><span>CGM · live</span></div>
      <p class="glucose">112<small>mg/dL</small></p>
      <div class="track" aria-hidden="true"><span></span></div>
      <div class="metrics">{"".join(metrics)}</div>
      <div class="alert"><span>Overnight low at 2:14 a.m.</span><strong>Review</strong></div>
    </div>
  </section>

  <section>
    <h2>How a day actually works</h2>
    <p class="sub">Connect a CGM, see the day clearly, and give your child a reason to check back tomorrow.</p>
    <div class="steps">
      <article class="step"><b>1</b><h3>See the trend</h3><p>A reading without the last hour is just a number. Ketsu shows where it is headed.</p></article>
      <article class="step"><b>2</b><h3>Know what to do</h3><p>Short guidance for meals, activity, and sleep. Dosing stays with your care team.</p></article>
      <article class="step"><b>3</b><h3>Keep showing up</h3><p>Check-ins earn progress. The goal is a habit, not a perfect graph.</p></article>
    </div>
  </section>

  <section>
    <div class="band">
      <div>
        <h2>Ready when your child is</h2>
        <p>A family account takes a few minutes. Bring the CGM you already use.</p>
      </div>
      <button type="button" class="btn btn-on-dark">Create account</button>
    </div>
  </section>

  <footer class="foot">
    <p><strong>ketsu</strong> · helping kids understand glucose</p>
    <p><a href="#">Privacy</a><a href="#">Support</a></p>
  </footer>
</main>
</div>"""


def render_palette_demo(
    palette: dict,
    primary: list[dict] | None = None,
    accent: list[dict] | None = None,
    neutrals: dict[str, str] | None = None,
) -> None:
    if primary is None or accent is None or neutrals is None:
        primary, accent, neutrals = page_swatches(palette)
    st.html(_page_html(primary, accent, neutrals), width="stretch")
