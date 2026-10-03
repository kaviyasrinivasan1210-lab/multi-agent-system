"""
Reusable SaaS KPI Metric Card Component.
"""

import streamlit as st


def render_kpi_card(
    label: str,
    value: str,
    delta: str = "",
    is_positive: bool = True,
    subtitle: str = "",
    icon: str = "📈",
    accent_color: str = "#00F0FF",
) -> None:
    """Render a modern SaaS KPI card with neon delta pill badge and glowing icon."""
    delta_class = "badge-success" if is_positive else "badge-danger"
    delta_icon = "↑" if is_positive else "↓"

    delta_html = ""
    if delta:
        delta_html = f"""
        <span class="badge-pill {delta_class}">
            {delta_icon} {delta}
        </span>
        """

    card_html = f"""
    <div class="kpi-metric-box" style="border-top: 2px solid {accent_color}; box-shadow: 0 4px 20px rgba(0,0,0,0.5), 0 0 12px {accent_color}22;">
        <div class="kpi-metric-header">
            <span class="kpi-metric-label">{label}</span>
            <div class="kpi-metric-icon" style="background-color: {accent_color}25; color: {accent_color}; box-shadow: 0 0 12px {accent_color}55;">
                {icon}
            </div>
        </div>
        <div class="kpi-metric-value">{value}</div>
        <div class="kpi-metric-footer">
            {delta_html}
            <span>{subtitle}</span>
        </div>
    </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)
