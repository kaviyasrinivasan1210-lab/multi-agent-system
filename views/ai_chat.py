"""
AI Chat View — Multi-Agent Conversational Decision Interface.
Provides agent switching, prompt suggestions, conversation history,
and deep thought-process & tool inspection styled in Dark Neon Cyber.
"""

import streamlit as st
from core.config import AGENT_REGISTRY
from core.state import add_chat_message, clear_chat_history
from core.agent_interface import default_orchestrator, AgentRequest
from components.agent_inspector import render_agent_inspector


def render_ai_chat_view() -> None:
    """Renders the AI Chat multi-agent interface with neon dark aesthetics."""
    st.markdown(
        """
        <div style="margin-bottom: 1.25rem;">
            <h2 style="font-size: 1.4rem; font-weight: 800; color: #F8FAFC; margin: 0 0 4px 0; text-shadow: 0 0 12px rgba(0, 240, 255, 0.4);">
                💬 Multi-Agent Business Decision Chat
            </h2>
            <p style="font-size: 0.85rem; color: #94A3B8; margin: 0;">
                Consult dedicated specialist agents or let the Executive Orchestrator automatically route and synthesize.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 1. Agent Selector Bar
    col_agents, col_actions = st.columns([5, 1])

    with col_agents:
        agent_options = list(AGENT_REGISTRY.keys())
        agent_labels = {k: f"{v['icon']} {v['name']}" for k, v in AGENT_REGISTRY.items()}

        current_agent = st.session_state.get("selected_agent", "orchestrator")
        selected_agent = st.segmented_control(
            "Select Specialist Agent",
            options=agent_options,
            format_func=lambda x: agent_labels[x],
            default=current_agent,
            key="chat_agent_segmented_control",
        )
        if selected_agent:
            st.session_state["selected_agent"] = selected_agent
        else:
            selected_agent = "orchestrator"

    with col_actions:
        st.markdown("<div style='margin-top: 24px;'></div>", unsafe_allow_html=True)
        if st.button("🗑️ Clear", use_container_width=True, help="Clear conversation"):
            clear_chat_history()
            st.rerun()

    # Show active agent info chip
    agent_info = AGENT_REGISTRY.get(selected_agent, AGENT_REGISTRY["orchestrator"])
    agent_color = agent_info.get("color", "#00F0FF")
    st.markdown(
        f"""
        <div style="background: rgba(13, 21, 39, 0.85); border: 1px solid {agent_color}55; border-radius: 8px; padding: 10px 16px; margin: 10px 0 16px 0; display: flex; align-items: center; justify-content: space-between; box-shadow: 0 0 15px {agent_color}18;">
            <div style="display: flex; align-items: center; gap: 10px;">
                <span style="font-size: 1.2rem;">{agent_info['icon']}</span>
                <strong style="font-size: 0.86rem; color: #F8FAFC;">{agent_info['name']}</strong>
                <span style="font-size: 0.78rem; color: #94A3B8;">— {agent_info['role']}</span>
            </div>
            <span class="badge-pill badge-purple" style="font-size: 0.72rem; border-color: {agent_color}; color: {agent_color};">
                ● State: Active & Grounded
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 2. Quick Prompt Chips
    st.markdown("<div style='font-size: 0.75rem; font-weight: 700; color: #00F0FF; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.06em;'>⚡ Suggested Executive Queries:</div>", unsafe_allow_html=True)
    q_col1, q_col2, q_col3 = st.columns(3)

    query_to_send = None
    with q_col1:
        if st.button("📊 Breakdown Q3 pipeline & sales quotas", key="chip_1", use_container_width=True):
            query_to_send = "Breakdown our Q3 sales pipeline by deal stage, highlight stalled deals, and evaluate sales rep quota attainment."
            st.session_state["selected_agent"] = "sales"

    with q_col2:
        if st.button("👥 Identify top accounts at churn risk", key="chip_2", use_container_width=True):
            query_to_send = "Which enterprise accounts have high churn probability and what save play does the customer agent recommend?"
            st.session_state["selected_agent"] = "customers"

    with q_col3:
        if st.button("📢 Compare marketing channel ROAS & CAC", key="chip_3", use_container_width=True):
            query_to_send = "Compare our marketing acquisition channels by ROAS and generate high-converting ad copy for LinkedIn."
            st.session_state["selected_agent"] = "marketing"

    # 3. Chat Messages History Display
    st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True)

    chat_container = st.container()
    with chat_container:
        for msg in st.session_state.get("chat_messages", []):
            role = msg["role"]
            if role == "user":
                with st.chat_message("user", avatar="👤"):
                    st.markdown(f"**You** <span style='font-size:0.7rem; color:#94A3B8;'>({msg.get('timestamp', '')})</span>", unsafe_allow_html=True)
                    st.markdown(msg["content"])
            else:
                agent_id = msg.get("agent_id", "orchestrator")
                info = AGENT_REGISTRY.get(agent_id, AGENT_REGISTRY["orchestrator"])
                agent_neon = info.get("color", "#00F0FF")
                with st.chat_message("assistant", avatar=info["icon"]):
                    st.markdown(
                        f"""
                        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 6px;">
                            <span style="font-weight: 700; color: {agent_neon}; font-size: 0.9rem; text-shadow: 0 0 10px {agent_neon}55;">
                                {info['name']}
                            </span>
                            <span style="font-size: 0.7rem; color: #94A3B8;">
                                {msg.get('timestamp', '')}
                            </span>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
                    st.markdown(msg["content"])

                    # Render Thought and Tool Inspection Drawer
                    render_agent_inspector(
                        thoughts=msg.get("thoughts", []),
                        tools_used=msg.get("tools_used", []),
                        confidence=0.96,
                        agent_name=info["name"],
                    )

    # 4. Handle Incoming Query (either from quick prompt chips or chat_input)
    user_prompt = st.chat_input("Ask a business question or instruct an agent...")
    active_prompt = query_to_send or user_prompt

    if active_prompt:
        # Add User Message
        add_chat_message("user", active_prompt)

        # Invoke Mock LangGraph Orchestrator
        target_agent = st.session_state.get("selected_agent", "orchestrator")
        with st.spinner("Multi-Agent Swarm reasoning in progress..."):
            request_payload = AgentRequest(
                query=active_prompt,
                target_agent_id=target_agent,
                context_filters={
                    "period": st.session_state.get("date_range_selection", "Last 30 Days"),
                    "business_unit": st.session_state.get("business_unit", "All"),
                },
            )
            response = default_orchestrator.invoke_workflow(request_payload)

            # Record Assistant Message
            add_chat_message(
                role="assistant",
                content=response.answer,
                agent_id=response.agent_id,
                thoughts=response.thoughts,
                tools_used=response.tool_traces,
            )

        st.rerun()
