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
    print(json.dumps(forecast, indent=2))
