"""Main flow for Business Analyst."""

import logging
import os
from dotenv import load_dotenv
from .agents import (
    create_business_planner_agent,
    create_market_analyst_agent,
    create_competitor_analyst_agent,
    create_finance_analyst_agent,
)
from .memory import get_memory_base

load_dotenv()
logging.basicConfig(level=logging.INFO)


def run_business_analyst(idea: str) -> str:
    """Main function running the Business Analyst."""

    print("\n" + "=" * 60)
    print("🧠 DREAM MARKETPLACE — AI Business Analyst")
    print("=" * 60)
    print(f"📝 Idea: {idea}\n")
    print(f"🧠 Model: {os.getenv('MODEL_NAME', 'gpt-4o-mini')}\n")

    # === Agent 1: Business Planner ===
    print("🔍 Agent 1: Business Planner...")
    planner = create_business_planner_agent()
    plan = planner.invoke({"input": idea})
    areas = plan["output"]
    print(f"✅ Areas for analysis:\n{areas}\n")

    # === Agent 2: Market Analyst ===
    print("🔍 Agent 2: Market Analyst...")
    market_agent = create_market_analyst_agent()
    market_result = market_agent.invoke({"input": areas})
    market_analysis = market_result["output"]
    print(f"✅ Market analysis:\n{market_analysis}\n")

    # === Agent 3: Competitor Analyst ===
    print("🔍 Agent 3: Competitor Analyst...")
    competitor_agent = create_competitor_analyst_agent()
    competitor_result = competitor_agent.invoke({"input": areas})
    competitor_analysis = competitor_result["output"]
    print(f"✅ Competitor analysis:\n{competitor_analysis}\n")

    # === Agent 4: Finance & Risk Analyst ===
    print("🔍 Agent 4: Finance & Risk Analyst...")
    memory = get_memory_base()
    finance_agent = create_finance_analyst_agent(memory=memory)
    combined = f"Idea: {idea}\n\nMarket analysis:\n{market_analysis}\n\nCompetitor analysis:\n{competitor_analysis}"
    finance_result = finance_agent.invoke({"input": combined})
    finance_report = finance_result["output"]
    print(f"✅ Financial report:\n{finance_report}\n")

    # === Final Report ===
    final_report = f"Idea: {idea}\n\n📊 MARKET ANALYSIS:\n{market_analysis}\n\n🏆 COMPETITORS:\n{competitor_analysis}\n\n💰 FINANCIAL ASSESSMENT:\n{finance_report}"

    return final_report


def main():
    """Main interactive function."""

    print("🧠 DREAM MARKETPLACE — AI Business Analyst")
    print(f"📦 Model: {os.getenv('MODEL_NAME', 'gpt-4o-mini')}")
    print("Type 'exit' to quit.\n")

    while True:
        idea = input("❓ Enter your business idea: ")

        if idea.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break

        if not idea.strip():
            print("⚠️ Please enter an idea.\n")
            continue

        try:
            result = run_business_analyst(idea)
            print("\n" + "=" * 60)
            print("📋 STARTUP REPORT:")
            print("=" * 60)
            print(result)
            print("=" * 60 + "\n")

        except Exception as e:
            print(f"❌ Error: {str(e)}\n")


if __name__ == "__main__":
    main()
