import sys
import os

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from pipeline.run_pipeline import run_full_pipeline
import streamlit as st
import json



st.set_page_config(
    page_title="Agentic News Impact Forecasting",
    layout="wide"
)

st.title("🧠 Agentic News Impact Forecasting (MVP)")
st.caption(
    "Multi-agent system inspired by MIRAI for forecasting event impact using LLM agents"
)

st.divider()

# --- Input Section ---
st.subheader("📰 Input News Article")

news_text = st.text_area(
    "Paste a news article or headline",
    height=200,
    placeholder="Example: The European Central Bank announced potential stimulus measures amid slowing growth..."
)

run_button = st.button("🔍 Run Forecast")

if run_button:
    if not news_text.strip():
        st.warning("Please enter some news text.")
    else:
        with st.spinner("Running agents..."):
            try:
                result = run_full_pipeline(news_text)

                signal = result["signal"]
                context = result["context"]
                forecast = result["forecast"]

                st.success("Forecast generated successfully!")

                st.divider()

                # --- Layout ---
                col1, col2, col3 = st.columns(3)

                with col1:
                    st.subheader("📌 Signal Extraction")
                    st.json(signal)

                with col2:
                    st.subheader("📚 Context Retrieval")
                    st.json(context)

                with col3:
                    st.subheader("📈 Impact Forecast")
                    st.json(forecast)

            except Exception as e:
                st.error(f"Error running pipeline: {e}")

st.divider()

st.caption(
    "Built with LangChain agents • Structured reasoning • Deterministic outputs"
)
