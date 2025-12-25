from agents.signal_extractor import run_signal_extraction
from agents.context_retriever import run_context_retrieval
from agents.impact_forecaster import (
    run_impact_forecast,
    sanitize_forecast,
    validate_rationale
)

import json

def run_full_pipeline(news_text: str) -> dict:
    with open("prompts/signal_prompt.md") as f:
        signal_prompt = f.read()

    with open("prompts/context_prompt.md") as f:
        context_prompt = f.read()

    with open("prompts/forecast_prompt.md") as f:
        forecast_prompt = f.read()

    signal = run_signal_extraction(news_text, signal_prompt)
    context = run_context_retrieval(signal, context_prompt)

    forecast = run_impact_forecast(signal, context, forecast_prompt)
    forecast = sanitize_forecast(forecast)
    forecast = validate_rationale(signal, forecast)

    return {
        "signal": signal,
        "context": context,
        "forecast": forecast
    }


if __name__ == "__main__":
    news = """
    The European Central Bank signaled potential stimulus measures
    amid slowing economic growth across the eurozone.
    """

    result = run_full_pipeline(news)
    print(result)
