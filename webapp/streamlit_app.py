import streamlit as st
from dotenv import load_dotenv
from langchain.agents import AgentType, initialize_agent
from langchain.callbacks import StreamlitCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import MessagesPlaceholder
from PIL import Image

from customtools import ToggleStreamlitLightTool, ToogleRemoteLightTool

load_dotenv()


# エージェントを作成する関数
def create_agent_chain():
    chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, streaming=True)

    agent_kwargs = {
        "extra_prompt_messages": [MessagesPlaceholder(variable_name="memory")],
    }
    memory = ConversationBufferMemory(memory_key="memory", return_messages=True)

    tools = [
        # ToggleStreamlitLightTool(),
        ToogleRemoteLightTool(room_id="myroom"),
    ]

    return initialize_agent(
        tools,
        chat,
        agent=AgentType.OPENAI_FUNCTIONS,
        agent_kwargs=agent_kwargs,
        memory=memory,
    )


# Streamlitのセッションに保存されるデータ
if "is_light_on" not in st.session_state:
    st.session_state.is_light_on = False

if "agent_chain" not in st.session_state:
    st.session_state.agent_chain = create_agent_chain()

agent_chain = st.session_state.agent_chain

# タイトルを表示
st.title("My AI Assistant")

# チャット履歴を表示
for message in agent_chain.memory.chat_memory.messages:
    if message.type == "human":
        role = "user"
    else:
        role = "assistant"

    with st.chat_message(role):
        st.markdown(message.content)

# 入力を受け付け
prompt = st.chat_input("What is up?")

# 入力があった場合、エージェントを実行
if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        callback = StreamlitCallbackHandler(st.container())
        response = agent_chain.run(prompt, callbacks=[callback])
        st.markdown(response)

# サイドバーに画像を表示
with st.sidebar:
    if st.session_state.is_light_on:
        image = "light-room.jpeg"
    else:
        image = "dark-room.jpeg"

    st.image(Image.open(f"assets/{image}"))
