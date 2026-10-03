"""
Enterprise Dark Neon Left Sidebar Component for AI Business Assistant.
Includes glowing cyber branding, active agent swarm indicator, navigation radio, filters, and system controls.
"""

import streamlit as st
from core.config import APP_NAME, APP_SUBTITLE, APP_VERSION, NAVIGATION_ITEMS, AGENT_REGISTRY


def render_sidebar() -> str:
    """
    Renders the persistent left sidebar with neon dark theme and returns the selected view id.
    """
    with st.sidebar:
        # 1. Branding Header
        st.markdown(
            f"""
            <div class="sidebar-brand-container">
                <div class="sidebar-logo-icon">🤖</div>
                <div class="sidebar-brand-text">
                    <span class="sidebar-brand-title">{APP_NAME}</span>
                    <span class="sidebar-brand-badge">Multi-Agent Intelligence</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # 2. Multi-Agent Swarm Live Status
        st.markdown(
            """
            <div class="sidebar-agent-swarm-card">
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 4px;">
                    <span style="font-size: 0.75rem; font-weight: 700; color: #F8FAFC; letter-spacing: 0.02em;">AGENT SWARM</span>
                    <span class="agent-status-indicator">
                        <span class="status-dot-pulse"></span>
                        <span>6 ACTIVE</span>
                    </span>
                </div>
                <div style="font-size: 0.72rem; color: #94A3B8; line-height: 1.3;">
                    LangGraph State Machine: <span style="color: #00F0FF; font-weight: 700; text-shadow: 0 0 8px rgba(0,240,255,0.6);">Online</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # 3. Main Navigation
        st.markdown(
            "<p style='font-size: 0.7rem; font-weight: 700; color: #94A3B8; letter-spacing: 0.08em; text-transform: uppercase; margin: 0 0 8px 4px;'>Navigation</p>",
            unsafe_allow_html=True,
        )

        nav_labels = [item["label"] for item in NAVIGATION_ITEMS]
        nav_id_map = {item["label"]: item["id"] for item in NAVIGATION_ITEMS}

        # Current active index
        current_id = st.session_state.get("active_view", "dashboard")
        default_index = 0
        for idx, item in enumerate(NAVIGATION_ITEMS):
            if item["id"] == current_id:
                default_index = idx
                break

        selected_label = st.radio(
            "Select Section",
            nav_labels,
            index=default_index,
            label_visibility="collapsed",
            key="main_nav_radio",
        )

        selected_view_id = nav_id_map[selected_label]
        st.session_state["active_view"] = selected_view_id

        # 4. Global Scope Filters
        st.markdown("<hr style='margin: 1.2rem 0; border-color: rgba(0, 240, 255, 0.18);'>", unsafe_allow_html=True)
        st.markdown(
            "<p style='font-size: 0.7rem; font-weight: 700; color: #94A3B8; letter-spacing: 0.08em; text-transform: uppercase; margin: 0 0 8px 4px;'>Global Scope Filters</p>",
            unsafe_allow_html=True,
        )

        st.session_state["date_range_selection"] = st.selectbox(
            "Reporting Period",
            ["Last 30 Days", "Current Quarter (Q3 2026)", "Year to Date (YTD)", "Last 12 Months"],
            index=0,
            key="sidebar_date_filter",
        )

        st.session_state["business_unit"] = st.selectbox(
            "Business Unit",
            ["All Business Units", "Enterprise SaaS", "Mid-Market", "Starter Tier", "International (EMEA/APAC)"],
            index=0,
            key="sidebar_bu_filter",
        )

        # 5. Agent Swarm Node Roster (Collapsible)
        with st.expander("🤖 Active Agent Roster", expanded=False):
            for agent_key, info in AGENT_REGISTRY.items():
                agent_neon_color = info.get("color", "#00F0FF")
                st.markdown(
                    f"""
                    <div style="display: flex; align-items: center; justify-content: space-between; padding: 6px 0; border-bottom: 1px solid rgba(0, 240, 255, 0.12);">
                        <div style="font-size: 0.78rem; color: #F8FAFC;">
                            <span>{info['icon']}</span> <strong>{info['name']}</strong>
                        </div>
                        <span style="font-size: 0.68rem; color: {agent_neon_color}; background: {agent_neon_color}18; border: 1px solid {agent_neon_color}44; padding: 1px 7px; border-radius: 4px; font-weight: 600;">Ready</span>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        # 6. System Footer
        st.markdown("<div style='margin-top: 2rem;'></div>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔄 Reset", use_container_width=True, help="Clear session chat & reset views"):
                from core.state import clear_chat_history
                clear_chat_history()
                st.rerun()
        with col2:
            st.markdown(
                f"""
                <div style="text-align: right; font-size: 0.68rem; color: #94A3B8; padding-top: 8px;">
                    v{APP_VERSION}
                </div>
                """,
                unsafe_allow_html=True,
            )

    return selected_view_id
