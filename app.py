import streamlit as st
import pandas as pd
import json
import plotly.graph_objects as go
from scoring import (
    TRAITS,
    TRAIT_DETAILS,
    QUESTIONS,
    score_responses,
    trait_description,
    interpretation,
    get_personality_archetype,
)

st.set_page_config(
    page_title="OCEAN MindScope | Big Five Assessment",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom High-End Styling (Glassmorphism, Vibrant Gradients & Modern Typography)
CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@500;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
}

/* Background subtle ambient glow */
.stApp {
    background: radial-gradient(circle at 15% 15%, rgba(139, 92, 246, 0.08) 0%, transparent 40%),
                radial-gradient(circle at 85% 85%, rgba(6, 182, 212, 0.08) 0%, transparent 40%),
                radial-gradient(circle at 50% 50%, rgba(244, 63, 94, 0.04) 0%, transparent 60%);
}

/* Header & Typography */
.hero-container {
    text-align: center;
    padding: 2.5rem 1.5rem 2rem 1.5rem;
    background: linear-gradient(135deg, rgba(30, 41, 59, 0.8) 0%, rgba(15, 23, 42, 0.95) 100%);
    border: 1.5px solid rgba(168, 85, 247, 0.35);
    border-radius: 24px;
    backdrop-filter: blur(16px);
    margin-bottom: 2rem;
    box-shadow: 0 20px 50px -10px rgba(0, 0, 0, 0.5);
}

.hero-pill {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: linear-gradient(135deg, rgba(139, 92, 246, 0.25), rgba(217, 70, 239, 0.25));
    border: 1px solid rgba(168, 85, 247, 0.5);
    color: #d8b4fe;
    padding: 6px 18px;
    border-radius: 9999px;
    font-size: 0.88rem;
    font-weight: 700;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    margin-bottom: 1rem;
}

.hero-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2.9rem;
    font-weight: 800;
    line-height: 1.15;
    background: linear-gradient(135deg, #FFFFFF 15%, #F1F5F9 50%, #C084FC 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.8rem;
}

.hero-subtitle {
    font-size: 1.12rem;
    color: #E2E8F0;
    max-width: 720px;
    margin: 0 auto 1.4rem auto;
    line-height: 1.65;
}

/* Feature badges row */
.meta-chips {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 12px;
}

.chip {
    background: rgba(255, 255, 255, 0.08);
    border: 1px solid rgba(255, 255, 255, 0.15);
    color: #F1F5F9;
    padding: 7px 16px;
    border-radius: 12px;
    font-size: 0.88rem;
    font-weight: 600;
}

/* Trait Category Header Card */
.trait-banner {
    padding: 1.2rem 1.6rem;
    border-radius: 18px;
    margin: 1.8rem 0 1rem 0;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border: 1px solid rgba(255, 255, 255, 0.1);
    box-shadow: 0 10px 25px -10px rgba(0,0,0,0.25);
}

.trait-banner-title {
    font-size: 1.4rem;
    font-weight: 700;
    color: #FFFFFF;
    display: flex;
    align-items: center;
    gap: 10px;
    margin: 0;
}

.trait-banner-desc {
    color: #CBD5E1;
    font-size: 0.92rem;
    margin-top: 4px;
}

/* Question Card */
.q-box {
    background: rgba(30, 41, 59, 0.35);
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 16px;
    padding: 1.2rem 1.4rem;
    margin-bottom: 1.2rem;
    transition: all 0.25s ease;
}

.q-box:hover {
    border-color: rgba(168, 85, 247, 0.3);
    background: rgba(30, 41, 59, 0.55);
    transform: translateY(-1px);
}

.q-number {
    font-size: 0.78rem;
    font-weight: 700;
    color: #A855F7;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 6px;
}

.q-text {
    font-size: 1.05rem;
    font-weight: 600;
    color: #F8FAFC;
    line-height: 1.45;
    margin-bottom: 0.8rem;
}

