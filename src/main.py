"""Główny przepływ dla Business Analyst."""

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
    """Główna funkcja uruchamiająca Business Analyst."""

    print("\n" + "=" * 60)
    print("🧠 DREAM MARKETPLACE — AI Business Analyst")
    print("=" * 60)
    print(f"📝 Pomysł: {idea}\n")
    print(f"🧠 Model: {os.getenv('MODEL_NAME', 'gpt-4o-mini')}\n")

    # === Agent 1: Business Planner ===
    print("🔍 Agent 1: Business Planner...")
    planner = create_business_planner_agent()
    plan = planner.invoke({"input": idea})
    areas = plan["output"]
    print(f"✅ Obszary do analizy:\n{areas}\n")

    # === Agent 2: Market Analyst ===
    print("🔍 Agent 2: Market Analyst...")
    market_agent = create_market_analyst_agent()
    market_result = market_agent.invoke({"input": areas})
    market_analysis = market_result["output"]
    print(f"✅ Analiza rynku:\n{market_analysis}\n")

    # === Agent 3: Competitor Analyst ===
    print("🔍 Agent 3: Competitor Analyst...")
    competitor_agent = create_competitor_analyst_agent()
    competitor_result = competitor_agent.invoke({"input": areas})
    competitor_analysis = competitor_result["output"]
    print(f"✅ Analiza konkurencji:\n{competitor_analysis}\n")

    # === Agent 4: Finance & Risk Analyst ===
    print("🔍 Agent 4: Finance & Risk Analyst...")
    memory = get_memory_base()
    finance_agent = create_finance_analyst_agent(memory=memory)
    combined = f"Pomysł: {idea}\n\nAnaliza rynku:\n{market_analysis}\n\nAnaliza konkurencji:\n{competitor_analysis}"
    finance_result = finance_agent.invoke({"input": combined})
    finance_report = finance_result["output"]
    print(f"✅ Raport finansowy:\n{finance_report}\n")

    # === Final Report ===
    final_report = f"Pomysł: {idea}\n\n📊 ANALIZA RYNKU:\n{market_analysis}\n\n🏆 KONKURENCJA:\n{competitor_analysis}\n\n💰 OCENA FINANSOWA:\n{finance_report}"

    return final_report


def main():
    """Główna funkcja interaktywna."""

    print("🧠 DREAM MARKETPLACE — AI Business Analyst")
    print(f"📦 Model: {os.getenv('MODEL_NAME', 'gpt-4o-mini')}")
    print("Wpisz 'exit' aby zakończyć.\n")

    while True:
        idea = input("❓ Podaj pomysł na biznes: ")

        if idea.lower() in ["exit", "quit"]:
            print("👋 Do widzenia!")
            break

        if not idea.strip():
            print("⚠️ Proszę wpisać pomysł.\n")
            continue

        try:
            result = run_business_analyst(idea)
            print("\n" + "=" * 60)
            print("📋 RAPORT STARTUPOWY:")
            print("=" * 60)
            print(result)
            print("=" * 60 + "\n")

        except Exception as e:
            print(f"❌ Błąd: {str(e)}\n")


if __name__ == "__main__":
    main()
