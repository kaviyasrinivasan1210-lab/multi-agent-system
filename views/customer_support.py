"""
Customer Support View — SLA Tracking, Sentiment Analysis & AI Response Assistant.
Styled with high-contrast Dark Neon Cyber aesthetic.
"""

import streamlit as st
from data.mock_data import get_support_tickets_queue, get_support_kpis
from components.kpi_card import render_kpi_card


def render_customer_support_view() -> None:
    """Renders the Customer Support & Ticket Triage view."""
    st.markdown(
        """
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.25rem;">
            <div>
                <h2 style="font-size: 1.4rem; font-weight: 800; color: #F8FAFC; margin: 0 0 4px 0; text-shadow: 0 0 12px rgba(0, 240, 255, 0.4);">
                    🎧 Customer Support & SLA Operations
                </h2>
                <p style="font-size: 0.85rem; color: #94A3B8; margin: 0;">
                    Real-time ticket queue triage, sentiment scoring, and autonomous response synthesis.
                </p>
            </div>
            <div>
                <span class="badge-pill badge-warning" style="font-size: 0.75rem;">
                    ● Agent: Support Triage Active
                </span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 1. Support Operations KPIs
    kpis = get_support_kpis()
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        render_kpi_card("Avg First Response", kpis["first_response_time"]["value"], kpis["first_response_time"]["delta"], True, kpis["first_response_time"]["subtitle"], "⏱️", "#00F0FF")
    with c2:
        render_kpi_card("Avg Resolution Speed", kpis["resolution_time"]["value"], kpis["resolution_time"]["delta"], True, kpis["resolution_time"]["subtitle"], "⚡", "#00FF9D")
    with c3:
        render_kpi_card("CSAT Rating", kpis["csat_score"]["value"], kpis["csat_score"]["delta"], True, kpis["csat_score"]["subtitle"], "⭐", "#FFB800")
    with c4:
        render_kpi_card("SLA Compliance", kpis["sla_compliance"]["value"], kpis["sla_compliance"]["delta"], True, kpis["sla_compliance"]["subtitle"], "🎯", "#B026FF")

    st.markdown("<div style='margin-top: 1.5rem;'></div>", unsafe_allow_html=True)

    # 2. Live Ticket Triage Queue
    st.markdown(
        """
        <div class="saas-card">
            <div class="saas-card-header">
                <div>
                    <h3 class="saas-card-title">📨 Active Support Ticket Queue</h3>
                    <p class="saas-card-subtitle">Tickets prioritized by SLA deadline, customer MRR, and NLP sentiment.</p>
                </div>
                <span class="badge-pill badge-danger">2 Approaching SLA</span>
            </div>
        """,
        unsafe_allow_html=True,
    )

    tickets_df = get_support_tickets_queue()

    st.dataframe(
        tickets_df,
        column_config={
            "Ticket ID": st.column_config.TextColumn("Ticket ID", width="small"),
            "Customer": st.column_config.TextColumn("Customer Account", width="medium"),
            "Category": st.column_config.TextColumn("Issue Category"),
            "Priority": st.column_config.TextColumn("Priority"),
            "Sentiment": st.column_config.TextColumn("NLP Sentiment"),
            "SLA Remaining": st.column_config.TextColumn("SLA Target"),
            "Assigned Rep": st.column_config.TextColumn("Support Engineer"),
            "Status": st.column_config.TextColumn("Ticket State"),
        },
        use_container_width=True,
        hide_index=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

    # 3. AI Copilot Ticket Resolution Workbench
    st.markdown(
        """
        <div class="saas-card">
            <div class="saas-card-header">
                <div>
                    <h3 class="saas-card-title">🤖 AI Copilot Ticket Resolution Workbench</h3>
                    <p class="saas-card-subtitle">Triage Agent cross-references client history and contract terms to craft zero-shot resolutions.</p>
                </div>
            </div>
        """,
        unsafe_allow_html=True,
    )

    selected_ticket_id = st.selectbox(
        "Select Ticket to Review & Resolve",
        tickets_df["Ticket ID"].tolist(),
        index=0,
    )

    ticket_data = tickets_df[tickets_df["Ticket ID"] == selected_ticket_id].iloc[0]

    t_col1, t_col2 = st.columns([1, 2])

    with t_col1:
        st.markdown(
            f"""
            <div style="background: rgba(13, 21, 39, 0.85); border: 1px solid rgba(0, 240, 255, 0.22); border-radius: 8px; padding: 16px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
                <div style="font-size: 0.75rem; font-weight: 700; color: #00F0FF; text-transform: uppercase; letter-spacing: 0.05em;">
                    {ticket_data['Ticket ID']} — {ticket_data['Category']}
                </div>
                <h4 style="font-size: 0.98rem; font-weight: 700; color: #F8FAFC; margin: 6px 0 10px 0;">
                    {ticket_data['Subject']}
                </h4>
                <div style="font-size: 0.78rem; color: #94A3B8; margin-bottom: 4px;">Customer: <strong style="color: #F8FAFC;">{ticket_data['Customer']}</strong></div>
                <div style="font-size: 0.78rem; color: #94A3B8; margin-bottom: 4px;">Priority: <strong style="color: #FF2A85;">{ticket_data['Priority']}</strong></div>
                <div style="font-size: 0.78rem; color: #94A3B8; margin-bottom: 4px;">NLP Sentiment: <strong style="color: #00FF9D;">{ticket_data['Sentiment']}</strong></div>
                <div style="font-size: 0.78rem; color: #94A3B8;">SLA Timer: <strong style="color: #FFB800;">{ticket_data['SLA Remaining']}</strong></div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with t_col2:
        # Pre-generated draft depending on ticket
        if "1042" in selected_ticket_id:
            default_draft = (
                "Hi Marcus,\n\n"
                "Thank you for reaching out, and I apologize for the confusion regarding the seat overage on invoice #INV-8821. "
                "Our billing engine cross-referenced your contract and verified that the 15 additional seats were part of your Q3 migration waiver.\n\n"
                "I have already processed an immediate credit memo of $1,200.00 to balance your statement. You should see the updated balance in your billing portal within the hour.\n\n"
                "Please let me know if you'd like to schedule a quick 10-minute check-in with your account manager Sarah Jenkins to review upcoming renewals."
            )
        elif "1043" in selected_ticket_id:
            default_draft = (
                "Hi Alex,\n\n"
                "Thanks for alerting us to the SAML SSO timeout issue. We inspected our identity provider logs and found a certificate expiration mismatch on the Okta metadata connector.\n\n"
                "Our engineering team has pushed a patch to resolve the clock-skew tolerance. Could you please attempt logging in again via incognito window and confirm if the session establishes normally?"
            )
        else:
            default_draft = (
                "Hello,\n\n"
                "Thank you for contacting enterprise support. Our diagnostics team has verified your configuration, "
                "and we have applied the recommended routing policy updates to your account.\n\n"
                "Please review the changes and let us know if you need further assistance."
            )

        draft_response = st.text_area(
            "AI-Synthesized Resolution Draft",
            value=default_draft,
            height=150,
            key="support_draft_textarea",
        )

        b1, b2 = st.columns(2)
        with b1:
            if st.button("🚀 Approve & Send Customer Email", key="send_support_btn", type="primary", use_container_width=True):
                st.success(f"Resolution dispatched to {ticket_data['Customer']}. Ticket {ticket_data['Ticket ID']} resolved.")
        with b2:
            if st.button("💬 Ask Triage Agent to Adjust", key="adjust_draft_btn", use_container_width=True):
                st.session_state["selected_agent"] = "support"
                st.session_state["active_view"] = "ai_chat"
                st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)
