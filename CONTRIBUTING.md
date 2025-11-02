# Contributing to LucknowviBabu 🕊️
> "Ek chatbot, Lucknow ke andaaz mein!"  

We’re building **LucknowviBabu**, a generative AI chatbot that understands and translates the Awadhi language.  
If you’d like to contribute, follow these guidelines to keep the repo clean and consistent.

---

## 🧩 1. Setting up the project locally
1. Clone the repository:
   ```bash
   git clone https://github.com/ansari1261130/LucknowviBabu.git
   cd LucknowviBabu
Create a virtual environment and install dependencies:

python -m venv .venv
.venv\Scripts\activate       # Windows
# or source .venv/bin/activate (Linux/Mac)
pip install -r requirements.txt


Verify everything runs:

python src/app.py

🌱 2. Branch naming convention

Use descriptive branch names:

Purpose	Example
New feature	feature/langchain-integration
Bug fix	fix/vector-store-bug
Docs update	docs/readme-update
Experiment	exp/translation-model-v1
🧠 3. Workflow (Git branching)

Always pull the latest main branch:

git checkout main
git pull origin main


Create a new branch:

git checkout -b feature/your-feature-name


Make your changes and commit:

git add .
git commit -m "Added LangChain retrieval agent"


Push your branch:

git push origin feature/your-feature-name


Create a Pull Request (PR) on GitHub → main.

🔍 4. Code style

Follow PEP8:

Use meaningful variable names.

Keep line length ≤ 100 characters.

Add comments to explain complex logic.

🧪 5. Testing your code

Before pushing:

Run your script in .venv to ensure dependencies are correct.

If you modify any training or inference logic, test using a small text sample.

📦 6. Folder structure reference
LucknowviBabu/
├── data/                  # Training and evaluation data
├── experiments/           # Logs, checkpoints
├── notebooks/             # Jupyter notebooks
├── src/                   # Python source code
├── README.md
├── requirements.txt
├── CONTRIBUTING.md
└── .gitignore

🧑‍🤝‍🧑 7. Contributors
Name	Role	GitHub
Mohd Azam Ansari	Project Lead	@ansari1261130

Your Teammate	Co-Developer	—
💬 8. Contact

If you face any issues or want to discuss improvements, open an Issue

or reach out via GitHub Discussions.

Shukriya! 🙏
Let’s make Awadhi go global! 🌍


---