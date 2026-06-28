import time
import streamlit as st
from pipeline import run_pipeline

# ==========================================================
# PAGE CONFIG
# ==========================================================
st.set_page_config(
    page_title="Multi-Agent Research System",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==========================================================
# CUSTOM CSS — Modern, colorful, eye-catching
# ==========================================================
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Poppins', sans-serif;
    }

    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        color: #f5f5f5;
    }

    /* Hero header */
    .hero-title {
        font-size: 3rem;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(90deg, #ff6ec4, #7873f5, #4ade80, #facc15);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradientShift 6s ease infinite;
        margin-bottom: 0;
    }

    .hero-subtitle {
        text-align: center;
        font-size: 1.1rem;
        color: #c9c9e8;
        margin-top: 0;
        margin-bottom: 1.5rem;
    }

    @keyframes gradientShift {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    /* Card style */
    .card {
        background: rgba(255, 255, 255, 0.06);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 18px;
        padding: 1.6rem 1.8rem;
        margin-bottom: 1.3rem;
        backdrop-filter: blur(8px);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.25);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .card:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 36px rgba(0, 0, 0, 0.35);
    }

    .card-header {
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 0.8rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    .scraped-header { color: #4ade80; }
    .report-header { color: #facc15; }
    .critic-header { color: #ff6ec4; }

    .badge {
        display: inline-block;
        padding: 0.25rem 0.8rem;
        border-radius: 999px;
        font-size: 0.75rem;
        font-weight: 600;
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }

    .badge-done {
        background: rgba(74, 222, 128, 0.18);
        color: #4ade80;
        border: 1px solid #4ade80;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1a2e, #16213e);
        border-right: 1px solid rgba(255,255,255,0.08);
    }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(90deg, #7873f5, #ff6ec4);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.7rem 1.4rem;
        font-weight: 700;
        font-size: 1rem;
        width: 100%;
        transition: 0.25s ease;
        box-shadow: 0 4px 18px rgba(120, 115, 245, 0.4);
    }
    .stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 6px 24px rgba(255, 110, 196, 0.5);
    }

    /* Text input */
    .stTextInput > div > div > input {
        background: rgba(255,255,255,0.08);
        color: white;
        border-radius: 10px;
        border: 1px solid rgba(255,255,255,0.18);
        padding: 0.6rem;
    }

    /* Divider line */
    .divider {
        height: 2px;
        background: linear-gradient(90deg, transparent, #7873f5, #ff6ec4, transparent);
        margin: 1.5rem 0;
        border: none;
    }

    /* Step pill row */
    .step-pill {
        padding: 0.5rem 1rem;
        border-radius: 999px;
        font-size: 0.85rem;
        font-weight: 600;
        text-align: center;
        margin: 0 0.3rem;
        transition: 0.3s;
    }
    .step-pending { background: rgba(255,255,255,0.06); color: #888; }
    .step-active  { background: rgba(120,115,245,0.3); color: #fff; border: 1px solid #7873f5; }
    .step-complete { background: rgba(74,222,128,0.2); color: #4ade80; border: 1px solid #4ade80; }

    footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

# ==========================================================
# HEADER
# ==========================================================
st.markdown('<p class="hero-title">🧠 AI Research Agent</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="hero-subtitle">Multi-Agent Pipeline · Search → Read → Write → Critique</p>',
    unsafe_allow_html=True,
)

# ==========================================================
# SIDEBAR
# ==========================================================
with st.sidebar:
    st.markdown("## ⚙️ Control Panel")
    st.markdown("---")
    st.markdown(
        """
        **How it works**

        1. 🔍 **Search Agent** finds reliable sources
        2. 📄 **Reader Agent** scrapes the best one
        3. ✍️ **Writer** drafts a full report
        4. 🧐 **Critic** reviews & gives feedback

        *(Search-agent raw data is hidden — only refined results are shown)*
        """
    )
    st.markdown("---")
    st.caption("Built with ❤️ using LangChain + Streamlit")

# ==========================================================
# MAIN INPUT
# ==========================================================
col1, col2 = st.columns([4, 1])
with col1:
    topic = st.text_input(
        "Enter your research topic",
        placeholder="e.g. Latest breakthroughs in quantum computing",
        label_visibility="collapsed",
    )
with col2:
    run_clicked = st.button("🚀 Run Research")

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ==========================================================
# PIPELINE EXECUTION
# ==========================================================
if run_clicked:
    if not topic.strip():
        st.warning("⚠️ Please enter a topic before running the pipeline.")
    else:
        step_placeholder = st.empty()
        status_box = st.empty()

        steps = ["🔍 Search", "📄 Read", "✍️ Write", "🧐 Critique"]

        def render_steps(active_index):
            cols = step_placeholder.columns(len(steps))
            for i, (col, step) in enumerate(zip(cols, steps)):
                if i < active_index:
                    css_class = "step-complete"
                elif i == active_index:
                    css_class = "step-active"
                else:
                    css_class = "step-pending"
                col.markdown(
                    f'<div class="step-pill {css_class}">{step}</div>',
                    unsafe_allow_html=True,
                )

        render_steps(0)
        with status_box.container():
            with st.spinner("Agents are working on your topic... this may take a minute ⏳"):
                try:
                    result = run_pipeline(topic)
                except Exception as e:
                    st.error(f"❌ Pipeline failed: {e}")
                    st.stop()

        render_steps(len(steps))
        status_box.empty()

        st.success("✅ Research pipeline completed successfully!")
        st.markdown('<hr class="divider">', unsafe_allow_html=True)

        # ---------------- Scraped Content ----------------
        st.markdown(
            """
            <div class="card">
                <div class="card-header scraped-header">
                    📄 Scraped Source Content
                    <span class="badge badge-done">Done</span>
                </div>
            """,
            unsafe_allow_html=True,
        )
        with st.expander("View scraped content", expanded=False):
            st.write(result.get("scraped_content", "No content available."))
        st.markdown("</div>", unsafe_allow_html=True)

        # ---------------- Final Report ----------------
        st.markdown(
            """
            <div class="card">
                <div class="card-header report-header">
                    📝 Final Research Report
                    <span class="badge badge-done">Done</span>
                </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(result.get("report", "No report generated."))
        st.markdown("</div>", unsafe_allow_html=True)

        st.download_button(
            label="⬇️ Download Report as Markdown",
            data=str(result.get("report", "")),
            file_name=f"{topic.strip().replace(' ', '_')}_report.md",
            mime="text/markdown",
        )

        # ---------------- Critic Feedback ----------------
        st.markdown(
            """
            <div class="card">
                <div class="card-header critic-header">
                    🧐 Critic Feedback
                    <span class="badge badge-done">Done</span>
                </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(result.get("feedback", "No feedback generated."))
        st.markdown("</div>", unsafe_allow_html=True)

else:
    st.info("👆 Enter a topic above and click **Run Research** to start the agents.")