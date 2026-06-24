"""Dream Marketplace — AI Business Analyst."""

from .agents import (
    create_business_planner_agent,
    create_market_analyst_agent,
    create_competitor_analyst_agent,
    create_finance_analyst_agent,
)
from .tools import get_tools
from .memory import get_memory_base
from .prompts import (
    AGENT_1_BUSINESS_PLANNER_PROMPT,
    AGENT_2_MARKET_ANALYST_PROMPT,
    AGENT_3_COMPETITOR_ANALYST_PROMPT,
    AGENT_4_FINANCE_ANALYST_PROMPT,
)
from .utils import format_report
from .main import run_business_analyst, main

__version__ = "1.0.0"
__all__ = [
    "create_business_planner_agent",
    "create_market_analyst_agent",
    "create_competitor_analyst_agent",
    "create_finance_analyst_agent",
    "get_tools",
    "get_memory_base",
    "AGENT_1_BUSINESS_PLANNER_PROMPT",
    "AGENT_2_MARKET_ANALYST_PROMPT",
    "AGENT_3_COMPETITOR_ANALYST_PROMPT",
    "AGENT_4_FINANCE_ANALYST_PROMPT",
    "format_report",
    "run_business_analyst",
    "main",
]
