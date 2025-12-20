from agents.signal_extractor import run_signal_extraction
from agents.context_retriever import run_context_retrieval


news_text = """
    The U.S. Federal Reserve indicated that it may begin cutting interest rates
    later this year as inflation shows signs of easing, according to statements
    released after the latest policy meeting.
    """
with open("../prompts/signal_prompt.md", "r") as f:
        signal_prompt = f.read()

signal = run_signal_extraction(prompt_text=signal_prompt, news_text=news_text)
with open("../prompts/context_prompt.md", "r") as f:
        context_prompt = f.read()
context = run_context_retrieval(signal, context_prompt)
print(context)