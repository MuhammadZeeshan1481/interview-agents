# Job Interview Agent System
An AI-driven multi-agent system that helps simulate and evaluate technical job interviews.

## Features
🔹 Auto-generates technical interview questions

🔹 Simulates realistic candidate answers

🔹 Evaluates responses with constructive feedback

## Tech Stack
Python

Streamlit – Interactive frontend

Hugging Face Hub – LLMs (e.g. Zephyr, Mixtral)

dotenv – API key management

## Project Structure
pgsql
Copy
Edit
job-interview-agents/
├── agents/                  # Question Generator, Candidate, Evaluator
├── utils/                   # HuggingFace LLM wrapper
├── ui/                      # Streamlit frontend
├── main.py                  # Orchestrates agent flow
├── .env                     # HF API key + model name
├── requirements.txt
└── README.md
🧪 Run Locally
bash
Copy
Edit
git clone https://github.com/your-username/job-interview-agents.git
cd job-interview-agents

# Create .env file
echo "HUGGINGFACEHUB_API_TOKEN=your_key_here" > .env
echo "HF_MODEL=HuggingFaceH4/zephyr-7b-beta" >> .env

# Install dependencies
pip install -r requirements.txt

# Launch the app
streamlit run ui/app.py
## Notes
Works with free-tier Hugging Face models

No OpenAI key needed

Modular design – easy to extend for other roles or tasks
# AI-Powered Job Interview Agents

A multi-agent AI system to simulate job interviews:
- 🧠 Generates intelligent questions
- 🤖 Simulates candidate answers
- 📋 Evaluates with helpful feedback

## Tech Stack
- Python
- Streamlit
- Hugging Face (LLM)
- dotenv

## Run Locally

```bash
pip install -r requirements.txt
streamlit run ui/app.py

