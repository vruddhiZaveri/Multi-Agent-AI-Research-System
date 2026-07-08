import streamlit as st
from pipeline import run_research_pipeline

st.set_page_config(
    page_title="ResearchMind",
    page_icon="🧠",
    layout="wide",
)

# ---------- Custom Styling ----------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background: #0a0a0a;
    }

    #MainMenu, header, footer {visibility: hidden;}

    .block-container {
        padding-top: 2.5rem;
        max-width: 1100px;
    }

    /* Eyebrow + Logo */
    p.eyebrow {
        color: #FF6B35 !important;
        font-weight: 700 !important;
        font-size: 0.78rem !important;
        letter-spacing: 4px !important;
        text-align: center !important;
        margin: 0 0 0.9rem 0 !important;
        text-transform: uppercase;
    }
    p.logo-title {
        text-align: center !important;
        font-size: 4.6rem !important;
        font-weight: 900 !important;
        letter-spacing: -2.5px !important;
        margin: 0 !important;
        line-height: 1 !important;
        font-family: 'Inter', sans-serif !important;
    }
    .logo-title .white { color: #F7F7F7; }
    .logo-title .orange { color: #FF6B35; }
    p.logo-sub {
        text-align: center !important;
        color: #999 !important;
        font-size: 1.05rem !important;
        font-weight: 400 !important;
        max-width: 620px !important;
        margin: 1.3rem auto 3rem auto !important;
        line-height: 1.65 !important;
    }

    /* Section labels */
    p.section-label {
        color: #FF6B35 !important;
        font-weight: 700 !important;
        font-size: 0.75rem !important;
        letter-spacing: 2.5px !important;
        margin: 0 0 0.6rem 0 !important;
        text-transform: uppercase;
    }
    p.pipeline-label {
        color: #f2f2f2 !important;
        font-weight: 800 !important;
        font-size: 1.2rem !important;
        letter-spacing: -0.3px !important;
        margin: 0 0 1.1rem 0 !important;
    }

    /* Input */
    div[data-testid="stTextInput"] input {
        background: #141414;
        border: 1px solid #262626;
        border-radius: 10px;
        padding: 0.85rem 1rem;
        color: #f0f0f0;
        font-size: 0.95rem;
    }
    div[data-testid="stTextInput"] input:focus {
        border-color: #FF6B35;
        box-shadow: 0 0 0 1px #FF6B35;
    }

    /* Run button */
    div.stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #FF6B35, #FF8C42);
        border: none;
        border-radius: 10px;
        font-weight: 700;
        height: 3rem;
        color: #0a0a0a;
        transition: all 0.15s ease;
    }
    div.stButton > button[kind="primary"]:hover {
        box-shadow: 0 8px 20px rgba(255, 107, 53, 0.35);
        transform: translateY(-1px);
    }
    div.stButton > button[kind="secondary"] {
        background: #141414;
        border: 1px solid #262626;
        border-radius: 999px;
        color: #ccc;
        font-weight: 500;
        font-size: 0.85rem !important;
        letter-spacing: 0.1px !important;
        height: 2.6rem;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        padding: 0 1.1rem;
    }
    div.stButton > button[kind="secondary"] p {
        white-space: nowrap !important;
        overflow: hidden;
        text-overflow: ellipsis;
        font-size: 0.85rem !important;
    }
    div.stButton > button[kind="secondary"]:hover {
        border-color: #FF6B35;
        color: #FF6B35;
    }

    /* Pipeline step cards */
    .step-card {
        background: #121212;
        border: 1px solid #232323;
        border-radius: 12px;
        padding: 0.95rem 1.1rem;
        margin-bottom: 0.65rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .step-left { display: flex; gap: 0.85rem; align-items: flex-start; }
    .step-num {
        color: #FF6B35;
        font-weight: 800;
        font-size: 0.8rem;
        letter-spacing: 0.5px;
        margin-top: 0.15rem;
        font-variant-numeric: tabular-nums;
    }
    .step-name {
        color: #f5f5f5;
        font-weight: 700;
        font-size: 0.98rem;
        letter-spacing: -0.2px;
        line-height: 1.3;
    }
    .step-desc {
        color: #7a7a7a;
        font-size: 0.82rem;
        font-weight: 400;
        margin-top: 0.15rem;
        line-height: 1.4;
    }
    .step-badge {
        font-size: 0.65rem;
        font-weight: 700;
        letter-spacing: 1.2px;
        padding: 0.3rem 0.65rem;
        border-radius: 6px;
        white-space: nowrap;
        text-transform: uppercase;
    }
    .badge-waiting { color: #666; background: rgba(255,255,255,0.04); border: 1px solid #262626; }
    .badge-done { color: #FF6B35; background: rgba(255,107,53,0.12); border: 1px solid rgba(255,107,53,0.3); }
    .badge-running { color: #FFC145; background: rgba(255,193,69,0.1); border: 1px solid rgba(255,193,69,0.3); }

    /* Result card */
    .result-card {
        background: #121212;
        border: 1px solid #232323;
        border-radius: 14px;
        padding: 1.6rem 1.8rem;
        margin-top: 0.6rem;
    }

    /* Footer */
    p.footer-note {
        text-align: center !important;
        color: #4a4a4a !important;
        font-size: 0.8rem !important;
        font-weight: 400 !important;
        letter-spacing: 0.2px !important;
        margin-top: 2.5rem !important;
        padding-top: 1.4rem !important;
        border-top: 1px solid #1a1a1a !important;
    }

    div.stButton > button[kind="primary"] {
        font-size: 0.98rem !important;
        letter-spacing: 0.2px !important;
    }
    div.stButton > button[kind="secondary"] {
        font-size: 0.85rem !important;
        letter-spacing: 0.1px !important;
    }
</style>
""", unsafe_allow_html=True)

# ---------- Session State ----------
if "state" not in st.session_state:
    st.session_state.state = None
if "topic" not in st.session_state:
    st.session_state.topic = ""

EXAMPLE_TOPICS = ["LLM agents 2026", "CRISPR gene editing", "Fusion energy progress"]

# ---------- Header ----------
st.markdown('<p class="eyebrow">MULTI-AGENT AI SYSTEM</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="logo-title"><span class="white">Research</span><span class="orange">Mind</span></p>',
    unsafe_allow_html=True,
)
st.markdown(
    '<p class="logo-sub">Four specialized AI agents collaborate — searching, scraping, writing, '
    'and critiquing — to deliver a polished research report on any topic.</p>',
    unsafe_allow_html=True,
)

left, right = st.columns([1.3, 1], gap="large")

with left:
    st.markdown('<p class="section-label">RESEARCH TOPIC</p>', unsafe_allow_html=True)
    topic = st.text_input(
        "Research topic",
        placeholder="e.g. Quantum computing breakthroughs in 2026",
        value=st.session_state.topic,
        label_visibility="collapsed",
    )

    run_clicked = st.button("Run Research Pipeline", use_container_width=True, type="primary")

    st.markdown('<p class="section-label" style="margin-top:1.4rem;">TRY →</p>', unsafe_allow_html=True)
    chip_cols = st.columns(len(EXAMPLE_TOPICS), gap="small")
    picked_example = None
    for c, ex in zip(chip_cols, EXAMPLE_TOPICS):
        if c.button(ex, key=f"chip_{ex}", use_container_width=True):
            picked_example = ex

    if picked_example:
        st.session_state.topic = picked_example
        st.rerun()

    if st.session_state.state:
        if st.button("🗑️  Clear Results", use_container_width=True):
            st.session_state.state = None
            st.session_state.topic = ""
            st.rerun()

with right:
    st.markdown('<p class="pipeline-label">Pipeline</p>', unsafe_allow_html=True)

    done = st.session_state.state is not None
    steps = [
        ("01", "Search Agent", "Gathers recent web information"),
        ("02", "Reader Agent", "Scrapes & extracts deep context"),
        ("03", "Writer Chain", "Drafts the full research report"),
        ("04", "Critic Chain", "Reviews & scores the report"),
    ]
    for num, name, desc in steps:
        badge_class = "badge-done" if done else "badge-waiting"
        badge_text = "DONE" if done else "WAITING"
        st.markdown(f"""
        <div class="step-card">
            <div class="step-left">
                <span class="step-num">{num}</span>
                <div>
                    <div class="step-name">{name}</div>
                    <div class="step-desc">{desc}</div>
                </div>
            </div>
            <span class="step-badge {badge_class}">{badge_text}</span>
        </div>
        """, unsafe_allow_html=True)

# ---------- Run Pipeline ----------
if run_clicked:
    if not topic.strip():
        st.warning("Please enter a topic before running the pipeline.")
    else:
        st.session_state.topic = topic
        with st.spinner("Running agents... this can take a minute ⏳"):
            try:
                st.session_state.state = run_research_pipeline(topic)
                st.rerun()
            except Exception as e:
                st.error(f"Pipeline failed: {e}")

# ---------- Results ----------
state = st.session_state.state

if state:
    st.markdown("<br>", unsafe_allow_html=True)
    st.success(f"✅ Research complete for: **{st.session_state.topic}**")

    tab_report, tab_feedback, tab_search, tab_reader = st.tabs(
        ["📄  Final Report", "🧐  Critic Feedback", "🔍  Search Results", "📖  Scraped Content"]
    )

    with tab_report:
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown(state.get("report", "_No report generated._"))
        st.markdown('</div>', unsafe_allow_html=True)
        st.download_button(
            "⬇️  Download Report (.md)",
            data=str(state.get("report", "")),
            file_name=f"{st.session_state.topic.replace(' ', '_')}_report.md",
            mime="text/markdown",
        )

    with tab_feedback:
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown(state.get("feedback", "_No feedback generated._"))
        st.markdown('</div>', unsafe_allow_html=True)

    with tab_search:
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.text(state.get("search_result", "_No search results._"))
        st.markdown('</div>', unsafe_allow_html=True)

    with tab_reader:
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.text(state.get("reader_result", "_No scraped content._"))
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown(
    '<p class="footer-note">ResearchMind · Powered by LangChain multi-agent pipeline · Built with Streamlit</p>',
    unsafe_allow_html=True,
)