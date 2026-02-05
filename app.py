# Insurance Claims Chatbot

An AI-powered insurance claims chatbot designed to simplify and accelerate the insurance claim submission process by using compressed policy documents and historical claim data.

## 🚀 Project Overview
Insurance claim processing often involves long policy documents and complex rules. This chatbot reduces processing time and cost by compressing insurance policies and claim histories into structured summaries, enabling faster and more accurate responses from AI models.

## 🎯 Key Features
- Interactive chatbot for insurance claim submission
- Compressed policy document understanding
- Claim eligibility validation
- Claim approval probability estimation
- Faster responses with reduced token usage

## 🧠 How Compression Works
Instead of sending full insurance policy documents to the AI model, this project:
- Extracts only essential coverage rules
- Summarizes exclusions and limits
- Compresses historical claims into approval patterns

This reduces input size, improves accuracy, and lowers processing costs.

## 🛠️ Tech Stack
- Python
- Large Language Model (LLM API)
- JSON / Text-based data storage

## 📂 Project Structure
insurance-claims-chatbot/
│
├── app.py
├── README.md
├── .gitignore
├── LICENSE
└── docs/
    ├── architecture.md
    ├── compression.md
    └── workflow.md
## ▶️ How to Run
1. Clone the repository
2. Install required Python packages
3. Run `python app.py`
4. Interact with the chatbot via terminal

## 💡 Creative Feature
The chatbot generates a **Claim Eligibility Score** based on historical claim patterns, helping users understand the likelihood of claim approval before submitting a claim.

## 📌 Learnings
- Built a real-world insurance chatbot use case
- Learned context compression for efficient AI systems
- Improved understanding of cost-efficient LLM usage
