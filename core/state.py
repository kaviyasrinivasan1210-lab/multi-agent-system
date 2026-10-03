"""
Session state initialization and helpers for AI Business Assistant.
"""

from typing import Dict, Any, List
import streamlit as st
from datetime import datetime


def init_session_state() -> None:
    """Initialize all session state keys if not already present."""
    if "active_view" not in st.session_state:
        st.session_state["active_view"] = "dashboard"

    if "selected_agent" not in st.session_state:
        st.session_state["selected_agent"] = "orchestrator"

    if "date_range_selection" not in st.session_state:
        st.session_state["date_range_selection"] = "Last 30 Days"

    if "business_unit" not in st.session_state:
        st.session_state["business_unit"] = "All Business Units"

    if "chat_messages" not in st.session_state:
        st.session_state["chat_messages"] = [
            {
                "role": "assistant",
                "agent_id": "orchestrator",
                "content": (
                    "Hello! I am your **Executive Orchestrator Agent**. "
                    "I monitor your revenue pipeline, marketing campaigns, customer health, "
                    "support triage, and market research. How can I assist your business strategy today?"
                ),
                "timestamp": datetime.now().strftime("%I:%M %p"),
                "thoughts": [
                    {"step": "State Initialization", "detail": "LangGraph multi-agent swarm state loaded successfully."},
                    {"step": "Context Hook", "detail": "Queried enterprise memory store for latest business KPIs."},
                ],
                "tools_used": ["memory_retriever", "swarm_health_check"],
            }
        ]

    if "saved_reports" not in st.session_state:
        st.session_state["saved_reports"] = []

    if "draft_responses" not in st.session_state:
        st.session_state["draft_responses"] = {}


def add_chat_message(
    role: str,
    content: str,
    agent_id: str = "orchestrator",
    thoughts: List[Dict[str, str]] = None,
    tools_used: List[str] = None,
) -> None:
    """Add a message to the persistent chat history."""
    if "chat_messages" not in st.session_state:
        st.session_state["chat_messages"] = []

    st.session_state["chat_messages"].append(
        {
            "role": role,
            "agent_id": agent_id,
            "content": content,
            "timestamp": datetime.now().strftime("%I:%M %p"),
            "thoughts": thoughts or [],
            "tools_used": tools_used or [],
        }
    )


def clear_chat_history() -> None:
    """Clear chat messages and restore welcome message."""
    st.session_state["chat_messages"] = []
    init_session_state()
