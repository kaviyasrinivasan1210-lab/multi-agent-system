"""
Neon Cyber Dark Theme Plotly visual generator for AI Business Assistant.
Designed for high-contrast presentation with neon glowing data traces,
translucent grid lines, and crisp typography.
"""

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from typing import Optional
from core.config import COLOR_PALETTE


def apply_enterprise_theme(fig: go.Figure, height: int = 360, title: Optional[str] = None) -> go.Figure:
    """Apply consistent neon dark styling to any Plotly chart."""
    fig.update_layout(
        title=dict(
            text=f"<b>{title}</b>" if title else "",
            font=dict(size=14, color="#F8FAFC", family="Plus Jakarta Sans, sans-serif"),
            x=0.01,
            y=0.96,
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        height=height,
        margin=dict(l=20, r=20, t=40 if title else 20, b=20),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            font=dict(size=11, color="#94A3B8", family="Plus Jakarta Sans"),
        ),
        font=dict(family="Plus Jakarta Sans, sans-serif", color="#94A3B8", size=11),
        hoverlabel=dict(
            bgcolor="#0A1020",
            bordercolor="#00F0FF",
            font_size=12,
            font_family="Plus Jakarta Sans",
            font_color="#F8FAFC",
        ),
    )
    fig.update_xaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor="rgba(255, 255, 255, 0.08)",
        linecolor="rgba(0, 240, 255, 0.25)",
        tickfont=dict(size=10, color="#94A3B8"),
    )
    fig.update_yaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor="rgba(255, 255, 255, 0.08)",
        linecolor="rgba(0, 240, 255, 0.25)",
        tickfont=dict(size=10, color="#94A3B8"),
    )
    return fig


def create_revenue_trend_chart(df: pd.DataFrame) -> go.Figure:
    """Generate 12-month Actual vs Target vs AI Forecast revenue chart with neon traces."""
    fig = go.Figure()

    # Target line (dashed muted gray)
    fig.add_trace(
        go.Scatter(
            x=df["Month"],
            y=df["Target Revenue"],
            mode="lines",
            name="Target Quota",
            line=dict(color="#64748B", width=2, dash="dash"),
            hovertemplate="Target: $%{y:,.0f}<extra></extra>",
        )
    )

    # Actual revenue (vibrant neon cyan line with subtle fill)
    fig.add_trace(
        go.Scatter(
            x=df["Month"],
            y=df["Actual Revenue"],
            mode="lines+markers",
            name="Actual Revenue",
            line=dict(color="#00F0FF", width=3, shape="spline"),
            marker=dict(size=7, color="#00F0FF", line=dict(width=1, color="#FFFFFF")),
            fill="tozeroy",
            fillcolor="rgba(0, 240, 255, 0.12)",
            hovertemplate="Actual: $%{y:,.0f}<extra></extra>",
        )
    )

    # AI Forecast (neon purple dashed line)
    fig.add_trace(
        go.Scatter(
            x=df["Month"],
            y=df["AI Forecast"],
            mode="lines+markers",
            name="AI Multi-Agent Forecast",
            line=dict(color="#B026FF", width=2.5, dash="dot", shape="spline"),
            marker=dict(size=6, color="#B026FF"),
            hovertemplate="AI Forecast: $%{y:,.0f}<extra></extra>",
        )
    )

    return apply_enterprise_theme(fig, height=350, title="Monthly Revenue vs Quota & AI Forecast")


def create_pipeline_funnel_chart(df: pd.DataFrame) -> go.Figure:
    """Generate deal progression funnel chart with neon gradient stages."""
    fig = go.Figure(
        go.Funnel(
            y=df["Stage"],
            x=df["Value ($)"],
            textinfo="value+percent initial",
            texttemplate="$%{value:,.0f} (%{percentInitial})",
            marker=dict(
                color=["#00F0FF", "#38BDF8", "#818CF8", "#A855F7", "#B026FF", "#D946EF", "#00FF9D"]
            ),
            connector=dict(line=dict(color="rgba(0, 240, 255, 0.3)", width=1)),
            hovertemplate="<b>%{y}</b><br>Pipeline Value: $%{x:,.0f}<extra></extra>",
        )
    )
    return apply_enterprise_theme(fig, height=360, title="Sales Pipeline Funnel by Deal Value")


