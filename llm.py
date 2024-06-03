from llama_index.llms.groq import Groq
from global_settings import GROQ_API_KEY


def get_model(model_name: str = "llama3-8b-8192"):
    return Groq(model=model_name, api_key=GROQ_API_KEY)


if __name__ == "__main__":
    llm = get_model()
    print(llm.complete("Who are you?"))
