"""
Sales Analytics View — Pipeline Funnel, Revenue Tiers & Quota Attainment.
Styled with high-contrast Dark Neon Cyber aesthetic.
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from data.mock_data import (
    get_sales_pipeline_data,
    get_sales_rep_performance,
    get_sales_by_tier,
)
from components.kpi_card import render_kpi_card
from components.charts import create_pipeline_funnel_chart, apply_enterprise_theme


def render_sales_analytics_view() -> None:
    """Renders the Sales Analytics view."""
    st.markdown(
        """
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.25rem;">
            <div>
                <h2 style="font-size: 1.4rem; font-weight: 800; color: #F8FAFC; margin: 0 0 4px 0; text-shadow: 0 0 12px rgba(0, 240, 255, 0.4);">
                    📊 Sales Pipeline & Revenue Analytics
                </h2>
                <p style="font-size: 0.85rem; color: #94A3B8; margin: 0;">
                    Deal progression velocity, quota leaderboard, and dynamic win-rate scenario simulation.
                </p>
            </div>
            <div>
                <span class="badge-pill badge-cyan" style="font-size: 0.75rem;">
                    ● Agent: Sales Analyst Active
                </span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 1. Sales Top KPIs
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        render_kpi_card("Active Pipeline Value", "$2,840,000", "+12.1%", True, "48 open enterprise deals", "💼", "#00F0FF")
    with c2:
        render_kpi_card("Closed Won ARR (YTD)", "$1,248,000", "+18.4%", True, "108.4% of quota target", "🏆", "#00FF9D")
    with c3:
        render_kpi_card("Average Deal Size", "$24,800", "+6.2%", True, "Enterprise avg: $42,500", "🏷️", "#B026FF")
    with c4:
        render_kpi_card("Sales Cycle Length", "32 Days", "-4.5 days", True, "Mid-market closing faster", "⏱️", "#38BDF8")

    st.markdown("<div style='margin-top: 1.5rem;'></div>", unsafe_allow_html=True)

    # 2. Charts Row: Pipeline Funnel & Product Tier Distribution
    col_funnel, col_tier = st.columns([5, 4])

    with col_funnel:
        st.markdown(
            """
            <div class="saas-card">
                <div class="saas-card-header">
                    <div>
                        <h3 class="saas-card-title">🎯 Sales Pipeline Progression Funnel</h3>
                        <p class="saas-card-subtitle">Volume and conversion rates through qualification stages.</p>
                    </div>
                </div>
            """,
            unsafe_allow_html=True,
        )
        pipe_df = get_sales_pipeline_data()
        fig_funnel = create_pipeline_funnel_chart(pipe_df)
        st.plotly_chart(fig_funnel, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col_tier:
        st.markdown(
            """
            <div class="saas-card">
                <div class="saas-card-header">
                    <div>
                        <h3 class="saas-card-title">🏢 Revenue by Customer Tier</h3>
                        <p class="saas-card-subtitle">Monthly contribution by plan segment.</p>
                    </div>
                </div>
            """,
            unsafe_allow_html=True,
        )
        tier_df = get_sales_by_tier()
        fig_tier = go.Figure()
        fig_tier.add_trace(go.Bar(x=tier_df["Month"], y=tier_df["Enterprise Tier"], name="Enterprise", marker_color="#00F0FF"))
        fig_tier.add_trace(go.Bar(x=tier_df["Month"], y=tier_df["Mid-Market Tier"], name="Mid-Market", marker_color="#38BDF8"))
        fig_tier.add_trace(go.Bar(x=tier_df["Month"], y=tier_df["Starter / Pro"], name="Starter", marker_color="#818CF8"))
        fig_tier.update_layout(barmode="stack")
        fig_tier = apply_enterprise_theme(fig_tier, height=360, title="")
        st.plotly_chart(fig_tier, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # 3. Sales Rep Leaderboard Table
    st.markdown(
        """
        <div class="saas-card">
            <div class="saas-card-header">
                <div>
                    <h3 class="saas-card-title">🏅 Account Executive Quota Attainment</h3>
                    <p class="saas-card-subtitle">Real-time performance tracking against quarterly targets.</p>
                </div>
                <span class="badge-pill badge-success">Team Avg: 107.9%</span>
            </div>
        """,
        unsafe_allow_html=True,
    )

    reps_df = get_sales_rep_performance()

    st.dataframe(
        reps_df,
        column_config={
            "Sales Representative": st.column_config.TextColumn("Sales Executive", width="medium"),
            "Quota ($)": st.column_config.NumberColumn("Quota", format="$%d"),
            "Closed ARR ($)": st.column_config.NumberColumn("Closed Revenue", format="$%d"),
            "Attainment (%)": st.column_config.ProgressColumn(
                "Quota Attainment",
                format="%.1f%%",
                min_value=0,
                max_value=130,
            ),
            "Active Deals": st.column_config.NumberColumn("Active Pipeline", format="%d deals"),
            "Win Rate (%)": st.column_config.NumberColumn("Win Rate", format="%.1f%%"),
            "Avg Deal Size ($)": st.column_config.NumberColumn("Avg Deal", format="$%d"),
        },
        use_container_width=True,
        hide_index=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

    # 4. Interactive AI Pipeline Scenario Simulator
    st.markdown(
        """
        <div class="saas-card">
            <div class="saas-card-header">
                <div>
                    <h3 class="saas-card-title">🔮 Interactive AI Pipeline Win-Rate Simulator</h3>
                    <p class="saas-card-subtitle">Simulate projected Q4 revenue outcomes under different deal close velocity scenarios.</p>
                </div>
            </div>
        """,
        unsafe_allow_html=True,
    )

    sim_col1, sim_col2 = st.columns([1, 2])

    with sim_col1:
        sim_win_rate = st.slider("Simulated Proposal Win Rate (%)", min_value=15, max_value=60, value=35, step=5)
        sim_deal_velocity = st.select_slider("Deal Closing Velocity", options=["Conservative (45 days)", "Expected (32 days)", "Aggressive (24 days)"], value="Expected (32 days)")

        # Calculation
        pipeline_at_proposal = 480000 + 420000  # Proposal + Negotiation
        velocity_multiplier = 0.85 if "Conservative" in sim_deal_velocity else (1.0 if "Expected" in sim_deal_velocity else 1.2)
        projected_additional_arr = int(pipeline_at_proposal * (sim_win_rate / 100.0) * velocity_multiplier)
        projected_total_arr = 1248000 + projected_additional_arr

        st.metric(
            label="Projected Q4 Incremental ARR",
            value=f"${projected_additional_arr:,.0f}",
            delta=f"+{(projected_additional_arr/1248000)*100:.1f}% to ARR",
        )
        st.metric(
            label="Year-End Projected ARR",
            value=f"${projected_total_arr:,.0f}",
        )

    with sim_col2:
        # Comparison Bar Chart
        scenarios = ["Current ARR", "Simulated Q4 Addition", "Projected Total ARR"]
        values = [1248000, projected_additional_arr, projected_total_arr]
        colors = ["#00F0FF", "#00FF9D", "#B026FF"]

        sim_fig = go.Figure(
            go.Bar(
                x=scenarios,
                y=values,
                marker=dict(color=colors, line=dict(color="rgba(0, 240, 255, 0.4)", width=1)),
                text=[f"${v:,.0f}" for v in values],
                textposition="auto",
                textfont=dict(color="#FFFFFF", size=11),
            )
        )
        sim_fig = apply_enterprise_theme(sim_fig, height=280, title="Projected Revenue Trajectory under Scenario")
        st.plotly_chart(sim_fig, use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)
