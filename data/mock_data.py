"""
Realistic business datasets and mock generation utilities for AI Business Assistant.
Covers Sales, Marketing, Customers, Support, Research, and Executive Metrics.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, Any, List


# -----------------------------------------------------------------------------
# 1. Executive Summary & KPIs
# -----------------------------------------------------------------------------
def get_executive_kpis() -> Dict[str, Any]:
    return {
        "arr": {"value": "$1,248,500", "delta": "+18.4%", "is_positive": True, "subtitle": "vs $1.05M prior year"},
        "mrr": {"value": "$104,040", "delta": "+4.8%", "is_positive": True, "subtitle": "Net new MRR: +$4,750"},
        "pipeline": {"value": "$2,840,000", "delta": "+12.1%", "is_positive": True, "subtitle": "48 qualified deals"},
        "cac": {"value": "$482", "delta": "-8.2%", "is_positive": True, "subtitle": "Target: < $500"},
        "ltv_cac_ratio": {"value": "4.8x", "delta": "+0.4x", "is_positive": True, "subtitle": "Healthy B2B benchmark"},
        "nrr": {"value": "114.2%", "delta": "+2.1%", "is_positive": True, "subtitle": "Expansion revenue driving growth"},
        "csat": {"value": "94.2%", "delta": "+1.5%", "is_positive": True, "subtitle": "From 312 survey responses"},
        "active_churn_risk": {"value": "4 Accounts", "delta": "-2 accounts", "is_positive": True, "subtitle": "$38.4k annual revenue at risk"},
    }


def get_monthly_revenue_history() -> pd.DataFrame:
    months = [
        "Oct 2025", "Nov 2025", "Dec 2025", "Jan 2026", "Feb 2026", "Mar 2026",
        "Apr 2026", "May 2026", "Jun 2026", "Jul 2026", "Aug 2026", "Sep 2026"
    ]
    actual_revenue = [72000, 75500, 78200, 81000, 84200, 87500, 91000, 94800, 98200, 100500, 102400, 104040]
    target_revenue = [70000, 73000, 76000, 79000, 82000, 85000, 88000, 92000, 95000, 98000, 101000, 103000]
    forecast_ai =    [72000, 75500, 78200, 81000, 84200, 87500, 91000, 94800, 98200, 100500, 103100, 105200]

    return pd.DataFrame({
        "Month": months,
        "Actual Revenue": actual_revenue,
        "Target Revenue": target_revenue,
        "AI Forecast": forecast_ai,
    })


def get_agent_swarm_events() -> List[Dict[str, str]]:
    return [
        {
            "time": "12 mins ago",
            "agent": "Customer Retention Agent",
            "icon": "👥",
            "type": "warning",
            "event": "Flagged Apex Logistics (MRR $12,500) due to 38% drop in active weekly seats.",
        },
        {
            "time": "34 mins ago",
            "agent": "Sales Analyst Agent",
            "icon": "📊",
            "type": "success",
            "event": "Deal closed: HyperScale Bio ($84,000 ARR) signed Enterprise 2-year contract.",
        },
        {
            "time": "1 hr ago",
            "agent": "Market Research Agent",
            "icon": "🔎",
            "type": "info",
            "event": "Competitor StratIQ updated public enterprise pricing tier from $80 to $95/user/mo.",
        },
        {
            "time": "2 hrs ago",
            "agent": "Support Triage Agent",
            "icon": "🎧",
            "type": "success",
            "event": "Drafted and resolved critical billing ticket #1042 in 18 minutes (SLA met).",
        },
        {
            "time": "3 hrs ago",
            "agent": "Growth & Marketing Agent",
            "icon": "📢",
            "type": "info",
            "event": "LinkedIn campaign 'Autonomous AI 2.0' surpassed benchmark at 3.82x ROAS.",
        },
    ]


# -----------------------------------------------------------------------------
# 2. Sales Analytics Dataset
# -----------------------------------------------------------------------------
def get_sales_pipeline_data() -> pd.DataFrame:
    return pd.DataFrame({
        "Stage": ["Lead", "MQL", "SQL", "Demo Held", "Proposal", "Negotiation", "Closed Won"],
        "Deal Count": [140, 85, 52, 38, 24, 15, 11],
        "Value ($)": [700000, 680000, 624000, 570000, 480000, 420000, 248000],
        "Conversion Rate (%)": [100.0, 60.7, 61.1, 73.0, 63.1, 62.5, 73.3],
    })


def get_sales_rep_performance() -> pd.DataFrame:
    return pd.DataFrame({
        "Sales Representative": ["Sarah Jenkins", "Michael Chang", "Elena Rostova", "David Miller", "Amina Patel"],
        "Quota ($)": [250000, 250000, 220000, 200000, 200000],
        "Closed ARR ($)": [292000, 274000, 235000, 198000, 215000],
        "Attainment (%)": [116.8, 109.6, 106.8, 99.0, 107.5],
        "Active Deals": [12, 10, 8, 9, 11],
        "Win Rate (%)": [38.2, 34.5, 36.0, 29.8, 33.1],
        "Avg Deal Size ($)": [24300, 27400, 29300, 22000, 19500],
    })


def get_sales_by_tier() -> pd.DataFrame:
    months = ["May 2026", "Jun 2026", "Jul 2026", "Aug 2026", "Sep 2026"]
    return pd.DataFrame({
        "Month": months,
        "Enterprise Tier": [52000, 54500, 56000, 57800, 59200],
        "Mid-Market Tier": [28000, 29200, 30100, 30500, 31100],
        "Starter / Pro": [14800, 14500, 14400, 14100, 13740],
    })


# -----------------------------------------------------------------------------
# 3. Marketing Dataset
# -----------------------------------------------------------------------------
def get_marketing_channels_data() -> pd.DataFrame:
    return pd.DataFrame({
        "Channel": ["LinkedIn Ads", "Google Search", "Organic SEO", "Email Nurture", "Industry Webinars", "Partner Referral"],
        "Spend ($)": [18500, 14200, 4500, 2100, 6800, 3400],
        "Leads Generated": [480, 410, 320, 210, 190, 85],
        "Customers Won": [24, 16, 19, 14, 11, 8],
        "CAC ($)": [770, 887, 236, 150, 618, 425],
        "Revenue Attributed ($)": [70800, 37200, 56000, 39200, 29700, 26400],
        "ROAS (x)": [3.82, 2.62, 12.44, 18.66, 4.36, 7.76],
    })


def get_cac_ltv_history() -> pd.DataFrame:
    quarters = ["Q3 2025", "Q4 2025", "Q1 2026", "Q2 2026", "Q3 2026"]
    return pd.DataFrame({
        "Quarter": quarters,
        "CAC ($)": [560, 535, 510, 495, 482],
        "LTV ($)": [2100, 2180, 2260, 2340, 2410],
        "LTV:CAC Ratio": [3.75, 4.07, 4.43, 4.72, 4.99],
    })


def get_ai_ad_copy_templates() -> List[Dict[str, str]]:
    return [
        {
            "platform": "LinkedIn Sponsored InMail",
            "angle": "Executive Decision Automation",
            "headline": "Cut business reporting from 14 hours to 10 seconds with Autonomous Multi-Agent AI.",
            "body": "Dear {First_Name}, While your competitors still build manual spreadsheets, enterprise leaders use autonomous AI agents to predict Q4 churn, optimize ad spend, and surface growth bottlenecks in real-time.",
            "cta": "Request Enterprise Access (Free 14-Day Pilot)",
            "predicted_ctr": "4.6% (Top 5% benchmark)",
        },
        {
            "platform": "Google Search Headline",
            "angle": "LangGraph & Enterprise RAG",
            "headline": "Autonomous AI Business Assistant | Multi-Agent Architecture",
            "body": "Empower your executive team with dedicated Sales, Marketing, and Churn AI Agents. Transparent reasoning traces, instant data connectors, and strict data security.",
            "cta": "See Live Interactive Demo",
            "predicted_ctr": "5.2%",
        },
        {
            "platform": "Email Nurture (At-Risk Save)",
            "angle": "Proactive Value Restoration",
            "headline": "We noticed a drop in your team's workflow activity — here to help.",
            "body": "Hi {First_Name}, our platform detected that your seat utilization dipped over the past 3 weeks. We have unlocked 3 complimentary agent workflows for your team and our Customer Success architect is available for a 15-minute tune-up.",
            "cta": "Schedule 15-Min Executive Review",
            "predicted_ctr": "28.4% Open | 12.1% Click",
        },
    ]


# -----------------------------------------------------------------------------
# 4. Customer Accounts & Churn Matrix
# -----------------------------------------------------------------------------
def get_customer_accounts_dataset() -> pd.DataFrame:
    accounts = [
        {"Account": "Apex Logistics Corp", "Tier": "Enterprise", "MRR ($)": 12500, "Health": 38, "Risk": "High", "NPS": 4, "Owner": "Sarah Jenkins", "Days Inactive": 18, "Status": "At Risk"},
        {"Account": "Nexus Cloud Systems", "Tier": "Enterprise", "MRR ($)": 9200, "Health": 42, "Risk": "High", "NPS": 5, "Owner": "Elena Rostova", "Days Inactive": 14, "Status": "At Risk"},
        {"Account": "Veritas Health Tech", "Tier": "Mid-Market", "MRR ($)": 4800, "Health": 54, "Risk": "Medium", "NPS": 6, "Owner": "David Miller", "Days Inactive": 9, "Status": "Monitoring"},
        {"Account": "Quantum Fintech Lab", "Tier": "Enterprise", "MRR ($)": 14800, "Health": 96, "Risk": "Low", "NPS": 10, "Owner": "Michael Chang", "Days Inactive": 1, "Status": "Champion"},
        {"Account": "Starlight Media Group", "Tier": "Mid-Market", "MRR ($)": 5600, "Health": 88, "Risk": "Low", "NPS": 9, "Owner": "Amina Patel", "Days Inactive": 2, "Status": "Healthy"},
        {"Account": "OmniRetail Global", "Tier": "Enterprise", "MRR ($)": 18400, "Health": 92, "Risk": "Low", "NPS": 10, "Owner": "Sarah Jenkins", "Days Inactive": 0, "Status": "Champion"},
        {"Account": "Vanguard Robotics", "Tier": "Mid-Market", "MRR ($)": 6200, "Health": 78, "Risk": "Low", "NPS": 8, "Owner": "Elena Rostova", "Days Inactive": 4, "Status": "Healthy"},
        {"Account": "Cobalt Cybersecurity", "Tier": "Enterprise", "MRR ($)": 11000, "Health": 84, "Risk": "Low", "NPS": 9, "Owner": "Michael Chang", "Days Inactive": 3, "Status": "Healthy"},
        {"Account": "Pinnacle Energy Inc", "Tier": "Mid-Market", "MRR ($)": 5900, "Health": 48, "Risk": "Medium", "NPS": 6, "Owner": "David Miller", "Days Inactive": 11, "Status": "Monitoring"},
        {"Account": "AeroDynamics Labs", "Tier": "Starter", "MRR ($)": 1200, "Health": 32, "Risk": "High", "NPS": 3, "Owner": "Amina Patel", "Days Inactive": 22, "Status": "At Risk"},
    ]
    return pd.DataFrame(accounts)


# -----------------------------------------------------------------------------
# 5. Customer Support Tickets & SLAs
# -----------------------------------------------------------------------------
def get_support_tickets_queue() -> pd.DataFrame:
    tickets = [
        {
            "Ticket ID": "TCK-1042",
            "Customer": "Apex Logistics Corp",
            "Subject": "Invoice overcharge on additional user seats",
            "Priority": "Urgent",
            "Category": "Billing",
            "Sentiment": "Negative (-0.72)",
            "SLA Remaining": "38 mins",
            "AI Draft Ready": "Yes",
            "Status": "Open",
        },
        {
            "Ticket ID": "TCK-1043",
            "Customer": "Nexus Cloud Systems",
            "Subject": "SSO SAML authentication timeout during login",
            "Priority": "High",
            "Category": "Authentication",
            "Sentiment": "Negative (-0.58)",
            "SLA Remaining": "1 hr 12 mins",
            "AI Draft Ready": "Yes",
            "Status": "Open",
        },
        {
            "Ticket ID": "TCK-1044",
            "Customer": "Quantum Fintech Lab",
            "Subject": "Request for custom LangGraph webhook export",
            "Priority": "Medium",
            "Category": "Feature Request",
            "Sentiment": "Positive (+0.84)",
            "SLA Remaining": "3 hrs 40 mins",
            "AI Draft Ready": "Yes",
            "Status": "In Progress",
        },
        {
            "Ticket ID": "TCK-1045",
            "Customer": "OmniRetail Global",
            "Subject": "API Rate limit increase for Black Friday batch test",
            "Priority": "High",
            "Category": "API / Infrastructure",
            "Sentiment": "Neutral (+0.12)",
            "SLA Remaining": "2 hrs 10 mins",
            "AI Draft Ready": "Yes",
            "Status": "In Progress",
        },
        {
            "Ticket ID": "TCK-1046",
            "Customer": "Pinnacle Energy Inc",
            "Subject": "Export to PDF fails with 500 error on heavy table",
            "Priority": "Medium",
            "Category": "Bug Report",
            "Sentiment": "Negative (-0.41)",
            "SLA Remaining": "4 hrs 15 mins",
            "AI Draft Ready": "Yes",
            "Status": "Open",
        },
    ]
    return pd.DataFrame(tickets)


def get_support_kpis() -> Dict[str, Any]:
    return {
        "first_response_time": {"value": "14.2 min", "delta": "-3.8 min", "subtitle": "SLA Benchmark: < 45 min"},
        "resolution_time": {"value": "2.4 hrs", "delta": "-0.6 hrs", "subtitle": "Median resolution speed"},
        "csat_score": {"value": "94.2%", "delta": "+1.5%", "subtitle": "Positive ratings (9-10/10)"},
        "sla_compliance": {"value": "98.8%", "delta": "+0.6%", "subtitle": "3 breaches out of 248 tickets"},
    }


# -----------------------------------------------------------------------------
# 6. Business Research & Competitor Intelligence
# -----------------------------------------------------------------------------
def get_competitor_matrix() -> pd.DataFrame:
    return pd.DataFrame({
        "Competitor": ["StratIQ Enterprise", "InsightWave AI", "CognitivePulse", "NextDecision Lab"],
        "Market Share (%)": [34.0, 22.5, 16.0, 11.5],
        "Starting Price ($/mo)": [95, 79, 65, 89],
        "Key Strength": ["Broad ecosystem integrations", "Strong natural language UI", "Low entry pricing", "Custom LLM fine-tuning"],
        "Core Weakness": ["High price, opaque reasoning", "Frequent latency spikes", "Weak customer support", "Complex enterprise setup"],
        "Recent Move": ["Raised prices by 18%", "Acquired open-source UI kit", "Launched EU data center", "Closed Series B funding"],
        "AI Threat Level": ["High", "Medium", "Low", "Medium"],
    })


def get_market_trends_data() -> List[Dict[str, str]]:
    return [
        {
            "trend": "Multi-Agent State Machine Orchestration (LangGraph standard)",
            "impact": "Very High",
            "readiness": "Our Architecture Leads",
            "description": "Enterprises are abandoning monolithic single-prompt LLM wrappers in favor of modular stateful multi-agent teams with transparent tool verification.",
        },
        {
            "trend": "Executive Auditability & Reasoning Inspection",
            "impact": "High",
            "readiness": "Implemented in UI",
            "description": "Compliance demands that every AI business recommendation expose its step-by-step reasoning and data retrieval traces before execution.",
        },
        {
            "trend": "Autonomous Real-time Churn Mitigation",
            "impact": "High",
            "readiness": "Beta Stage",
            "description": "Automated cross-referencing of login frequency with customer sentiment to trigger proactive retention offers within minutes.",
        },
        {
            "trend": "Private Enterprise RAG & SQLite Storage",
            "impact": "Medium",
            "readiness": "Schema Ready",
            "description": "On-premise / private cloud embedding stores allowing enterprise executives to chat with proprietary transactional records securely.",
        },
    ]


# -----------------------------------------------------------------------------
# 7. Reports Repository & Audit Logs
# -----------------------------------------------------------------------------
def get_repository_documents() -> pd.DataFrame:
    return pd.DataFrame({
        "Document Name": [
            "Q3 Executive Business Review (EBR).pdf",
            "Weekly Multi-Agent Revenue Briefing.pdf",
            "Customer Churn Risk Mitigation Matrix.csv",
            "Marketing Channel Attribution & ROAS Analysis.xlsx",
            "Competitor Pricing Intelligence Radar.pdf",
            "Customer Support SLA & CSAT Quarterly Audit.pdf",
        ],
        "Generated By": [
            "Executive Orchestrator",
            "Sales Analyst Agent",
            "Customer Retention Agent",
            "Growth & Marketing Agent",
            "Market Research Agent",
            "Support Triage Agent",
        ],
        "Generated Date": [
            "Sep 15, 2026",
            "Sep 17, 2026",
            "Sep 18, 2026",
            "Sep 12, 2026",
            "Sep 10, 2026",
            "Sep 05, 2026",
        ],
        "File Size": ["2.4 MB", "840 KB", "180 KB", "1.2 MB", "960 KB", "1.5 MB"],
        "Status": ["Approved", "Current", "Action Required", "Approved", "Verified", "Archived"],
    })


def get_agent_audit_logs() -> pd.DataFrame:
    return pd.DataFrame({
        "Timestamp": [
            "2026-09-18 11:42:10",
            "2026-09-18 10:15:32",
            "2026-09-18 09:20:45",
            "2026-09-18 08:30:12",
            "2026-09-17 17:05:00",
        ],
        "Agent": [
            "Customer Retention Agent",
            "Support Triage Agent",
            "Sales Analyst Agent",
            "Market Research Agent",
            "Executive Orchestrator",
        ],
        "Action Executed": [
            "Generated proactive retention play for Apex Logistics",
            "Synthesized instant empathetic draft for Ticket #1042",
            "Updated Q4 weighted revenue forecast via ARIMA model",
            "Detected Competitor StratIQ pricing increase",
            "Compiled Weekly Multi-Agent Executive Briefing",
        ],
        "Confidence": ["96.2%", "94.5%", "98.1%", "99.0%", "95.8%"],
        "Impact Level": ["High (Revenue Protection)", "Medium (Customer SLA)", "High (Board Reporting)", "Strategic", "Company-wide"],
    })