/* Archetype Showcase Card */
.archetype-card {
    background: linear-gradient(135deg, rgba(30, 41, 59, 0.85) 0%, rgba(15, 23, 42, 0.95) 100%);
    border: 1.5px solid rgba(168, 85, 247, 0.4);
    border-radius: 24px;
    padding: 2.2rem;
    box-shadow: 0 25px 50px -12px rgba(139, 92, 246, 0.25);
    margin: 1.5rem 0 2.5rem 0;
    position: relative;
    overflow: hidden;
}

.archetype-badge {
    font-size: 3rem;
    margin-bottom: 0.5rem;
}

.archetype-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2.2rem;
    font-weight: 800;
    background: linear-gradient(135deg, #FFFFFF 0%, #E0E7FF 60%, #C084FC 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0;
}

.archetype-tagline {
    font-size: 1.15rem;
    font-style: italic;
    color: #F472B6;
    margin-top: 6px;
    margin-bottom: 1.2rem;
}

.archetype-bio {
    font-size: 1.05rem;
    line-height: 1.7;
    color: #E2E8F0;
    max-width: 900px;
}

/* Deep-dive trait card */
.dive-card {
    background: rgba(30, 41, 59, 0.45);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 18px;
    padding: 1.4rem;
    margin-bottom: 1.2rem;
    height: 100%;
}

.dive-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.8rem;
}

.dive-title {
    font-size: 1.2rem;
    font-weight: 700;
    color: #FFFFFF;
    display: flex;
    align-items: center;
    gap: 8px;
}

.score-badge {
    padding: 4px 12px;
    border-radius: 9999px;
    font-size: 0.85rem;
    font-weight: 700;
    color: #FFFFFF;
}

.progress-track {
    width: 100%;
    height: 10px;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 9999px;
    margin: 0.8rem 0 1rem 0;
    overflow: hidden;
}

.progress-fill {
    height: 100%;
    border-radius: 9999px;
    transition: width 0.6s ease;
}

/* Insight Cards */
.insight-box {
    background: rgba(30, 41, 59, 0.35);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 18px;
    padding: 1.6rem;
    height: 100%;
}

.insight-header {
    font-size: 1.15rem;
    font-weight: 700;
    color: #FFFFFF;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    gap: 8px;
}

/* Custom Likert Radio button styling */
div[role="radiogroup"] > label {
    padding: 6px 12px !important;
    border-radius: 8px !important;
    transition: background-color 0.2s ease !important;
}

div[role="radiogroup"] > label:hover {
    background-color: rgba(255, 255, 255, 0.06) !important;
}

/* Button glow styling */
div.stButton > button {
    border-radius: 12px !important;
    font-weight: 600 !important;
}

div.stButton > button[data-testid="baseButton-primary"],
div.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #8B5CF6 0%, #EC4899 100%) !important;
    border: none !important;
    color: #FFFFFF !important;
    font-size: 1.1rem !important;
    font-weight: 700 !important;
    padding: 0.75rem 2rem !important;
    border-radius: 14px !important;
    box-shadow: 0 10px 25px -5px rgba(236, 72, 153, 0.45) !important;
    transition: all 0.25s ease !important;
}

div.stButton > button[data-testid="baseButton-primary"]:hover,
div.stButton > button[kind="primary"]:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 15px 30px -5px rgba(236, 72, 153, 0.65) !important;
}

div.stButton > button[data-testid="baseButton-secondary"],
div.stButton > button:not([kind="primary"]):not([data-testid="baseButton-primary"]) {
    background: #1E293B !important;
    border: 1px solid rgba(255, 255, 255, 0.2) !important;
    color: #FFFFFF !important;
    border-radius: 12px !important;
    transition: all 0.2s ease !important;
}

div.stButton > button[data-testid="baseButton-secondary"]:hover,
div.stButton > button:not([kind="primary"]):not([data-testid="baseButton-primary"]):hover {
    background: rgba(168, 85, 247, 0.3) !important;
    border-color: rgba(168, 85, 247, 0.6) !important;
    color: #FFFFFF !important;
    transform: translateY(-1px) !important;
}
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ----------------- SESSION STATE MANAGEMENT -----------------
if "assessment_answers" not in st.session_state:
    st.session_state.assessment_answers = {}

if "calculated_scores" not in st.session_state:
    st.session_state.calculated_scores = None

