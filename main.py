import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationTokenBufferMemory
from langchain.memory import ConversationBufferMemory
from langchain.memory import ConversationSummaryMemory
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationChain
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

# 🔐 Load environment variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# 🤖 Initialize Groq LLM
llm = ChatGroq(
    model_name="meta-llama/llama-4-scout-17b-16e-instruct",
    groq_api_key=groq_api_key
)

# 🧠 Define prompt template (outside condition to avoid NameError)
prompt = PromptTemplate(
    input_variables=["history", "input"],
    template="""
You are a helpful and concise assistant. Always answer briefly in one paragraph only.

Chat History:
{history}

User: {input}
AI:"""
)

# 🧠 Initialize memory in session state
memory_type = st.selectbox("Choose Memory Type", ["BufferWindow", "TokenBuffer", "Summary", "BufferMemory"])


if memory_type == "BufferWindow":
    memory = ConversationBufferWindowMemory(k=3, return_messages=True)
elif memory_type == "TokenBuffer":
    memory = ConversationTokenBufferMemory(llm=llm, max_token_limit=100)
elif memory_type == "Summary":
    memory = ConversationSummaryMemory(llm=llm, memory_key="chat_history", return_messages=True)
elif memory_type == "BufferMemory":
    memory = ConversationBufferMemory(return_messages=True)

# 🔗 Create ConversationChain
conversation = ConversationChain(
    llm=llm,
    prompt=prompt,
    memory=memory,
    verbose=False
    )

# 🌐 Streamlit UI
st.title("💬 Chat with Groq LLM - With Memory")

# 📝 Input & Output UI
user_input = st.text_input("Ask something:")
if st.button("Send") and user_input.strip():
    response = conversation.predict(input=user_input)
    st.markdown(f"**You:** {user_input}")
    st.markdown(f"**AI:** {response}")