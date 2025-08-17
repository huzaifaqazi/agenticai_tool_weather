from agents import AsyncOpenAI,OpenAIChatCompletionsModel,RunConfig
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("gemini_api_keys")

provider = AsyncOpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client=provider
)

config = RunConfig(
    model = model,
    model_provider=provider,
    tracing_disabled=True
)
