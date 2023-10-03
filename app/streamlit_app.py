import json

import streamlit as st
from dotenv import load_dotenv
from langchain.agents import AgentType, initialize_agent
from langchain.callbacks import StreamlitCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import MessagesPlaceholder
from langchain.tools import tool
from PIL import Image
from pydantic import BaseModel, Field

load_dotenv()

if "is_light_on" not in st.session_state:
    st.session_state.is_light_on = False


class ToggleLightInput(BaseModel):
    on: bool = Field(description="Whether to turn the light on or off")


@tool
def toggle_light(on):
    """toggle the light on or off"""
    st.session_state.is_light_on = on
    return json.dumps({"is_light_on": on})


def create_agent_chain():
    chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, streaming=True)

    agent_kwargs = {
        "extra_prompt_messages": [MessagesPlaceholder(variable_name="memory")],
    }
    memory = ConversationBufferMemory(memory_key="memory", return_messages=True)

    tools = [toggle_light]

    return initialize_agent(
        tools,
        chat,
        agent=AgentType.OPENAI_FUNCTIONS,
        agent_kwargs=agent_kwargs,
        memory=memory,
    )


if "agent_chain" not in st.session_state:
    st.session_state.agent_chain = create_agent_chain()


st.title("My AI Assistant")

for message in st.session_state.agent_chain.memory.chat_memory.messages:
    if message.type == "human":
        role = "user"
    else:
        role = "assistant"

    with st.chat_message(role):
        st.markdown(message.content)

prompt = st.chat_input("What is up?")

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        callback = StreamlitCallbackHandler(st.container())
        response = st.session_state.agent_chain.run(prompt, callbacks=[callback])
        st.markdown(response)

with st.sidebar:
    if st.session_state.is_light_on:
        image = "light-room.jpeg"
    else:
        image = "dark-room.jpeg"

    st.image(Image.open(f"assets/{image}"))
