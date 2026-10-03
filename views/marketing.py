"""
Marketing View — Channel Attribution, ROAS, CAC vs LTV, and AI Copy Generator.
Styled with high-contrast Dark Neon Cyber aesthetic.
"""

import streamlit as st
from data.mock_data import (
    get_marketing_channels_data,
    get_cac_ltv_history,
    get_ai_ad_copy_templates,
)
from components.kpi_card import render_kpi_card
from components.charts import create_marketing_roas_chart, create_cac_ltv_chart


def render_marketing_view() -> None:
    """Renders the Marketing view."""
    st.markdown(
        """
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.25rem;">
            <div>
                <h2 style="font-size: 1.4rem; font-weight: 800; color: #F8FAFC; margin: 0 0 4px 0; text-shadow: 0 0 12px rgba(0, 240, 255, 0.4);">
                    📢 Marketing Attribution & Growth Engine
                </h2>
                <p style="font-size: 0.85rem; color: #94A3B8; margin: 0;">
                    Multi-touch channel attribution, CAC vs LTV efficiency, and autonomous campaign copy generation.
                </p>
            </div>
            <div>
                <span class="badge-pill badge-cyan" style="font-size: 0.75rem;">
                    ● Agent: Growth Marketer Active
                </span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 1. Marketing Top KPIs
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        render_kpi_card("Blended CAC", "$482", "-8.2%", True, "Target: < $500", "🎯", "#00F0FF")
    with c2:
        render_kpi_card("Blended ROAS", "4.82x", "+0.6x", True, "Return on Ad Spend", "📈", "#00FF9D")
    with c3:
        render_kpi_card("Qualified MQLs", "1,695", "+14.3%", True, "Last 30 days total", "👥", "#B026FF")
    with c4:
        render_kpi_card("LTV to CAC Ratio", "4.99x", "+0.3x", True, "Benchmark: > 3.0x", "⚖️", "#38BDF8")

    st.markdown("<div style='margin-top: 1.5rem;'></div>", unsafe_allow_html=True)

    # 2. Charts Row
    col_roas, col_ltv = st.columns(2)

    with col_roas:
        st.markdown(
            """
            <div class="saas-card">
                <div class="saas-card-header">
                    <div>
                        <h3 class="saas-card-title">📊 Channel ROAS Ranking</h3>
                        <p class="saas-card-subtitle">Efficiency across organic and paid channels.</p>
                    </div>
                </div>
            """,
            unsafe_allow_html=True,
        )
        mkt_df = get_marketing_channels_data()
        fig_roas = create_marketing_roas_chart(mkt_df)
        st.plotly_chart(fig_roas, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col_ltv:
        st.markdown(
            """
            <div class="saas-card">
                <div class="saas-card-header">
                    <div>
                        <h3 class="saas-card-title">📉 CAC Compression vs LTV Expansion</h3>
                        <p class="saas-card-subtitle">Long-term unit economic health trajectory.</p>
                    </div>
                </div>
            """,
            unsafe_allow_html=True,
        )
        cac_df = get_cac_ltv_history()
        fig_cac = create_cac_ltv_chart(cac_df)
        st.plotly_chart(fig_cac, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # 3. Channel Attribution Performance Table
    st.markdown(
        """
        <div class="saas-card">
            <div class="saas-card-header">
                <div>
                    <h3 class="saas-card-title">📑 Acquisition Channel Attribution Matrix</h3>
                    <p class="saas-card-subtitle">Granular breakdown of spend, leads, CAC, and attributed pipeline revenue.</p>
                </div>
            </div>
        """,
        unsafe_allow_html=True,
    )

    st.dataframe(
        mkt_df,
        column_config={
            "Channel": st.column_config.TextColumn("Channel", width="medium"),
            "Spend ($)": st.column_config.NumberColumn("Spend", format="$%d"),
            "Leads Generated": st.column_config.NumberColumn("Leads", format="%d"),
            "Customers Won": st.column_config.NumberColumn("Closed Customers", format="%d"),
            "CAC ($)": st.column_config.NumberColumn("CAC", format="$%d"),
            "Revenue Attributed ($)": st.column_config.NumberColumn("Attributed Revenue", format="$%d"),
            "ROAS (x)": st.column_config.NumberColumn("ROAS", format="%.2fx"),
        },
        use_container_width=True,
        hide_index=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

    # 4. AI Campaign Copy & Strategy Generator
    st.markdown(
        """
        <div class="saas-card">
            <div class="saas-card-header">
                <div>
                    <h3 class="saas-card-title">✍️ AI Campaign Copy & Strategy Generator</h3>
                    <p class="saas-card-subtitle">Growth Agent creates persona-tailored ad variations grounded in historical conversion data.</p>
                </div>
                <span class="badge-pill badge-purple">LangGraph Copy Node</span>
            </div>
        """,
        unsafe_allow_html=True,
    )

    p1, p2, p3 = st.columns(3)
    with p1:
        selected_platform = st.selectbox(
            "Target Marketing Channel",
            ["LinkedIn Sponsored InMail", "Google Search Headline", "Email Nurture (At-Risk Save)"],
        )
    with p2:
        selected_persona = st.selectbox(
            "Target Buyer Persona",
            ["Chief Revenue Officer / VP Sales", "Head of Customer Success", "Director of Financial Ops"],
        )
    with p3:
        selected_tone = st.selectbox(
            "Messaging Angle",
            ["Data-driven Executive", "High Urgency / FOMO", "Empathetic Advisory"],
        )

    templates = get_ai_ad_copy_templates()
    matched_template = templates[0]
    for t in templates:
        if t["platform"] == selected_platform:
            matched_template = t
            break

    st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)

    col_preview, col_action = st.columns([4, 1])
    with col_preview:
        st.markdown(
            f"""
            <div style="background: rgba(13, 21, 39, 0.85); border: 1px solid rgba(0, 240, 255, 0.25); border-radius: 10px; padding: 18px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <span style="font-size: 0.75rem; font-weight: 700; color: #00F0FF; text-transform: uppercase; letter-spacing: 0.05em;">{matched_template['platform']}</span>
                    <span class="badge-pill badge-success">{matched_template['predicted_ctr']}</span>
                </div>
                <div style="font-size: 0.98rem; font-weight: 700; color: #F8FAFC; margin-bottom: 8px;">
                    "{matched_template['headline']}"
                </div>
                <div style="font-size: 0.85rem; color: #CBD5E1; line-height: 1.55; margin-bottom: 14px;">
                    {matched_template['body']}
                </div>
                <div style="display: inline-block; background: linear-gradient(135deg, #00F0FF, #38BDF8); color: #030712; font-size: 0.78rem; font-weight: 700; padding: 6px 14px; border-radius: 6px; box-shadow: 0 0 12px rgba(0, 240, 255, 0.4);">
                    {matched_template['cta']}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_action:
        st.markdown("<div style='margin-top: 25px;'></div>", unsafe_allow_html=True)
        if st.button("📋 Copy Copy", use_container_width=True):
            st.toast("Ad copy copied to clipboard!")
        if st.button("🔄 Generate Variant", type="primary", use_container_width=True):
            st.toast("Generating alternative messaging variant via Growth Marketer agent...")

    st.markdown("</div>", unsafe_allow_html=True)
