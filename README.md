# 🤖 AI Business Assistant – Multi-Agent AI for Smarter Business Decisions

A modern, commercial-grade enterprise SaaS web application built with **Python, Streamlit, Pandas, and Plotly**. The application delivers real-time decision intelligence across Sales, Marketing, Customer Retention, Support Operations, and Market Research.

The user interface and backend architecture are engineered from the ground up to connect seamlessly with **LangGraph multi-agent workflows, SQLite transactional databases, vector RAG pipelines, and external enterprise APIs**.

---

## 🚀 Key Features & Enterprise Modules

### 1. 🏠 Executive Decision Center (Dashboard)
- **C-Suite Metric Cards**: ARR ($1.25M, +18.4% YoY), Pipeline ($2.84M), Blended CAC ($482), CSAT (94.2%).
- **Interactive Revenue Trajectory**: 12-month actuals vs. quota target vs. LangGraph AI forecasted trajectory.
- **Live Swarm Pulse**: Real-time event feed capturing autonomous cross-department agent signals.
- **One-Click Strategic Workflows**: Fast triggers for executive review and retention plays.

### 2. 💬 Multi-Agent Business Decision Chat
- **Specialist Agent Switcher**: Segmented control switching between:
  - 🧠 **Executive Orchestrator** (Cross-department synthesis & routing)
  - 📊 **Sales Analyst Agent** (Revenue, deal pipeline & quota attainment)
  - 📢 **Growth & Marketing Agent** (Attribution, CAC vs LTV & ad copy)
  - 👥 **Customer Retention Agent** (Health scoring & churn prediction)
  - 🎧 **Support Triage Agent** (SLA monitoring & empathetic ticket drafting)
  - 🔎 **Market Research Agent** (Competitor scraping & SWOT radar)
- **Transparent Reasoning Inspector**: Expandable drawer showing the agent's chain-of-thought, state transitions, tool invocations (`sqlite_sales_db.query`, `churn_model_service.predict`), execution latency, and confidence scores.
- **Quick-Prompt Starter Chips**: Instant pre-populated queries for common executive decisions.

### 3. 📊 Sales Analytics
- **Pipeline Progression Funnel**: Deal count and value from Lead to Closed Won.
- **Revenue by Customer Tier**: Stacked breakdown of Enterprise, Mid-Market, and Starter contributions.
- **Quota Attainment Leaderboard**: Account executive progress bars, closed ARR, win rates, and deal sizes.
- **Interactive Win-Rate Scenario Simulator**: Dynamic slider allowing leaders to model projected Q4 revenue under varying win rates and deal velocity assumptions.

### 4. 📢 Marketing & Growth Engine
- **Multi-Touch Channel Attribution**: Granular ROAS, CAC, spend, and customer acquisition metrics.
- **Unit Economics Health**: Quarterly CAC compression vs. Customer LTV expansion.
- **Autonomous AI Copy Generator**: Select target channels (LinkedIn, Google Search, Email) and buyer personas to generate high-converting ad copy with predicted CTR.

### 5. 👥 Customer Success & Churn Intelligence
- **Account Health vs. MRR Quadrant Matrix**: Visual scatter chart highlighting high-value accounts in the danger zone.
- **Filterable Account Directory**: Real-time health scores, NPS, days inactive, and assigned owners.
- **Autonomous AI Churn Save Playbook**: Instant root-cause diagnosis and recommended 3-step retention action for at-risk accounts.

### 6. 🎧 Customer Support & SLA Operations
- **SLA Countdown Queue**: Tickets prioritized by priority, customer tier, and NLP sentiment scores.
- **AI Copilot Response Drafter**: Pre-synthesized empathetic drafts ready for one-click dispatch or human review.

### 7. 🔎 Business Research & Competitor Radar
- **Competitor Landscape Matrix**: Feature comparison, seat pricing, and AI threat ratings.
- **Enterprise Market Share Donut Chart**: Visual competitive distribution.
- **AI-Synthesized SWOT Matrix**: Dynamic 4-quadrant strategic assessment.
- **Industry Trend Radar**: Real-time macro movements in AI, multi-agent frameworks, and data governance.

