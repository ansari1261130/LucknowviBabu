# 🕌 LucknowwiBabu – The Awadhi Language Chatbot

**LucknowwiBabu** is a Generative AI-powered chatbot designed to understand, translate, and communicate in the **Awadhi language** — a classical dialect of Lucknow and Awadh region.  
This project aims to preserve the linguistic heritage of Awadhi by developing an intelligent model capable of translating words and phrases *to and from* Awadhi, irrespective of the input language.

---

## 🧠 Project Overview

The **Awadhi Language Chatbot** is a research-oriented project built using **LangChain**, **PyTorch**, and **Generative AI** frameworks.  
It focuses on:
- Data collection from Awadhi literature and text sources  
- Preprocessing and annotation of Awadhi–English parallel corpora  
- Training and fine-tuning transformer models for Awadhi translation  
- Creating a LangChain-based conversational agent for interactive responses  

This project contributes toward low-resource language preservation and provides a foundational model for Awadhi NLP applications.

---

## ⚙️ Tech Stack

| Category | Technologies Used |
|-----------|-------------------|
| **Programming Language** | Python 3.13 |
| **AI / ML Frameworks** | PyTorch, LangChain |
| **NLP Libraries** | Hugging Face Transformers, SentencePiece, spaCy |
| **Vector Database** | FAISS |
| **Development Tools** | Jupyter Notebook, VS Code / PyCharm |
| **Version Control** | Git & GitHub |

---

## 📁 Folder Structure

LucknowwiBabu/

├── data/

│ ├── awadhi_pages/ # Original Awadhi text corpus

│ │ └── raw/ # Raw, unprocessed Awadhi text files
│ └── parallel_pairs.csv # Awadhi–English sentence pairs
│
├── experiments/
│ └── logs/ # Model training and evaluation logs
│
├── notebooks/
│ ├── EDA_dataset.ipynb # Exploratory Data Analysis on corpus
│ └── Annotation_tool.ipynb # Manual labeling and cleaning notebook
│
├── src/
│ ├── init.py
│ ├── app.py # Main chatbot interface
│ ├── preprocess.py # Text cleaning and normalization
│ ├── build_vector_store.py # Vector embeddings creation (FAISS)
│ ├── langchain_agent.py # LangChain conversational logic
│ ├── train.py # Model training and fine-tuning
│ └── model_utils.py # Utility functions for model handling
│
├── requirements.txt # Dependencies list
└── README.md # Project documentation

---

## 🧩 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/LucknowwiBabu.git
cd LucknowwiBabu

2️⃣ Create a Virtual Environment
python -m venv venv
source venv/bin/activate        # for macOS/Linux
venv\Scripts\activate           # for Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Prepare Data

Place your Awadhi text pages and annotated pairs inside the data/ folder:

data/
├── awadhi_pages/raw/
└── parallel_pairs.csv

5️⃣ Run Preprocessing
python src/preprocess.py

6️⃣ Train the Model
python src/train.py

7️⃣ Build Vector Store
python src/build_vector_store.py

8️⃣ Launch Chatbot
python src/app.py

💬 Example Interaction

User: Translate “How are you?” into Awadhi.

LucknowwiBabu: “तू का हाल बा?” 😄

User: Translate “मोरा नाव रामु है” into English.

LucknowwiBabu: “My name is Ramu.”

🧪 Research Goals

Build a bilingual Awadhi–English corpus for machine translation.

Train transformer-based translation and language understanding models.

Evaluate accuracy and fluency of Awadhi generation.

Deploy an interactive LangChain-based chatbot for real-world use.

🧍‍♂️ Author

Mohd Azam Ansari
B.Tech – Computer Science and Engineering
GitHub
 | LinkedIn

📜 License

This project is released under the MIT License.
You are free to use, modify, and distribute it for academic and research purposes.

🌟 Acknowledgments

Special thanks to:

The people of Lucknow and Awadh for preserving the beauty of Awadhi.

Open-source contributors in NLP and low-resource language research.

The LangChain and PyTorch communities.

"Babu kahe ke kahat hain hum Lucknow ke log, par bhasha mein hai pyaar aur tehzeeb dono!"