if "user_nickname" not in st.session_state:
    st.session_state.user_nickname = ""

# ----------------- HERO HEADER -----------------
st.markdown(
    """
    <div class="hero-container">
        <div class="hero-pill">✨ OCEAN Behavioral Diagnostics</div>
        <div class="hero-title">Discover Your Mind's Architecture</div>
        <div class="hero-subtitle">
            Move beyond generic quizzes. Explore 25 vibrant, real-world behavioral scenarios to uncover your 
            Big Five psychological archetype, unique cognitive superpowers, and pressure dynamics.
        </div>
        <div class="meta-chips">
            <span class="chip">🎯 25 Relatable Scenarios</span>
            <span class="chip">⏱️ ~3 Min Completion</span>
            <span class="chip">📊 High-Res Polar Radar</span>
            <span class="chip">🧬 Archetype Persona Synthesis</span>
            <span class="chip">🔒 100% Client-Side Privacy</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ----------------- SIDEBAR & UTILITIES -----------------
with st.sidebar:
    st.markdown("### ⚙️ Quick Actions")
    nickname_input = st.text_input(
        "Your Name or Handle",
        value=st.session_state.user_nickname,
        placeholder="e.g., Alex or Explorer",
        help="Optional. Will be featured on your final archetype scorecard.",
    )
    if nickname_input != st.session_state.user_nickname:
        st.session_state.user_nickname = nickname_input

    st.markdown("---")
    st.markdown("#### 🎲 Instant Preview")
    st.caption("Want to test-drive the dashboard immediately without clicking all 25 questions?")

    col_demo1, col_demo2 = st.columns(2)
    with col_demo1:
        if st.button("Creative Spark", use_container_width=True, type="secondary"):
            st.session_state.assessment_answers = {
                "O1": 5, "O2": 5, "O3": 5, "O4": 1, "O5": 5,
                "C1": 3, "C2": 4, "C3": 4, "C4": 2, "C5": 4,
                "E1": 5, "E2": 4, "E3": 5, "E4": 2, "E5": 5,
                "A1": 4, "A2": 4, "A3": 4, "A4": 2, "A5": 4,
                "N1": 2, "N2": 2, "N3": 4, "N4": 2, "N5": 2,
            }
            if not st.session_state.user_nickname:
                st.session_state.user_nickname = "Alex (Pioneer)"
            st.session_state.calculated_scores = score_responses(st.session_state.assessment_answers)
            st.rerun()

    with col_demo2:
        if st.button("Zen Strategist", use_container_width=True, type="secondary"):
            st.session_state.assessment_answers = {
                "O1": 4, "O2": 3, "O3": 4, "O4": 3, "O5": 4,
                "C1": 1, "C2": 5, "C3": 5, "C4": 1, "C5": 5,
                "E1": 2, "E2": 3, "E3": 2, "E4": 5, "E5": 2,
                "A1": 4, "A2": 3, "A3": 3, "A4": 3, "A5": 3,
                "N1": 1, "N2": 1, "N3": 5, "N4": 1, "N5": 1,
            }
            if not st.session_state.user_nickname:
                st.session_state.user_nickname = "Morgan (Strategist)"
            st.session_state.calculated_scores = score_responses(st.session_state.assessment_answers)
            st.rerun()

    if st.button("🔄 Reset Questionnaire", use_container_width=True):
        st.session_state.assessment_answers = {}
        st.session_state.calculated_scores = None
        st.rerun()

    st.markdown("---")
    st.markdown("### 📚 The OCEAN Framework")
    for trait_key, details in TRAIT_DETAILS.items():
        st.markdown(
            f"**{details['icon']} {trait_key}**  \n"
            f"<small style='color: #94A3B8;'>{details['subtitle']}</small>",
            unsafe_allow_html=True,
        )

# ----------------- QUESTIONNAIRE SECTION -----------------
# Response scale mapping with evocative emoji pills
OPTIONS_MAP = {
    "1 — Strongly Disagree 🔴": 1,
    "2 — Disagree 🟠": 2,
    "3 — Neutral / Situational ⚪": 3,
    "4 — Agree 🟢": 4,
    "5 — Strongly Agree 🔥": 5,
}

REVERSE_OPTIONS_MAP = {v: k for k, v in OPTIONS_MAP.items()}

# If results are already generated, offer toggle to view or retake
if st.session_state.calculated_scores is not None:
    res_col1, res_col2 = st.columns([3, 1])
    with res_col1:
        st.success("🎉 **Profile Analysis Complete!** Scroll down to explore your interactive dashboard.")
    with res_col2:
        if st.button("✏️ Edit Answers", use_container_width=True):
            st.session_state.calculated_scores = None
            st.rerun()

# Display Questionnaire Tabs if not in finished view or if user wants to review
with st.expander("📝 The 25 Interactive Behavioral Prompts", expanded=(st.session_state.calculated_scores is None)):
    st.caption("Select the response that best describes your instinctual, default reaction in daily life.")

    tabs = st.tabs([
        f"{TRAIT_DETAILS[t]['icon']} {t}" for t in TRAITS
    ])

    with st.form("personality_questionnaire_form"):
        form_answers = dict(st.session_state.assessment_answers)

        for i, trait in enumerate(TRAITS):
            with tabs[i]:
                details = TRAIT_DETAILS[trait]
                st.markdown(
                    f"""
                    <div class="trait-banner" style="background: {details['gradient']}20; border-color: {details['color']}40;">
                        <div>
                            <h3 class="trait-banner-title">{details['icon']} {trait} — {details['alias']}</h3>
                            <div class="trait-banner-desc">{details['subtitle']}</div>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                for q_idx, q in enumerate(QUESTIONS[trait], 1):
                    current_val = form_answers.get(q["id"], None)
                    current_idx = list(OPTIONS_MAP.values()).index(current_val) if current_val else None

                    st.markdown(
                        f"""
                        <div class="q-box">
                            <div class="q-number">Prompt {q['id']} • {trait}</div>
                            <div class="q-text">{q['text']}</div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                    chosen = st.radio(
                        label=f"Response for {q['id']}",
                        options=list(OPTIONS_MAP.keys()),
                        index=current_idx,
                        key=f"radio_{q['id']}",
                        horizontal=True,
                        label_visibility="collapsed",
                    )
                    if chosen:
                        form_answers[q["id"]] = OPTIONS_MAP[chosen]

        st.markdown("<br>", unsafe_allow_html=True)
        submitted = st.form_submit_button(
            "✨ Calculate & Reveal My Personality Archetype",
            type="primary",
            use_container_width=True,
        )

        if submitted:
            # Check completeness
            missing = [
                q["id"]
                for qs in QUESTIONS.values()
                for q in qs
                if q["id"] not in form_answers or form_answers[q["id"]] is None
            ]
            if missing:
                st.error(
                    f"⚠️ Please complete all questions! ({len(missing)} remaining across tabs). "
                    "Or use the 'Quick Preview' presets in the sidebar to test instantly."
                )
            else:
                st.session_state.assessment_answers = form_answers
                st.session_state.calculated_scores = score_responses(form_answers)
                st.rerun()


# ----------------- DASHBOARD & RESULTS PRESENTATION -----------------
if st.session_state.calculated_scores is not None:
    scores = st.session_state.calculated_scores
    archetype = get_personality_archetype(scores)
    user_name = st.session_state.user_nickname.strip() or "Explorer"

    st.markdown("---")

    # 1. ARCHETYPE SHOWCASE HERO CARD
    st.markdown(
        f"""
        <div class="archetype-card">
            <div class="archetype-badge">{archetype['icon']}</div>
            <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 10px;">
                <div>
                    <h2 class="archetype-title">{user_name}'s Archetype: {archetype['title']}</h2>
                    <div class="archetype-tagline">“{archetype['tagline']}”</div>
                </div>
                <div class="hero-pill" style="margin: 0; background: rgba(168, 85, 247, 0.25);">
                    Validated Profile • 100 pt Scale
                </div>
            </div>
            <div class="archetype-bio">{archetype['bio']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 2. CHARTS SECTION (RADAR + TRAIT SPECTRUM)
    chart_col1, chart_col2 = st.columns([1, 1], gap="medium")

    with chart_col1:
        st.markdown("### 🕸️ Polar Mind Radar")
        st.caption("Visual representation of trait dimensions radiating outward from balance (0 to 100).")

        radar_categories = [
            "Openness (Curiosity)",
            "Conscientiousness (Drive)",
            "Extraversion (Energy)",
            "Agreeableness (Empathy)",
            "Stress Reactivity (Neuroticism)",
        ]
        radar_values = [
            scores["Openness"],
            scores["Conscientiousness"],
            scores["Extraversion"],
            scores["Agreeableness"],
            scores["Neuroticism"],
        ]
        # Close radar loop
        radar_categories_closed = radar_categories + [radar_categories[0]]
        radar_values_closed = radar_values + [radar_values[0]]

        fig_radar = go.Figure()

        # Benchmark background polygon (Average 50%)
        fig_radar.add_trace(
            go.Scatterpolar(
                r=[50, 50, 50, 50, 50, 50],
                theta=radar_categories_closed,
                fill="toself",
                fillcolor="rgba(148, 163, 184, 0.08)",
                line=dict(color="rgba(148, 163, 184, 0.3)", dash="dash", width=1),
                name="Population Benchmark (50%)",
                hoverinfo="skip",
            )
        )

        # User's Polygon
        fig_radar.add_trace(
            go.Scatterpolar(
                r=radar_values_closed,
                theta=radar_categories_closed,
                fill="toself",
                fillcolor="rgba(168, 85, 247, 0.35)",
                line=dict(color="#A855F7", width=3),
                marker=dict(size=8, color="#F43F5E"),
                name=f"{user_name}'s Profile",
                hovertemplate="%{theta}: <b>%{r:.1f}</b>/100<extra></extra>",
            )
        )

        fig_radar.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100],
                    tickvals=[25, 50, 75, 100],
                    tickfont=dict(size=9, color="#94A3B8"),
                    gridcolor="rgba(255, 255, 255, 0.08)",
                ),
                angularaxis=dict(
                    tickfont=dict(size=11, color="#E2E8F0", family="Plus Jakarta Sans"),
                    gridcolor="rgba(255, 255, 255, 0.08)",
                    linecolor="rgba(255, 255, 255, 0.15)",
                ),
                bgcolor="rgba(0,0,0,0)",
            ),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            showlegend=True,
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=-0.2,
                xanchor="center",
                x=0.5,
                font=dict(color="#94A3B8"),
            ),
            margin=dict(l=40, r=40, t=20, b=40),
            height=390,
        )

        st.plotly_chart(fig_radar, use_container_width=True, config={"displayModeBar": False})

    with chart_col2:
        st.markdown("### 📊 Trait Spectrum Breakdown")
        st.caption("Normalized scores benchmarked across low (<36), balanced (36-65), and high (>65) spectrums.")

        trait_names = TRAITS
        trait_scores = [scores[t] for t in trait_names]
        colors = [TRAIT_DETAILS[t]["color"] for t in trait_names]

        fig_bar = go.Figure()

        # Add benchmark shaded bands
        fig_bar.add_vrect(x0=0, x1=35, fillcolor="rgba(148, 163, 184, 0.05)", line_width=0, layer="below")
        fig_bar.add_vrect(x0=35, x1=65, fillcolor="rgba(148, 163, 184, 0.1)", line_width=0, layer="below")
        fig_bar.add_vrect(x0=65, x1=100, fillcolor="rgba(148, 163, 184, 0.05)", line_width=0, layer="below")

        fig_bar.add_trace(
            go.Bar(
                y=trait_names,
                x=trait_scores,
                orientation="h",
                marker=dict(
                    color=colors,
                    line=dict(color="rgba(255, 255, 255, 0.2)", width=1),
                    opacity=0.9,
                ),
                text=[f"{v:.0f}%" for v in trait_scores],
                textposition="outside",
                textfont=dict(color="#FFFFFF", size=12, family="Plus Jakarta Sans"),
                hovertemplate="Trait: <b>%{y}</b><br>Score: <b>%{x:.1f}</b>/100<extra></extra>",
            )
        )

        fig_bar.update_layout(
            xaxis=dict(
                range=[0, 110],
                tickvals=[0, 35, 65, 100],
                ticktext=["0", "Low (35)", "Balanced (65)", "100"],
                gridcolor="rgba(255, 255, 255, 0.08)",
                tickfont=dict(color="#94A3B8"),
            ),
            yaxis=dict(
                autorange="reversed",
                tickfont=dict(color="#FFFFFF", size=13, family="Plus Jakarta Sans"),
            ),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            margin=dict(l=20, r=30, t=20, b=40),
            height=390,
        )

        st.plotly_chart(fig_bar, use_container_width=True, config={"displayModeBar": False})

    # 3. DEEP-DIVE TRAIT CARDS (2-Column Grid + Synergy Card)
    st.markdown("### 🔍 Granular Trait Analysis")
    st.caption("How each trait influences your choices, communication style, and blind spots.")

    row1_c1, row1_c2 = st.columns(2, gap="medium")
    row2_c1, row2_c2 = st.columns(2, gap="medium")
    row3_c1, row3_c2 = st.columns(2, gap="medium")

    card_slots = [row1_c1, row1_c2, row2_c1, row2_c2, row3_c1]

    for idx, trait in enumerate(TRAITS):
        details = TRAIT_DETAILS[trait]
        score_val = scores[trait]
        level, desc = trait_description(trait, score_val)

        badge_bg = (
            "rgba(16, 185, 129, 0.25)"
            if level == "High Range"
            else "rgba(6, 182, 212, 0.25)"
            if level == "Balanced Range"
            else "rgba(148, 163, 184, 0.25)"
        )

        with card_slots[idx]:
            st.markdown(
                f"""
                <div class="dive-card">
                    <div class="dive-header">
                        <div class="dive-title">{details['icon']} {trait} — <small style="font-size: 0.9rem; color: #94A3B8;">{details['alias']}</small></div>
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 4px;">
                        <span style="font-size: 1.7rem; font-weight: 800; color: #FFFFFF;">{score_val:.0f}<small style='font-size: 0.95rem; color: #94A3B8;'>/100</small></span>
                        <span class="score-badge" style="background: {badge_bg}; border: 1px solid {details['color']}80; color: #FFFFFF;">
                            {level.replace(' Range', '')}
                        </span>
                    </div>
                    <div class="progress-track">
                        <div class="progress-fill" style="width: {score_val}%; background: {details['gradient']};"></div>
                    </div>
                    <div style="font-size: 0.95rem; color: #CBD5E1; line-height: 1.65;">
                        {desc}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    # 6th Slot: Holistic OCEAN Synthesis Card
    with row3_c2:
        resilience_index = 100 - scores["Neuroticism"]
        clarity_index = (scores["Openness"] + scores["Conscientiousness"]) / 2
        st.markdown(
            f"""
            <div class="dive-card" style="border: 1px solid rgba(168, 85, 247, 0.35); background: linear-gradient(135deg, rgba(30, 41, 59, 0.6), rgba(15, 23, 42, 0.8));">
                <div class="dive-header">
                    <div class="dive-title">🧬 Profile Synergy Indices</div>
                </div>
                <div style="margin-top: 10px; color: #E2E8F0; font-size: 0.95rem; line-height: 1.6;">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
                        <span>🛡️ Pressure Resilience:</span>
                        <b style="color: #10B981;">{resilience_index:.0f}%</b>
                    </div>
                    <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
                        <span>💡 Strategic Clarity Index:</span>
                        <b style="color: #A855F7;">{clarity_index:.0f}%</b>
                    </div>
                    <div style="display: flex; justify-content: space-between; margin-bottom: 12px;">
                        <span>🤝 Interpersonal Warmth:</span>
                        <b style="color: #06B6D4;">{(scores['Extraversion'] + scores['Agreeableness'])/2:.0f}%</b>
                    </div>
                    <small style="color: #94A3B8;">
                        Synergies synthesize opposing and reinforcing traits across your OCEAN distribution.
                    </small>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # 4. SUPERPOWERS & GROWTH RADAR
    st.markdown("<br>", unsafe_allow_html=True)
    insight_c1, insight_c2, insight_c3 = st.columns([1, 1, 1], gap="medium")

    with insight_c1:
        st.markdown(
            f"""
            <div class="insight-box" style="border-top: 3px solid #10B981;">
                <div class="insight-header">🚀 Core Superpowers</div>
                <ul style="color: #E2E8F0; padding-left: 1.2rem; line-height: 1.7; font-size: 0.95rem;">
                    {''.join(f'<li style="margin-bottom: 0.6rem;">{sp}</li>' for sp in archetype['superpowers'])}
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with insight_c2:
        st.markdown(
            f"""
            <div class="insight-box" style="border-top: 3px solid #F59E0B;">
                <div class="insight-header">💡 Strategic Growth Areas</div>
                <ul style="color: #E2E8F0; padding-left: 1.2rem; line-height: 1.7; font-size: 0.95rem;">
                    {''.join(f'<li style="margin-bottom: 0.6rem;">{ga}</li>' for ga in archetype['growth_areas'])}
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with insight_c3:
        st.markdown(
            f"""
            <div class="insight-box" style="border-top: 3px solid #8B5CF6;">
                <div class="insight-header">🏢 Ideal Environment</div>
                <p style="color: #E2E8F0; line-height: 1.7; font-size: 0.95rem; margin-bottom: 1rem;">
                    {archetype['ideal_environment']}
                </p>
                <div style="background: rgba(255, 255, 255, 0.05); padding: 10px 14px; border-radius: 10px; border-left: 3px solid #C084FC;">
                    <small style="color: #CBD5E1;">“Self-awareness is not about changing your nature, but unlocking environments where your nature shines.”</small>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # 5. EXPORT & SHAREABILITY
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 📤 Export & Share Your Personality Dossier")

    down_c1, down_c2, down_c3 = st.columns(3)

    # CSV Data preparation
    df_export = pd.DataFrame([
        {
            "Candidate": user_name,
            "Trait": trait,
            "Score": scores[trait],
            "Band": interpretation(scores[trait])[0],
            "Archetype": archetype["title"],
        }
        for trait in TRAITS
    ])

    with down_c1:
        csv_data = df_export.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📥 Download CSV Report",
            data=csv_data,
            file_name=f"big_five_{user_name.lower().replace(' ', '_')}.csv",
            mime="text/csv",
            use_container_width=True,
        )

    with down_c2:
        json_payload = json.dumps({
            "candidate": user_name,
            "archetype": archetype,
            "scores": scores,
            "assessment_framework": "Big Five (OCEAN)",
        }, indent=2).encode("utf-8")
        st.download_button(
            label="📦 Download Full JSON Dossier",
            data=json_payload,
            file_name=f"personality_{user_name.lower().replace(' ', '_')}.json",
            mime="application/json",
            use_container_width=True,
        )

    with down_c3:
        share_summary = (
            f"🧠 My Big Five OCEAN Profile:\n"
            f"Archetype: {archetype['icon']} {archetype['title']}\n"
            f"• Openness: {scores['Openness']:.0f}%\n"
            f"• Conscientiousness: {scores['Conscientiousness']:.0f}%\n"
            f"• Extraversion: {scores['Extraversion']:.0f}%\n"
            f"• Agreeableness: {scores['Agreeableness']:.0f}%\n"
            f"• Neuroticism: {scores['Neuroticism']:.0f}%\n"
            f"Tagline: “{archetype['tagline']}”"
        )
        st.download_button(
            label="📋 Download Shareable Text Card",
            data=share_summary,
            file_name=f"archetype_card_{user_name.lower().replace(' ', '_')}.txt",
            mime="text/plain",
            use_container_width=True,
        )

st.markdown("<br><br>", unsafe_allow_html=True)
st.divider()
st.markdown(
    """
    <div style="text-align: center; color: #64748B; font-size: 0.85rem; padding-bottom: 2rem;">
        ⚡ Built with <b>Python</b>, <b>Streamlit</b>, and <b>Plotly</b> • 
        Educational Self-Reflection & Exploration Instrument • Not for clinical diagnosis or hiring evaluations.
    </div>
    """,
    unsafe_allow_html=True,
)
