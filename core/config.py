"""
Configuration and constants for the AI Business Assistant.
"""

from typing import Dict, List, Any

APP_NAME = "AI Business Assistant"
APP_SUBTITLE = "Multi-Agent AI for Smarter Business Decisions"
APP_VERSION = "2.4.0 Enterprise"

# Navigation Items mapped to internal view IDs
NAVIGATION_ITEMS: List[Dict[str, str]] = [
    {"label": "🏠 Dashboard", "id": "dashboard"},
    {"label": "💬 AI Chat", "id": "ai_chat"},
    {"label": "📊 Sales Analytics", "id": "sales_analytics"},
    {"label": "📢 Marketing", "id": "marketing"},
    {"label": "👥 Customers", "id": "customers"},
    {"label": "🎧 Customer Support", "id": "customer_support"},
    {"label": "🔎 Business Research", "id": "business_research"},
    {"label": "📄 Repo", "id": "reports_repo"},
]

# Registered AI Agents in the Swarm (Ready for LangGraph)
AGENT_REGISTRY: Dict[str, Dict[str, Any]] = {
    "orchestrator": {
        "name": "Executive Orchestrator",
        "role": "Coordinator & Strategic Synthesis",
        "icon": "🧠",
        "status": "Online",
        "color": "#B026FF",
        "description": "Routes user queries to domain specialists and synthesizes executive action plans.",
    },
    "sales": {
        "name": "Sales Analyst Agent",
        "role": "Revenue, Quotas & Deal Pipeline",
        "icon": "📊",
        "status": "Online",
        "color": "#00F0FF",
        "description": "Analyzes deal velocity, sales rep attainment, and churn-adjusted pipeline forecasts.",
    },
    "marketing": {
        "name": "Growth & Marketing Agent",
        "role": "Attribution, CAC & Campaign Copy",
        "icon": "📢",
        "status": "Online",
        "color": "#38BDF8",
        "description": "Evaluates multi-touch channel ROAS, optimizes spend, and drafts targeted copy.",
    },
    "customers": {
        "name": "Customer Retention Agent",
        "role": "RFM Segmentation & Churn Risk",
        "icon": "👥",
        "status": "Online",
        "color": "#00FF9D",
        "description": "Detects early churn signals, health drop-offs, and recommends targeted save offers.",
    },
    "support": {
        "name": "Support Triage Agent",
        "role": "SLA Monitor & Ticket Resolution",
        "icon": "🎧",
        "status": "Online",
        "color": "#FFB800",
        "description": "Prioritizes customer tickets by sentiment and generates instant empathetic drafts.",
    },
    "research": {
        "name": "Market Research Agent",
        "role": "Competitor Intel & Trend Radar",
        "icon": "🔎",
        "status": "Online",
        "color": "#FF2A85",
        "description": "Scrapes market trends, pricing changes, and compiles SWOT matrices.",
    },
}

# Neon Dark Color Palette for Plotly Charts and UI Elements
COLOR_PALETTE = {
    "primary": "#00F0FF",
    "primary_light": "#38BDF8",
    "secondary": "#0A0F1D",
    "accent_cyan": "#00F0FF",
    "success": "#00FF9D",
    "warning": "#FFB800",
    "danger": "#FF2A85",
    "purple": "#B026FF",
    "grid": "rgba(255, 255, 255, 0.08)",
    "background": "#070B14",
    "card_bg": "#0D1527",
    "text": "#F8FAFC",
    "text_muted": "#94A3B8",
}