def create_marketing_roas_chart(df: pd.DataFrame) -> go.Figure:
    """Generate channel ROAS comparison bar chart with neon color scale."""
    sorted_df = df.sort_values(by="ROAS (x)", ascending=True)

    fig = go.Figure(
        go.Bar(
            y=sorted_df["Channel"],
            x=sorted_df["ROAS (x)"],
            orientation="h",
            marker=dict(
                color=sorted_df["ROAS (x)"],
                colorscale=[[0, "#38BDF8"], [0.5, "#00F0FF"], [1.0, "#00FF9D"]],
                showscale=False,
                line=dict(color="rgba(0, 240, 255, 0.3)", width=1),
            ),
            text=[f"{val:.1f}x" for val in sorted_df["ROAS (x)"]],
            textposition="auto",
            textfont=dict(color="#FFFFFF", size=11),
            hovertemplate="<b>%{y}</b><br>Return on Ad Spend: %{x:.2f}x<extra></extra>",
        )
    )
    return apply_enterprise_theme(fig, height=320, title="Channel Return on Ad Spend (ROAS)")


def create_cac_ltv_chart(df: pd.DataFrame) -> go.Figure:
    """Generate CAC vs LTV progression chart with neon bars and line."""
    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=df["Quarter"],
            y=df["CAC ($)"],
            name="Blended CAC ($)",
            marker=dict(color="#FF2A85", line=dict(color="rgba(255, 42, 133, 0.5)", width=1)),
            hovertemplate="CAC: $%{y:,.0f}<extra></extra>",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df["Quarter"],
            y=df["LTV ($)"],
            name="Customer LTV ($)",
            mode="lines+markers",
            yaxis="y2",
            line=dict(color="#00FF9D", width=3),
            marker=dict(size=8, color="#00FF9D", line=dict(color="#FFFFFF", width=1)),
            hovertemplate="LTV: $%{y:,.0f}<extra></extra>",
        )
    )

    fig.update_layout(
        yaxis2=dict(
            title="LTV ($)",
            overlaying="y",
            side="right",
            showgrid=False,
            tickfont=dict(size=10, color="#94A3B8"),
        )
    )

    return apply_enterprise_theme(fig, height=320, title="Quarterly CAC Reduction vs LTV Growth")


def create_customer_health_scatter(df: pd.DataFrame) -> go.Figure:
    """Generate Customer Health vs MRR risk matrix with neon glowing clusters."""
    color_map = {"Low": "#00FF9D", "Medium": "#FFB800", "High": "#FF2A85"}

    fig = px.scatter(
        df,
        x="Health",
        y="MRR ($)",
        size="MRR ($)",
        color="Risk",
        hover_name="Account",
        hover_data={"Health": True, "MRR ($)": ":$,.0f", "Days Inactive": True, "Risk": False},
        color_discrete_map=color_map,
        size_max=35,
    )

    # Add quadrant thresholds with neon dash lines
    fig.add_vline(x=50, line_width=1, line_dash="dash", line_color="rgba(0, 240, 255, 0.35)")
    fig.add_hline(y=10000, line_width=1, line_dash="dash", line_color="rgba(0, 240, 255, 0.35)")

    fig.add_annotation(
        x=25, y=17000,
        text="CRITICAL ACCOUNTS (High Value, Low Health)",
        showarrow=False,
        font=dict(size=10, color="#FF2A85", family="Plus Jakarta Sans"),
    )
    fig.add_annotation(
        x=75, y=17000,
        text="ENTERPRISE CHAMPIONS",
        showarrow=False,
        font=dict(size=10, color="#00FF9D", family="Plus Jakarta Sans"),
    )

    return apply_enterprise_theme(fig, height=380, title="Customer Risk Matrix: Health Score vs MRR")


def create_competitor_share_donut(df: pd.DataFrame) -> go.Figure:
    """Generate market share distribution donut chart with neon arcs."""
    fig = go.Figure(
        go.Pie(
            labels=df["Competitor"],
            values=df["Market Share (%)"],
            hole=0.55,
            marker=dict(
                colors=["#00F0FF", "#B026FF", "#00FF9D", "#38BDF8", "#FFB800"],
                line=dict(color="#070B14", width=2),
            ),
            textinfo="label+percent",
            textfont=dict(color="#FFFFFF"),
            hovertemplate="<b>%{label}</b><br>Share: %{percent}<extra></extra>",
        )
    )
    return apply_enterprise_theme(fig, height=320, title="Enterprise Market Share Breakdown")
