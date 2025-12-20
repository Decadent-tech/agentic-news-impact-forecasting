import json
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

load_dotenv()


def run_context_retrieval(event_json: dict, prompt_text: str) -> dict:
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",  # safe MVP choice
        temperature=0
    )

    prompt = PromptTemplate(
        template=prompt_text,
        input_variables=["event_json"]
    )

    # Format the JSON as string to pass into the prompt
    event_str = json.dumps(event_json, indent=2)

    response = llm.invoke(prompt.format(event_json=event_str))

    raw = response.content.strip()
    if not raw:
        raise ValueError(
            "Empty response from LLM. Check API key or prompt formatting."
        )

    return json.loads(raw)


if __name__ == "__main__":
    # Sample input from Signal Extraction Agent
    sample_event = {
        "event_summary": "The European Central Bank (ECB) is expected to announce a new stimulus package to support the economy amid the ongoing pandemic.",
        "domain": "macroeconomics",
        "key_actors": ["European Central Bank"],
        "geographic_scope": "Europe",
        "time_horizon": "short_term",
        "urgency": "high"
    }

    with open("../prompts/context_prompt.md", "r") as f:
        context_prompt = f.read()

    context_output = run_context_retrieval(sample_event, context_prompt)
    print(json.dumps(context_output, indent=2))