### 8. 📄 Reports Repository & Audit Trail
- **Autonomous Executive Report Generator**: Compile EBR briefings with downloadable CSV data packages.
- **Document Archive**: Historical reports, date stamps, and authoring agent metadata.
- **Verifiable Decision Audit Trail**: Immutable log of high-impact AI inferences, confidence ratings, and business scopes.

---

## 🎨 Enterprise Design System

- **Sidebar**: Dark navy (`#0B1329` / `#0F172A`) with subtle border lines (`#1E315E`) and pulsing agent swarm status dot.
- **Main Canvas**: Off-white (`#F8FAFC`) with pure white (`#FFFFFF`) card containers.
- **Accent Palette**: Royal Blue (`#2563EB`) as the primary brand color, supported by Emerald Green (`#10B981`), Amber (`#F59E0B`), and Purple (`#8B5CF6`).
- **Cards & Typography**: `Plus Jakarta Sans`, 12px rounded corners, subtle shadows (`0 1px 3px rgba(0,0,0,0.05)`), and clean pill badges.

---

## 📂 Project Architecture

```
c:\antigravity works\
├── app.py                      # Main entrypoint, page routing & global CSS injection
├── requirements.txt            # Dependency specification
├── README.md                   # System documentation
├── .streamlit/
│   └── config.toml             # Theme configuration (light base, colors, server options)
├── assets/
│   └── styles.css              # Deep CSS overrides for enterprise SaaS styling
├── core/
│   ├── __init__.py
│   ├── config.py               # Constants, agent registry, navigation items, color palette
│   ├── state.py                # Streamlit session state initialization & helpers
│   └── agent_interface.py     # LangGraph protocol, data contracts (AgentRequest, AgentResponse)
├── data/
│   ├── __init__.py
│   └── mock_data.py            # Cohesive B2B SaaS datasets (Sales, Marketing, Churn, Support, Intel)
├── components/
│   ├── __init__.py
│   ├── sidebar.py              # Dark navy sidebar (Logo, Swarm status, Navigation, Filters)
│   ├── kpi_card.py             # Reusable SaaS metric cards with delta pill badges
│   ├── agent_inspector.py      # LangGraph chain-of-thought & tool execution drawer
│   └── charts.py               # Reusable Plotly enterprise themes
└── views/
    ├── __init__.py
    ├── dashboard.py            # 🏠 Dashboard
    ├── ai_chat.py              # 💬 AI Chat
    ├── sales_analytics.py      # 📊 Sales Analytics
    ├── marketing.py            # 📢 Marketing
    ├── customers.py            # 👥 Customers
    ├── customer_support.py     # 🎧 Customer Support
    ├── business_research.py    # 🔎 Business Research
    └── reports_repo.py         # 📄 Repo / Reports
```

---

## 🔌 Connecting to LangGraph, SQLite, RAG, and APIs

The application is architected so that backend connections require zero changes to the UI layer:

1. **LangGraph Multi-Agent Workflows**:
   In `core/agent_interface.py`, implement `BaseAgentOrchestrator` by replacing `MockLangGraphOrchestrator` with your compiled `StateGraph.compile()` object. The `AgentRequest` and `AgentResponse` dataclasses map 1:1 to LangGraph state dictionaries.

2. **SQLite Database**:
   Replace static calls in `data/mock_data.py` with `sqlite3` or SQLAlchemy connections (e.g. `sqlite:///business_assistant.db`). The tables map directly to the DataFrame schemas already defined in `mock_data.py`.

3. **Enterprise RAG & Vector Stores**:
   In `views/ai_chat.py`, the agent tool executor hooks into `tool_traces`. Plug in ChromaDB, FAISS, or Pinecone to populate document context chunks.

4. **External APIs**:
   Connect Salesforce/HubSpot in `views/sales_analytics.py`, Google Ads / LinkedIn Marketing API in `views/marketing.py`, and Zendesk / Intercom in `views/customer_support.py`.

---

## 🛠️ How to Run Locally

1. Activate your virtual environment:
   ```bash
   .venv\Scripts\activate
   ```
2. Start the Streamlit application:
   ```bash
   streamlit run app.py
   ```
3. Open your browser at `http://localhost:8501`.
