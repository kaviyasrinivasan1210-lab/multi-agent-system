"""
Customers View — Health Scoring, RFM Segmentation, Churn Risk & AI Save Playbook.
Styled with high-contrast Dark Neon Cyber aesthetic.
"""

import streamlit as st
import pandas as pd
from data.mock_data import get_customer_accounts_dataset
from components.kpi_card import render_kpi_card
from components.charts import create_customer_health_scatter


def render_customers_view() -> None:
    """Renders the Customers & Churn Risk view."""
    st.markdown(
        """
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.25rem;">
            <div>
                <h2 style="font-size: 1.4rem; font-weight: 800; color: #F8FAFC; margin: 0 0 4px 0; text-shadow: 0 0 12px rgba(0, 240, 255, 0.4);">
                    👥 Customer Success & Churn Intelligence
                </h2>
                <p style="font-size: 0.85rem; color: #94A3B8; margin: 0;">
                    Account health monitoring, early churn prediction, and autonomous retention playbooks.
                </p>
            </div>
            <div>
                <span class="badge-pill badge-success" style="font-size: 0.75rem;">
                    ● Agent: Retention Agent Active
                </span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 1. Customer Health KPIs
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        render_kpi_card("Portfolio Health Score", "86.4 / 100", "+1.8 pts", True, "Healthy benchmark", "🛡️", "#00FF9D")
    with c2:
        render_kpi_card("Net Retention Rate (NRR)", "114.2%", "+2.1%", True, "Expansion revenue positive", "📈", "#00F0FF")
    with c3:
        render_kpi_card("Accounts at Risk", "4 Accounts", "-2 accounts", True, "$38,400 MRR exposed", "⚠️", "#FF2A85")
    with c4:
        render_kpi_card("Net Promoter Score (NPS)", "+64", "+4 pts", True, "Excellent satisfaction", "💬", "#B026FF")

    st.markdown("<div style='margin-top: 1.5rem;'></div>", unsafe_allow_html=True)

    # 2. Risk Matrix Quadrant Chart
    cust_df = get_customer_accounts_dataset()

    st.markdown(
        """
        <div class="saas-card">
            <div class="saas-card-header">
                <div>
                    <h3 class="saas-card-title">🔍 Enterprise Account Risk vs MRR Matrix</h3>
                    <p class="saas-card-subtitle">Bubble size represents MRR. Red quadrant indicates high-value accounts in danger.</p>
                </div>
            </div>
        """,
        unsafe_allow_html=True,
    )
    fig_scatter = create_customer_health_scatter(cust_df)
    st.plotly_chart(fig_scatter, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # 3. Account Roster Table with Health Badges
    st.markdown(
        """
        <div class="saas-card">
            <div class="saas-card-header">
                <div>
                    <h3 class="saas-card-title">📋 Enterprise Account Health & Churn Roster</h3>
                    <p class="saas-card-subtitle">Continuous RFM telemetry, product usage health scores, and assigned CSM.</p>
                </div>
            </div>
        """,
        unsafe_allow_html=True,
    )

    st.dataframe(
        cust_df,
        column_config={
            "Account": st.column_config.TextColumn("Account Name", width="medium"),
            "Tier": st.column_config.TextColumn("Tier"),
            "MRR ($)": st.column_config.NumberColumn("Monthly MRR", format="$%d"),
            "Health": st.column_config.ProgressColumn(
                "Health Score",
                format="%d / 100",
                min_value=0,
                max_value=100,
            ),
            "Risk": st.column_config.TextColumn("Churn Risk"),
            "Days Inactive": st.column_config.NumberColumn("Days Inactive", format="%d d"),
            "Owner": st.column_config.TextColumn("CSM Owner"),
            "Renewal Date": st.column_config.TextColumn("Contract Renewal"),
        },
        use_container_width=True,
        hide_index=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

    # 4. AI Churn Save Playbook Generator
    st.markdown(
        """
        <div class="saas-card">
            <div class="saas-card-header">
                <div>
                    <h3 class="saas-card-title">🛡️ AI Churn Save Playbook Generator</h3>
                    <p class="saas-card-subtitle">Select an at-risk client to generate an instant root-cause diagnosis and proactive retention plan.</p>
                </div>
                <span class="badge-pill badge-danger">Action Required</span>
            </div>
        """,
        unsafe_allow_html=True,
    )

    at_risk_accounts = cust_df[cust_df["Risk"].isin(["High", "Medium"])]["Account"].tolist()
    selected_client = st.selectbox("Select Account for AI Diagnosis", at_risk_accounts)

    client_row = cust_df[cust_df["Account"] == selected_client].iloc[0]

    p_col1, p_col2 = st.columns([1, 2])

    with p_col1:
        st.markdown(
            f"""
            <div style="background: rgba(13, 21, 39, 0.85); border: 1px solid rgba(0, 240, 255, 0.22); border-radius: 8px; padding: 16px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
                <div style="font-size: 0.95rem; font-weight: 700; color: #F8FAFC; margin-bottom: 8px;">
                    {client_row['Account']}
                </div>
                <div style="font-size: 0.78rem; color: #94A3B8; margin-bottom: 4px;">Tier: <strong style="color:#F8FAFC;">{client_row['Tier']}</strong></div>
                <div style="font-size: 0.78rem; color: #94A3B8; margin-bottom: 4px;">Monthly Revenue: <strong style="color:#00F0FF;">${client_row['MRR ($)']:,}</strong></div>
                <div style="font-size: 0.78rem; color: #94A3B8; margin-bottom: 4px;">Health Score: <strong style="color: #FF2A85;">{client_row['Health']}/100</strong></div>
                <div style="font-size: 0.78rem; color: #94A3B8; margin-bottom: 8px;">Days Inactive: <strong style="color:#F8FAFC;">{client_row['Days Inactive']} days</strong></div>
                <div style="font-size: 0.78rem; color: #94A3B8;">Account Owner: <strong style="color:#00FF9D;">{client_row['Owner']}</strong></div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with p_col2:
        st.markdown(
            f"""
            <div style="background: rgba(13, 21, 39, 0.85); border-left: 3px solid #FF2A85; border-radius: 0 8px 8px 0; padding: 16px; border-top: 1px solid rgba(255,255,255,0.05); border-right: 1px solid rgba(255,255,255,0.05); border-bottom: 1px solid rgba(255,255,255,0.05);">
                <strong style="font-size: 0.86rem; color: #FF2A85; text-shadow: 0 0 8px rgba(255,42,133,0.4);">⚡ AI Root Cause Diagnosis:</strong>
                <p style="font-size: 0.8rem; color: #CBD5E1; margin: 4px 0 10px 0; line-height: 1.45;">
                    Login activity dropped by 42% over the last 18 days following internal IT restructuring. Unresolved billing ticket #1042 compounded frustration.
                </p>
                <strong style="font-size: 0.86rem; color: #00F0FF; text-shadow: 0 0 8px rgba(0,240,255,0.4);">Recommended 3-Step Save Action:</strong>
                <ol style="font-size: 0.8rem; color: #CBD5E1; margin: 6px 0 0 18px; padding: 0; line-height: 1.5;">
                    <li>Issue immediate $1,200 billing credit memo for the duplicate seat charge.</li>
                    <li>CSM {client_row['Owner']} to host a 20-min executive alignment session with their new VP of Ops.</li>
                    <li>Unlock free 60-day access to Advanced LangGraph Multi-Agent Workflows.</li>
                </ol>
            </div>
            """,
            unsafe_allow_html=True,
        )

        b1, b2 = st.columns(2)
        with b1:
            if st.button("🚀 Trigger CSM Save Outreach", key="save_csm_btn", type="primary", use_container_width=True):
                st.success("Save workflow initiated. Notification dispatched to account owner.")
        with b2:
            if st.button("💬 Consult Retention Agent", key="ask_retention_btn", use_container_width=True):
                st.session_state["selected_agent"] = "customers"
                st.session_state["active_view"] = "ai_chat"
                st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)
