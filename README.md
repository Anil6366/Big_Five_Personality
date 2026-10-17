# 🧠 OCEAN MindScope — Big Five Personality Assessment

An interactive behavioral assessment web application based on the scientific Big Five (OCEAN) personality framework. Users answer 25 situational real-world prompts, discover their unique **Personality Archetype** (e.g., *The Trailblazing Catalyst*, *The Visionary Architect*, *The Zen Strategist*), view high-resolution **Plotly Polar Radar** and **Spectrum** charts, explore cross-trait synergy indices, and export their full dossier.

---

## ✨ Features

- **25 Relatable, Engaging Prompts**: 5 situational prompts per trait designed to minimize survey fatigue and capture instinctual reactions.
- **Scientifically Balanced Scoring**: Reverse-scored items to prevent straight-lining and acquiescence bias.
- **Personality Archetype Synthesis**: Dynamic archetype generator identifying dominant traits, superpowers, growth areas, and ideal work/social environments.
- **High-Res Interactive Polar Mind Radar**: Radar chart built with Plotly comparing personal profile against population benchmarks.
- **Horizontal Trait Spectrum**: Clean breakdown benchmarked across Low (<36), Balanced (36–65), and High (>65) spectrums.
- **Profile Synergy Indices**: Evaluates emergent cross-trait combinations (e.g., *Pressure Resilience*, *Strategic Clarity*, *Interpersonal Warmth*).
- **One-Click Instant Presets**: Built-in preview presets in the sidebar (*Creative Spark*, *Zen Strategist*) for fast test-driving.
- **Multi-Format Export**: One-click download of results as **CSV**, **Full JSON Dossier**, or **Shareable Text Card**.
- **Dark Glassmorphism UI**: Styled with Google Fonts (`Plus Jakarta Sans` & `Space Grotesk`), vibrant neon gradients, and responsive cards.

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Streamlit** — Web interface & reactive state management
- **Plotly** — High-resolution interactive charts
- **Pandas** — Data structuring & tabular reports
- **NumPy & Matplotlib** — Numerical calculations & auxiliary plotting

---

## 🚀 Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR-USERNAME/big-five-personality-assessment.git
   cd big-five-personality-assessment
   ```

2. **Create and activate a virtual environment (recommended):**
   - **Windows:**
     ```bash
     python -m venv .venv
     .venv\Scripts\activate
     ```
   - **macOS / Linux:**
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the application:**
   ```bash
   streamlit run app.py
   ```

5. Open your browser at `http://localhost:8501`.

---

## ☁️ Deploy for Free to Streamlit Community Cloud

1. Push this repository to your GitHub account.
2. Visit [share.streamlit.io](https://share.streamlit.io/) and log in with GitHub.
3. Click **"New app"**, select your repository, branch (`main`), and set the main file path to `app.py`.
4. Click **"Deploy"**!

---

## 📁 Project Structure

```text
big-five-personality-assessment/
├── .streamlit/
│   └── config.toml          # Custom dark modern theme configuration
├── app.py                   # Main Streamlit dashboard & reactive UI
├── scoring.py               # Question bank, scoring algorithm & archetype generator
├── requirements.txt         # Project dependencies
├── README.md                # Documentation & setup guide
├── LICENSE                  # Open-source license
└── .gitignore               # Ignored files & virtual environments
```

---

## ⚖️ Limitations & Educational Disclaimer

This project is an educational self-reflection and exploration instrument. Scores are derived from self-reported answers and are intended for personal insight, team empathy, and learning. They are **not** clinical diagnoses and should **not** be used for hiring assessments, medical decisions, or high-stakes evaluations.
