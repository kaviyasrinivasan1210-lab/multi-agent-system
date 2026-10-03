"""
Business Research View — Competitor Intelligence, Market Share, and AI SWOT Generator.
Styled with high-contrast Dark Neon Cyber aesthetic.
"""

import streamlit as st
from data.mock_data import (
    get_competitor_matrix,
    get_market_trends_data,
)
from components.charts import create_competitor_share_donut


def render_business_research_view() -> None:
    """Renders the Business Research and Competitor Intel view."""
    st.markdown(
        """
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.25rem;">
            <div>
                <h2 style="font-size: 1.4rem; font-weight: 800; color: #F8FAFC; margin: 0 0 4px 0; text-shadow: 0 0 12px rgba(0, 240, 255, 0.4);">
                    🔎 Market & Competitor Intelligence
                </h2>
                <p style="font-size: 0.85rem; color: #94A3B8; margin: 0;">
                    Automated competitor tracking, pricing shift monitors, and AI-synthesized SWOT assessments.
                </p>
            </div>
            <div>
                <span class="badge-pill badge-purple" style="font-size: 0.75rem;">
                    ● Agent: Market Research Active
                </span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 1. Competitor Grid & Market Share Row
    comp_col1, comp_col2 = st.columns([5, 4])

    comp_df = get_competitor_matrix()

    with comp_col1:
        st.markdown(
            """
            <div class="saas-card">
                <div class="saas-card-header">
                    <div>
                        <h3 class="saas-card-title">🏢 Competitor Landscape & Pricing Matrix</h3>
                        <p class="saas-card-subtitle">Real-time intelligence scraped from public tiers and win/loss transcripts.</p>
                    </div>
                </div>
            """,
            unsafe_allow_html=True,
        )

        st.dataframe(
            comp_df,
            column_config={
                "Competitor": st.column_config.TextColumn("Competitor", width="medium"),
                "Market Share (%)": st.column_config.NumberColumn("Share", format="%.1f%%"),
                "Starting Price ($/mo)": st.column_config.NumberColumn("Seat Price", format="$%d/mo"),
                "Key Strength": st.column_config.TextColumn("Core Strength"),
                "Core Weakness": st.column_config.TextColumn("Vulnerability"),
                "Recent Move": st.column_config.TextColumn("Recent Strategic Action"),
                "AI Threat Level": st.column_config.TextColumn("Threat Rating"),
            },
            use_container_width=True,
            hide_index=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with comp_col2:
        st.markdown(
            """
            <div class="saas-card">
                <div class="saas-card-header">
                    <div>
                        <h3 class="saas-card-title">🥧 Market Share Distribution</h3>
                        <p class="saas-card-subtitle">Estimated market capture across enterprise segments.</p>
                    </div>
                </div>
            """,
            unsafe_allow_html=True,
        )
        fig_donut = create_competitor_share_donut(comp_df)
        st.plotly_chart(fig_donut, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # 2. Automated AI SWOT Matrix Generator
    st.markdown(
        """
        <div class="saas-card">
            <div class="saas-card-header">
                <div>
                    <h3 class="saas-card-title">⚔️ AI Competitor SWOT Matrix Dossier</h3>
                    <p class="saas-card-subtitle">Select an enterprise adversary to generate a dynamic strengths, weaknesses, and counter-positioning strategy.</p>
                </div>
                <span class="badge-pill badge-blue">LangGraph SWOT Synthesizer</span>
            </div>
        """,
        unsafe_allow_html=True,
    )

    competitor_list = comp_df["Competitor"].tolist()
    selected_comp = st.selectbox("Select Target Competitor", competitor_list, index=0)

    # Preset mock SWOT for selected competitor
    if "Apex" in selected_comp:
        s = ["Proprietary custom fine-tuned SLMs for enterprise sales", "24/7 dedicated solutions engineering team included in base tier"]
        w = ["High implementation professional service costs ($15k minimum)", "Clunky legacy UI and slow query latency on reports"]
        o = ["Targeting healthcare compliance (HIPAA / SOC2 Type II) niche", "Expanding partner marketplace integrations"]
        t = ["Rapid erosion of market share in mid-market ($20k-$50k ACV)", "Customer dissatisfaction with rigid annual contracts"]
    elif "Cogni" in selected_comp:
        s = ["Largest market share (34%) and established enterprise vendor relations", "Pre-built connectors to 150+ enterprise tools"]
        w = ["High seat price ($95/user) causing mid-market customer backlash", "Opaque agent decision-making with zero reasoning audit logs", "High latency during peak hours"]
        o = ["Targeting Fortune 500 legacy transformations", "Pushing bundle deals with existing cloud enterprise agreements"]
        t = ["Vulnerable to agile multi-agent startups with lower TCO", "Customer churn toward modular, open architectures"]
    else:
        s = ["Strong natural language conversational UI", "Rapid Series B funding momentum"]
        w = ["Inconsistent reliability and 98.2% SLA (sub-par for critical workflows)", "Weak multi-agent coordination; relies on single LLM calls"]
        o = ["Aggressive discounting in mid-market tech startups", "Expanding European data residency presence"]
        t = ["Cash burn on subsidized compute pricing", "Vulnerability to price wars with enterprise incumbents"]

    swot_c1, swot_c2 = st.columns(2)
    with swot_c1:
        st.markdown(
            f"""
            <div style="background: rgba(13, 21, 39, 0.85); border: 1px solid rgba(0, 255, 157, 0.35); border-radius: 8px; padding: 16px; margin-bottom: 14px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
                <strong style="color: #00FF9D; font-size: 0.9rem; text-shadow: 0 0 8px rgba(0,255,157,0.4);">💪 Strengths (Internal Assets)</strong>
                <ul style="font-size: 0.82rem; color: #CBD5E1; margin: 8px 0 0 18px; padding: 0; line-height: 1.5;">
                    {''.join(f'<li>{item}</li>' for item in s)}
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            f"""
            <div style="background: rgba(13, 21, 39, 0.85); border: 1px solid rgba(0, 240, 255, 0.35); border-radius: 8px; padding: 16px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
                <strong style="color: #00F0FF; font-size: 0.9rem; text-shadow: 0 0 8px rgba(0,240,255,0.4);">🚀 Opportunities (Market Growth)</strong>
                <ul style="font-size: 0.82rem; color: #CBD5E1; margin: 8px 0 0 18px; padding: 0; line-height: 1.5;">
                    {''.join(f'<li>{item}</li>' for item in o)}
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with swot_c2:
        st.markdown(
            f"""
            <div style="background: rgba(13, 21, 39, 0.85); border: 1px solid rgba(255, 184, 0, 0.35); border-radius: 8px; padding: 16px; margin-bottom: 14px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
                <strong style="color: #FFB800; font-size: 0.9rem; text-shadow: 0 0 8px rgba(255,184,0,0.4);">⚠️ Weaknesses (Internal Gaps)</strong>
                <ul style="font-size: 0.82rem; color: #CBD5E1; margin: 8px 0 0 18px; padding: 0; line-height: 1.5;">
                    {''.join(f'<li>{item}</li>' for item in w)}
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            f"""
            <div style="background: rgba(13, 21, 39, 0.85); border: 1px solid rgba(255, 42, 133, 0.35); border-radius: 8px; padding: 16px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
                <strong style="color: #FF2A85; font-size: 0.9rem; text-shadow: 0 0 8px rgba(255,42,133,0.4);">🛡️ Threats (External Hazards)</strong>
                <ul style="font-size: 0.82rem; color: #CBD5E1; margin: 8px 0 0 18px; padding: 0; line-height: 1.5;">
                    {''.join(f'<li>{item}</li>' for item in t)}
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("</div>", unsafe_allow_html=True)

    # 3. Market Trends Radar
    st.markdown(
        """
        <div class="saas-card">
            <div class="saas-card-header">
                <div>
                    <h3 class="saas-card-title">📡 Industry Technology & Regulatory Radar</h3>
                    <p class="saas-card-subtitle">Emerging macro trends, agentic automation adoption, and strategic advisory.</p>
                </div>
            </div>
        """,
        unsafe_allow_html=True,
    )

    trends = get_market_trends_data()
    for trend in trends:
        impact_color = (
            "#00FF9D" if "Positive" in trend["sentiment"]
            else "#FF2A85" if "Negative" in trend["sentiment"]
            else "#00F0FF"
        )
        st.markdown(
            f"""
            <div style="border-left: 3px solid {impact_color}; background: rgba(13, 21, 39, 0.8); border-radius: 0 8px 8px 0; padding: 12px 16px; margin-bottom: 12px; border-top: 1px solid rgba(255,255,255,0.05); border-right: 1px solid rgba(255,255,255,0.05); border-bottom: 1px solid rgba(255,255,255,0.05);">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <strong style="font-size: 0.92rem; color: #F8FAFC;">{trend['trend']}</strong>
                    <span class="badge-pill badge-purple" style="font-size: 0.7rem;">Impact: {trend['sentiment']}</span>
                </div>
                <div style="font-size: 0.82rem; color: #CBD5E1; margin: 5px 0 6px 0; line-height: 1.4;">
                    {trend['impact']}
                </div>
                <div style="font-size: 0.78rem; color: #00FF9D; font-weight: 600;">
                    🎯 Recommended Counter-Play: {trend['recommended_action']}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("</div>", unsafe_allow_html=True)
