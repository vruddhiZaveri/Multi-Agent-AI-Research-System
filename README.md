# 🔍 Multi-Agent AI Research System

An AI-powered research assistant built using **LangChain**, **Google Gemini**, **Tavily Search API**, and **BeautifulSoup**. The system leverages a multi-agent architecture to automate web research, content extraction, report generation, and quality review.

---

## 📸 Project Preview

<p align="center">
  <img src="screenshots/homepage.jpeg" width="900">
</p>

---

## 🚀 Features

- 🔎 AI-Powered Web Research
- 🤖 Multi-Agent Architecture
- 🌐 Real-Time Web Search using Tavily
- 📄 Content Extraction with BeautifulSoup
- ✍️ Automated Research Report Generation
- 🧠 AI-Based Report Review & Critique
- 🎨 Streamlit User Interface
- ⚡ Modular & Scalable Design

---

## 🏗️ System Architecture

```text
User Query
    │
    ▼
┌─────────────────┐
│ Search Agent    │
│ (Tavily Search) │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Reader Agent    │
│ (BeautifulSoup) │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Writer Chain    │
│ (Gemini LLM)    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Critic Chain    │
│ (Review Agent)  │
└────────┬────────┘
         │
         ▼
     Final Report
```

---

## 🛠️ Tech Stack

### AI & LLM Frameworks

- LangChain
- Google Gemini API

### Search & Data Collection

- Tavily Search API
- BeautifulSoup4
- Requests

### Frontend

- Streamlit

### Backend

- Python

---

## 📂 Project Structure

```text
Multi-Agent-AI-Research-System/
│
├── screenshots/
│   └── homepage.jpeg
│
├── agents.py
├── tools.py
├── pipeline.py
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/vruddhiZaveri/Multi-Agent-AI-Research-System.git
cd Multi-Agent-AI-Research-System
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate Virtual Environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / Mac

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

### Gemini Configuration

```env
GOOGLE_API_KEY=your_google_api_key
```

### Tavily Configuration

```env
TAVILY_API_KEY=your_tavily_api_key
```

---

## ▶️ Running the Application

Launch the Streamlit application:

```bash
streamlit run app.py
```

Open your browser and navigate to:

```text
http://localhost:8501
```

---

## 💡 Example Workflow

### User Input

```text
Generative AI
```

### Processing Pipeline

1. Search Agent performs web research using Tavily Search.
2. Reader Agent extracts content from discovered URLs.
3. Writer Chain generates a structured research report.
4. Critic Chain reviews and improves the report.
5. Final report is displayed to the user.

---

## 🎯 Learning Outcomes

This project demonstrates:

- Agentic AI Systems
- Multi-Agent Architectures
- LangChain Framework
- Tool Calling
- Prompt Engineering
- Web Search Integration
- Web Scraping
- LLM Workflow Orchestration
- Research Automation

---

## 📈 Future Improvements

- Memory-Enabled Agents
- Agent Collaboration & Planning
- Research Citation Generation
- PDF Report Export
- Multi-Model Support
- RAG Integration with Vector Databases
- Cloud Deployment

---

## 👨‍💻 Author

### Vruddhi Zaveri

B.Tech in Artificial Intelligence & Machine Learning

- AI/ML Engineer
- GenAI Enthusiast
- Multi-Agent Systems Developer

GitHub: https://github.com/vruddhiZaveri

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!

It helps others discover the project and motivates further development.
