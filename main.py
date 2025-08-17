from agents import Agent,Runner , ModelSettings
from config import config
from Tools.weather import get_weather
import chainlit as cl

agent = Agent(
    name="Weather-Agent",
    instructions="You are helpfull assistant that answer user's Quiries of your best ability.provide accurate information. And You also use Tool to get the information about weather forcast any city.",
    tools=[get_weather],
)

@cl.on_chat_start
async def on_chat_start():
    cl.user_session.set("history" , [])
    await cl.Message(content="Welcome to the Weather Agent! You can ask about the weather in any city.").send()


@cl.on_message
async def main(msg: cl.Message):
    history = cl.user_session.get("history")
    history.append({"role": "user" , "content" : msg.content})

    result = Runner.run_sync(
    agent,
    input=history,
    run_config=config
)
    await cl.Message(content=result.final_output).send()
    history.append({"role": "assistant", "content": result.final_output})
    cl.user_session.set("history", history)
    # print(result.final_output)


