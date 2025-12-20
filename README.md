# 📰 News Impact Forecaster (Agentic AI POC)

> **An Agentic AI system that analyzes current news and forecasts potential short‑ and medium‑term impacts using structured reasoning and uncertainty estimation.**

This project is inspired by the ideas explored in **MIRAI: Evaluating LLM Agents for Event Forecasting**, but is adapted into a **practical, portfolio‑ready MVP** focused on *impact forecasting* rather than deterministic prediction.

---

## 🚀 Project Motivation

Forecasting future events directly is unreliable and often misleading. However, **forecasting potential impacts and scenarios** based on current signals and historical analogies is both realistic and valuable.

This project demonstrates how **LLM agents**, when orchestrated correctly, can:
- Extract structured signals from unstructured news
- Ground reasoning in historical context
- Generate causal, scenario‑based forecasts
- Explicitly model uncertainty and risk

---

## 🎯 What This Project Does (MVP Scope)

**Input**
- A news headline or short article (manual input)

**Output**
- Structured forecast including:
  - Event summary
  - Short‑term impact
  - Medium‑term impact
  - Key assumptions
  - Risk & uncertainty analysis
  - Confidence score

**Important:**
- This system **does not predict exact outcomes or prices**
- It focuses on *impact assessment*, not deterministic forecasting

---

## 🧠 System Architecture (Agentic Design)

The system is implemented as a **LangGraph‑based multi‑agent workflow**.

```
User News Input
        ↓
Signal Extraction Agent
        ↓
Context Retrieval Agent (RAG)
        ↓
Impact Forecasting Agent
        ↓
Critic / Uncertainty Agent
        ↓
Final Structured Output
```

### Why LangGraph?
- Explicit state transitions
- Deterministic agent orchestration
- Easier debugging and evaluation
- Clear separation of responsibilities

---

## 🤖 Agent Responsibilities

### 1️⃣ Signal Extraction Agent
- Converts raw news into a structured event signal
- Extracts:
  - Event summary
  - Domain
  - Key actors
  - Time horizon
  - Urgency
- **No forecasting at this stage** (hallucination reduction)

---

### 2️⃣ Context Retrieval Agent
- Retrieves historical analogs or background information
- MVP uses a lightweight, stubbed retriever
- Designed to scale to vector‑based RAG (FAISS / Chroma)

---

### 3️⃣ Impact Forecasting Agent
- Performs causal reasoning
- Uses historical analogies when available
- Produces:
  - Short‑term impact
  - Medium‑term impact
  - Affected domains
  - Explicit assumptions

---

### 4️⃣ Critic / Uncertainty Agent ⭐
- Reviews the forecast critically
- Identifies:
  - Key risks
  - Alternative scenarios
  - Uncertainty level
- Assigns a confidence score (0–1)

This agent is critical for avoiding overconfidence and mirrors real‑world decision‑making systems.

---

## 🗂️ Project Structure

```
news-impact-forecaster/
│
├── agents/                # Individual agent logic
├── graph/                 # LangGraph orchestration
├── prompts/               # Agent prompt templates
├── state.py               # Shared graph state definition
├── app.py                 # Streamlit UI
├── requirements.txt
└── README.md
```

---

## 🛠️ Tech Stack

- **Python**
- **LangChain**
- **LangGraph**
- **OpenAI / LLM API**
- **Streamlit** (UI)
- **FAISS / Chroma** (planned for RAG)

---

## 🔍 Design Decisions

### Why decompose into multiple agents?
- Reduces hallucinations
- Improves interpretability
- Allows independent testing and evaluation

### Why include a critic agent?
- Forecasting is inherently uncertain
- Confidence calibration is essential in real‑world systems
- Mirrors research‑grade evaluation approaches

---

## 📊 Evaluation Strategy (Planned)

Inspired by MIRAI, but simplified for MVP:
- Backtesting on historical news events
- Human plausibility review
- Consistency checks across similar inputs

---

## ⚠️ Limitations

- Uses a stubbed retrieval system in MVP
- No real‑time data ingestion
- No quantitative market prediction
- Relies on LLM reasoning quality

These limitations are **intentional** to maintain realism and clarity.

---

## 🔮 Future Improvements

- Vector‑based RAG with historical datasets
- Conditional graph routing based on confidence
- Parallel domain‑specific agents (economics, geopolitics)
- Automated backtesting framework
- Dashboard‑level analytics

---

## 📚 Inspiration

- *MIRAI: Evaluating LLM Agents for Event Forecasting*
- Research on agentic reasoning and uncertainty modeling

---

## 👤 Author

**Debosmita Chatterjee**  
Data Science & Applied AI Practitioner

---

## ⭐ Why This Project Matters

This project demonstrates:
- Agentic AI system design
- Responsible forecasting practices
- Research‑inspired but production‑aware thinking
- Practical use of LangGraph beyond demos

It is designed to be discussed, extended, and evaluated — not just run.

