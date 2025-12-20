import json
import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

load_dotenv()


def run_signal_extraction(news_text: str, prompt_text: str) -> dict:
    '''llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )'''
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)


    prompt = PromptTemplate(
        template=prompt_text,
        input_variables=["news_text"]
    )

    response = llm.invoke(
        prompt.format(news_text=news_text)
    )
    raw = response.content.strip()
    if not raw:
        raise ValueError("Empty response from LLM. Check API key or model name.")
    return json.loads(raw)



if __name__ == "__main__":
    sample_news = """
    The U.S. Federal Reserve indicated that it may begin cutting interest rates
    later this year as inflation shows signs of easing, according to statements
    released after the latest policy meeting.
    """

    with open("../prompts/signal_prompt.md", "r") as f:
        signal_prompt = f.read()

    result = run_signal_extraction(sample_news, signal_prompt)
    print(json.dumps(result, indent=2))
