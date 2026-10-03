"""
Dashboard View — Executive Multi-Agent Intelligence Center.
Styled with high-contrast Dark Neon Cyber aesthetic.
"""

import streamlit as st
from data.mock_data import (
    get_executive_kpis,
    get_monthly_revenue_history,
    get_agent_swarm_events,
)
from components.kpi_card import render_kpi_card
from components.charts import create_revenue_trend_chart


def render_dashboard_view() -> None:
    """Renders the executive summary dashboard."""
    # 1. Executive Top Banner
    st.markdown(
        """
        <div class="executive-banner">
            <div>
                <h2>⚡ Executive Decision Center</h2>
                <p>
                    Autonomous Multi-Agent AI Swarm monitoring Sales, Marketing, Customer Retention, and Operations in real-time.
                </p>
            </div>
            <div style="text-align: right;">
                <span class="badge-pill badge-success" style="font-size: 0.8rem; padding: 6px 14px;">
                    ● Multi-Agent Swarm: Fully Synced
                </span>
                <div style="font-size: 0.75rem; color: #94A3B8; margin-top: 6px;">
                    Last state checkpoint: Just now
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 2. Key Executive Metric Cards
    kpis = get_executive_kpis()
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        render_kpi_card(
            label="Annual Recurring Revenue (ARR)",
            value=kpis["arr"]["value"],
            delta=kpis["arr"]["delta"],
            is_positive=kpis["arr"]["is_positive"],
            subtitle=kpis["arr"]["subtitle"],
            icon="💰",
            accent_color="#00F0FF",
        )

    with c2:
        render_kpi_card(
            label="Qualified Sales Pipeline",
            value=kpis["pipeline"]["value"],
            delta=kpis["pipeline"]["delta"],
            is_positive=kpis["pipeline"]["is_positive"],
            subtitle=kpis["pipeline"]["subtitle"],
            icon="🎯",
            accent_color="#B026FF",
        )

    with c3:
        render_kpi_card(
            label="Blended CAC (Acquisition Cost)",
            value=kpis["cac"]["value"],
            delta=kpis["cac"]["delta"],
            is_positive=kpis["cac"]["is_positive"],
            subtitle=kpis["cac"]["subtitle"],
            icon="📢",
            accent_color="#00FF9D",
        )

    with c4:
        render_kpi_card(
            label="Customer Satisfaction (CSAT)",
            value=kpis["csat"]["value"],
            delta=kpis["csat"]["delta"],
            is_positive=kpis["csat"]["is_positive"],
            subtitle=kpis["csat"]["subtitle"],
            icon="⭐",
            accent_color="#FFB800",
        )

    st.markdown("<div style='margin-top: 1.5rem;'></div>", unsafe_allow_html=True)

    # 3. Main Chart & Live Agent Event Feed
    col_chart, col_feed = st.columns([5, 3])

    with col_chart:
        st.markdown(
            """
            <div class="saas-card">
                <div class="saas-card-header">
                    <div>
                        <h3 class="saas-card-title">📈 Revenue Trajectory & AI Projections</h3>
                        <p class="saas-card-subtitle">Comparing closed revenue vs planned quota and LangGraph forecasted trajectory.</p>
                    </div>
                    <span class="badge-pill badge-cyan">YTD Track: +18.4%</span>
                </div>
            """,
            unsafe_allow_html=True,
        )
        rev_df = get_monthly_revenue_history()
        fig_rev = create_revenue_trend_chart(rev_df)
        st.plotly_chart(fig_rev, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col_feed:
        st.markdown(
            """
            <div class="saas-card">
                <div class="saas-card-header">
                    <div>
                        <h3 class="saas-card-title">🤖 Swarm Activity Pulse</h3>
                        <p class="saas-card-subtitle">Autonomous agent actions and signals in last 4 hours.</p>
                    </div>
                </div>
            """,
            unsafe_allow_html=True,
        )

        events = get_agent_swarm_events()
        for ev in events:
            border_color = (
                "#00FF9D" if ev["type"] == "success"
                else "#FFB800" if ev["type"] == "warning"
                else "#00F0FF"
            )
            st.markdown(
                f"""
                <div style="border-left: 3px solid {border_color}; padding: 8px 12px; margin-bottom: 10px; background: rgba(13, 21, 39, 0.75); border-radius: 0 8px 8px 0; border-top: 1px solid rgba(255,255,255,0.05); border-right: 1px solid rgba(255,255,255,0.05); border-bottom: 1px solid rgba(255,255,255,0.05);">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2px;">
                        <span style="font-size: 0.78rem; font-weight: 700; color: #F8FAFC;">{ev['icon']} {ev['agent']}</span>
                        <span style="font-size: 0.68rem; color: #94A3B8;">{ev['time']}</span>
                    </div>
                    <div style="font-size: 0.77rem; color: #CBD5E1; line-height: 1.35;">
                        {ev['event']}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown("</div>", unsafe_allow_html=True)

    # 4. Strategic Recommendations & One-Click Agent Workflows
    st.markdown(
        """
        <div class="saas-card">
            <div class="saas-card-header">
                <div>
                    <h3 class="saas-card-title">⚡ Recommended Multi-Agent Strategic Plays</h3>
                    <p class="saas-card-subtitle">High-impact actions identified by cross-agent analysis ready for one-click review.</p>
                </div>
            </div>
        """,
        unsafe_allow_html=True,
    )

    act_col1, act_col2, act_col3 = st.columns(3)

    with act_col1:
        st.markdown(
            """
            <div style="background: rgba(13, 21, 39, 0.85); border: 1px solid rgba(0, 240, 255, 0.2); border-radius: 10px; padding: 16px; height: 100%; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
                <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
                    <span style="font-size: 1.3rem;">👥</span>
                    <strong style="font-size: 0.9rem; color: #00FF9D; text-shadow: 0 0 8px rgba(0,255,157,0.4);">Save 4 At-Risk Accounts</strong>
                </div>
                <p style="font-size: 0.79rem; color: #94A3B8; margin-bottom: 14px; line-height: 1.4;">
                    Retention Agent found $38.4k MRR showing seat login decay. Trigger customized CSM save workflows.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("Inspect Churn Radar →", key="dash_btn_churn", use_container_width=True):
            st.session_state["active_view"] = "customers"
            st.rerun()

    with act_col2:
        st.markdown(
            """
            <div style="background: rgba(13, 21, 39, 0.85); border: 1px solid rgba(0, 240, 255, 0.2); border-radius: 10px; padding: 16px; height: 100%; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
                <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
                    <span style="font-size: 1.3rem;">📢</span>
                    <strong style="font-size: 0.9rem; color: #00F0FF; text-shadow: 0 0 8px rgba(0,240,255,0.4);">Capitalize on LinkedIn ROAS</strong>
                </div>
                <p style="font-size: 0.79rem; color: #94A3B8; margin-bottom: 14px; line-height: 1.4;">
                    Marketing Agent calculated 3.82x ROAS on LinkedIn. Reallocate $6k from underperforming display ads.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("Review Marketing Plan →", key="dash_btn_mkt", use_container_width=True):
            st.session_state["active_view"] = "marketing"
            st.rerun()

    with act_col3:
        st.markdown(
            """
            <div style="background: rgba(13, 21, 39, 0.85); border: 1px solid rgba(176, 38, 255, 0.3); border-radius: 10px; padding: 16px; height: 100%; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
                <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
                    <span style="font-size: 1.3rem;">💬</span>
                    <strong style="font-size: 0.9rem; color: #B026FF; text-shadow: 0 0 8px rgba(176,38,255,0.4);">Consult Orchestrator</strong>
                </div>
                <p style="font-size: 0.79rem; color: #94A3B8; margin-bottom: 14px; line-height: 1.4;">
                    Ask open-ended business questions with transparent multi-agent reasoning traces and tool calls.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("Open AI Chat →", key="dash_btn_chat", use_container_width=True, type="primary"):
            st.session_state["active_view"] = "ai_chat"
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)
