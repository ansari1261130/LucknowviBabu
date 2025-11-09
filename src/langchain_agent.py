import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_huggingface import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate

# Paths
VECTOR_STORE_DIR = os.path.join("data", "vector_store")

# Initialize model and embeddings
model_name = "mistralai/Mistral-7B-Instruct-v0.2"  # multilingual reasoning model
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

# Load FAISS vector store
print("🔍 Loading FAISS vector store...")
db = FAISS.load_local(VECTOR_STORE_DIR, embeddings, allow_dangerous_deserialization=True)

retriever = db.as_retriever(search_kwargs={"k": 3})

# Hugging Face LLM endpoint (you can switch to OpenAI or Ollama if needed)
llm = HuggingFaceEndpoint(
    repo_id=model_name,
    temperature=0.5,
    max_new_tokens=256
)

# Define prompt template
prompt_template = """
You are LucknowviBabu — an AI chatbot fluent in Awadhi and English.
Answer the user's question using Awadhi context.

Context:
{context}

Question:
{question}

Answer in Awadhi (and briefly explain in English if necessary).
"""

prompt = PromptTemplate(
    input_variables=["context", "question"],
    template=prompt_template
)

# Create RAG Chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    chain_type_kwargs={"prompt": prompt}
)

def chat_with_awadhi_bot(question: str):
    response = qa_chain.invoke({"query": question})
    print("\n💬 LucknowviBabu says:\n")
    print(response["result"])

if __name__ == "__main__":
    while True:
        query = input("\n🗣️ You: ")
        if query.lower() in ["exit", "quit"]:
            print("👋 Bye! LucknowviBabu signing off...")
            break
        chat_with_awadhi_bot(query)
