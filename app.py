"""
AI Business Assistant — Multi-Agent AI for Smarter Business Decisions
Main application entry point and routing coordinator.
"""

import os
import streamlit as st

# 1. Page Configuration (Must be first Streamlit command)
st.set_page_config(
    page_title="AI Business Assistant – Multi-Agent AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 2. Inject Enterprise SaaS CSS
def load_css() -> None:
    css_path = os.path.join(os.path.dirname(__file__), "assets", "styles.css")
    if os.path.exists(css_path):
        with open(css_path, "r", encoding="utf-8") as f:
            custom_css = f.read()
            st.markdown(f"<style>{custom_css}</style>", unsafe_allow_html=True)

load_css()

# 3. Initialize Global Session State
from core.state import init_session_state
init_session_state()

# 4. Render Persistent Dark Navy Sidebar
from components.sidebar import render_sidebar
active_view_id = render_sidebar()

# 5. Route to Active View
from views.dashboard import render_dashboard_view
from views.ai_chat import render_ai_chat_view
from views.sales_analytics import render_sales_analytics_view
from views.marketing import render_marketing_view
from views.customers import render_customers_view
from views.customer_support import render_customer_support_view
from views.business_research import render_business_research_view
from views.reports_repo import render_reports_repo_view

VIEW_DISPATCHER = {
    "dashboard": render_dashboard_view,
    "ai_chat": render_ai_chat_view,
    "sales_analytics": render_sales_analytics_view,
    "marketing": render_marketing_view,
    "customers": render_customers_view,
    "customer_support": render_customer_support_view,
    "business_research": render_business_research_view,
    "reports_repo": render_reports_repo_view,
}

render_func = VIEW_DISPATCHER.get(active_view_id, render_dashboard_view)
render_func()
