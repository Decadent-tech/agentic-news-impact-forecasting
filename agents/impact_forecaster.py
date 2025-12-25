
import json
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

load_dotenv()


def run_impact_forecast(signal: dict, context: dict, prompt_text: str) -> dict:
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0
    )

    prompt = PromptTemplate(
        template=prompt_text,
        input_variables=["signal_json", "context_json"]
    )

    signal_str = json.dumps(signal, indent=2)
    context_str = json.dumps(context, indent=2)

    response = llm.invoke(
        prompt.format(
            signal_json=signal_str,
            context_json=context_str
        )
    )

    raw = response.content.strip()
    if not raw:
        raise ValueError("Empty response from Impact Forecasting Agent")

    return json.loads(raw)

ALLOWED_DOMAINS = {"policy", "markets", "economy", "industry", "society"}

def sanitize_forecast(forecast: dict) -> dict:
    domains = forecast.get("impact_domains", [])
    cleaned = [d for d in domains if d in ALLOWED_DOMAINS]

    # If model hallucinated domains → downgrade impact
    if len(cleaned) < len(domains):
        forecast["impact_domains"] = cleaned
        forecast["predicted_impact"] = "low"
        forecast["confidence_score"] = min(
            forecast.get("confidence_score", 0.5), 0.5
        )
        forecast.setdefault("risk_factors", [])
        forecast["risk_factors"].append(
        "Model attempted to introduce unsupported impact domains"
        )

    return forecast

def validate_rationale(signal: dict, forecast: dict) -> dict:
    forbidden_terms = [
        "consumer spending",
        "demand",
        "economic slowdown",
        "economic growth",
        "recession",
        "inflation",
        "supply chain",
        "natural disaster",
        "pandemic",
        "war"
    ]

    rationale = forecast.get("rationale", "").lower()

    for term in forbidden_terms:
        if term in rationale:
            forecast["predicted_impact"] = "low"
            forecast["impact_domains"] = []
            forecast["confidence_score"] = min(
                forecast.get("confidence_score", 0.5), 0.3
            )
            forecast.setdefault("risk_factors", [])
            forecast["risk_factors"].append(
                f"Unjustified causal inference introduced: {term}"
            )
            forecast["rationale"] = (
                "Insufficient information in signal or context to justify "
                "specific downstream economic mechanisms."
            )
            break

    return forecast




if __name__ == "__main__":
    sample_signal = {
        "event_summary": "ECB expected to announce stimulus",
        "domain": "macroeconomics",
        "key_actors": ["European Central Bank"],
        "geographic_scope": "Europe",
        "time_horizon": "short_term",
        "urgency": "high"
    }

    sample_context = {
        "historical_analogs": ["2008 financial crisis"],
        "background_context": "Economic slowdown impacting markets",
        "notes": "Inflation trends remain uncertain"
    }

    with open("../prompts/forecast_prompt.md") as f:
        forecast_prompt = f.read()
    
    
    forecast = run_impact_forecast(sample_signal, sample_context, forecast_prompt)

    forecast = sanitize_forecast(forecast)
    forecast = validate_rationale(sample_signal, forecast)

    print(json.dumps(forecast, indent=2))
