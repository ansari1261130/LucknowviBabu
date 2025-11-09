import os
import streamlit as st
from langchain_classic.chains.retrieval_qa.base import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEndpoint

from langchain_core.prompts import PromptTemplate

# Paths
VECTOR_STORE_DIR = os.path.join("data", "vector_store")

# Streamlit Page Config
st.set_page_config(page_title="LucknowviBabu 🕌", page_icon="🕌", layout="wide")

# Title and Header
st.title("🕌 LucknowviBabu — The Awadhi Chatbot")
st.caption("**Speak in any language, and I’ll reply in *Awadhi with style!* 💬**")

# Sidebar Controls
with st.sidebar:
    st.header("⚙️ Settings")
    temperature = st.slider("Creativity (temperature)", 0.0, 1.0, 0.5)
    top_k = st.slider("Knowledge Depth (k)", 1, 5, 3)
    st.markdown("---")
    if st.button("🧹 Clear Chat History"):
        st.session_state["chat_history"] = []
        st.success("Chat history cleared!")

# Cache FAISS vector store
@st.cache_resource
def load_vector_store(k):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
    db = FAISS.load_local(VECTOR_STORE_DIR, embeddings, allow_dangerous_deserialization=True)
    return db.as_retriever(search_kwargs={"k": k})

retriever = load_vector_store(top_k)

# Initialize LLM
llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    temperature=temperature,
    max_new_tokens=256
)

# Prompt Template
prompt_template = """
You are LucknowviBabu — an AI chatbot fluent in Awadhi and English.
You live in Lucknow and speak politely with cultural warmth.
Use the given context and chat history to respond naturally.

Context:
{context}

Chat history:
{chat_history}

User question:
{question}

Reply in Awadhi (and add a short English explanation if helpful).
"""

prompt = PromptTemplate(
    input_variables=["context", "question", "chat_history"],
    template=prompt_template
)

# Build QA Chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    chain_type_kwargs={"prompt": prompt}
)

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Chat Input Box
user_input = st.chat_input("💬 Type your message here...")

# Process input when user sends message
if user_input:
    history_text = "\n".join([f"User: {u}\nBot: {b}" for u, b in st.session_state["chat_history"]])
    with st.spinner("Thinking in Awadhi... 🧠"):
        response = qa_chain.invoke({"query": user_input, "chat_history": history_text})
        bot_reply = response["result"]

    # Store conversation
    st.session_state["chat_history"].append((user_input, bot_reply))

# Display chat history
for user_msg, bot_msg in st.session_state["chat_history"]:
    with st.chat_message("user"):
        st.markdown(f"**You:** {user_msg}")
    with st.chat_message("assistant"):
        st.markdown(f"🕌 **LucknowviBabu:** {bot_msg}")
