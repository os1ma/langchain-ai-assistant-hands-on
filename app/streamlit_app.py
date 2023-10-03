import streamlit as st
from dotenv import load_dotenv
from langchain.agents import AgentType, initialize_agent
from langchain.callbacks import StreamlitCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import MessagesPlaceholder
from langchain.tools import Tool
from PIL import Image

load_dotenv()

if "is_light_on" not in st.session_state:
    st.session_state.is_light_on = False


def turn_on_light(param):
    st.session_state.is_light_on = True
    return "Success"


def turn_off_light(param):
    st.session_state.is_light_on = False
    return "Success"


tools = [
    Tool.from_function(
        func=turn_on_light,
        name="turn_on_light",
        description="Turn on the light",
    ),
    Tool.from_function(
        func=turn_off_light,
        name="turn_off_light",
        description="Turn off the light",
    ),
]


def create_agent_chain():
    chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, streaming=True)

    agent_kwargs = {
        "extra_prompt_messages": [MessagesPlaceholder(variable_name="memory")],
    }
    memory = ConversationBufferMemory(memory_key="memory", return_messages=True)

    return initialize_agent(
        tools,
        chat,
        agent=AgentType.OPENAI_FUNCTIONS,
        agent_kwargs=agent_kwargs,
        memory=memory,
    )


if "agent_chain" not in st.session_state:
    st.session_state.agent_chain = create_agent_chain()


st.title("langchain-streamlit-app")

for message in st.session_state.agent_chain.memory.chat_memory.messages:
    if message.type == "human":
        role = "user"
    else:
        role = "assistant"

    with st.chat_message(role):
        st.markdown(message["content"])

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
