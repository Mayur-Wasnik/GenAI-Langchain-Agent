from dotenv import load_dotenv
load_dotenv()

from langchain_core.tools import Tool
from langchain_groq import ChatGroq
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain.agents import create_agent
from groq import BadRequestError
from langgraph.checkpoint.memory import MemorySaver
import streamlit as st

model = ChatGroq(model="llama-3.1-8b-instant", streaming=True)
search = GoogleSerperAPIWrapper()

# Properly define the search tool with schema
search_tool = Tool(
    name="google_search",
    func=search.run,
    description="Search Google for information about a query. Returns search results."
)
tools = [search_tool]
memory = MemorySaver()

if "memory" not in st.session_state:
    st.session_state.memory = MemorySaver()
    st.session_state.history = []

agent = create_agent(
    model=model,
    tools=tools,
    system_prompt="You are a agent and can search for any question on google. Answer the question based on the search results and if you don't know the answer, say you don't know.",
    checkpointer=MemorySaver()
)

st.subheader("QuikAnswer - Answer your questions in a flash! ⚡")

for message in st.session_state.history:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)

query = st.chat_input("Ask me anything! (Type 'quit' to exit)")
if query:
    st.chat_message("user").markdown(query)
    st.session_state.history.append({"role": "user", "content": query})

    response = agent.stream(
        {"messages":[{"role": "user", "content": query}]},
        {"configurable": {"thread_id": "1"}},
        stream_mode="messages"
    )

    ai_container = st.chat_message("ai")
    with ai_container:
        space = st.empty()

        message = ""

        for chunk in response:
            message = message + chunk[0].content
            space.write(message)
    st.session_state.history.append({"role": "ai", "content": message})