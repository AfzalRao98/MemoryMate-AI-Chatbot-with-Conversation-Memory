# 🧠 MemoryMate - AI Chatbot with Conversational Memory

MemoryMate is a smart chatbot application built using **LangChain**, **Streamlit**, and **Groq LLMs**. It supports persistent conversation using advanced memory techniques like:

- 📚 ConversationBufferMemory
- 💬 ConversationTokenBufferMemory
- 🧠 ConversationSummaryMemory
- 💬 ConversationWindowBufferMemory

This ensures the chatbot remembers past messages, improving relevance and continuity — just like a real conversation.

---

## 🚀 Features

- 🗣️ Real-time conversation with chat history
- 🧠 Built-in memory options to keep track of previous messages
- 🔄 Memory-powered context retention for personalized replies
- 🧼 Simple and intuitive UI built with Streamlit

---

## 📦 Memory Types Explained

| Memory Type | Behavior | Use Case |
|-------------|----------|----------|
| `ConversationBufferMemory` | Stores full chat history | Ideal for short sessions |
| `ConversationTokenBufferMemory` | Stores recent context within token limit | Efficient for LLM token constraints |
| `ConversationSummaryMemory` | Summarizes past conversation | Best for long sessions with limited memory usage |

---



