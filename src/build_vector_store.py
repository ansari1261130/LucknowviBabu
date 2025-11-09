import os
import pandas as pd
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Paths
CLEANED_DATA_PATH = os.path.join("data", "cleaned_awadhi.csv")
VECTOR_STORE_DIR = os.path.join("data", "vector_store")

def build_vector_store():
    if not os.path.exists(CLEANED_DATA_PATH):
        print("❌ Cleaned data not found. Run preprocess.py first.")
        return

    df = pd.read_csv(CLEANED_DATA_PATH)
    texts = df["cleaned_text"].tolist()

    print("✅ Data loaded. Creating embeddings...")

    # Create embedding model
    model_name = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    embeddings = HuggingFaceEmbeddings(model_name=model_name)

    # Create FAISS index
    vector_store = FAISS.from_texts(texts, embedding=embeddings)

    # Save the vector store
    os.makedirs(VECTOR_STORE_DIR, exist_ok=True)
    vector_store.save_local(VECTOR_STORE_DIR)

    print(f"✅ Vector store saved successfully at {VECTOR_STORE_DIR}")

if __name__ == "__main__":
    build_vector_store()
