# 🤖 Multi-Agent AI Research System

> An intelligent multi-agent research assistant built with **LangChain**, **Mistral AI**, **Tavily Search**, **BeautifulSoup**, and **Streamlit**.

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![LangChain](https://img.shields.io/badge/LangChain-Agent-green)
![Mistral](https://img.shields.io/badge/LLM-Mistral-orange)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

---

# 📖 Overview

The **Multi-Agent AI Research System** is an end-to-end research assistant that automates the complete research workflow using multiple AI agents.

Instead of relying on a single LLM response, the system divides the work among specialized agents:

- 🔎 Search Agent
- 📚 Reader Agent
- ✍️ Writer Agent
- 🧐 Critic Agent

Each agent has a dedicated responsibility, making the generated research reports significantly more accurate, structured, and reliable.

The application also includes an interactive **Streamlit UI**, allowing users to generate professional research reports from any topic with a single click.

# ✨ Features

- 🔎 Multi-Agent Architecture
- 🌐 Real-time Web Search using Tavily
- 📄 Intelligent Web Scraping using BeautifulSoup
- 🤖 Mistral AI Integration
- 📝 Professional Research Report Generation
- 🧐 Automated Report Quality Review
- 📊 Structured Markdown Reports
- 🎯 Source Citation
- 💻 Interactive Streamlit Dashboard
- ⚡ Fast and Lightweight
- 🔒 Environment Variable Support
- 📦 Easy Deployment

# 🏗️ System Architecture

```text
                   User
                     │
                     ▼
            Streamlit Interface
                     │
                     ▼
              Search Agent
          (Tavily Search Tool)
                     │
                     ▼
              Reader Agent
       (BeautifulSoup Scraper)
                     │
                     ▼
              Writer Chain
          (Research Generator)
                     │
                     ▼
              Critic Chain
        (Quality Assurance Agent)
                     │
                     ▼
           Final Research Report
```

# ⚙️ Workflow

### Step 1 — Search Agent

Searches the internet using Tavily and retrieves the most relevant information.

↓

### Step 2 — Reader Agent

Chooses the most relevant webpage and extracts clean text using BeautifulSoup.

↓

### Step 3 — Writer Agent

Generates a comprehensive research report using the collected information.

↓

### Step 4 — Critic Agent

Reviews the generated report for:

- Accuracy
- Completeness
- Hallucinations
- Missing Information
- Structure
- References

↓

### Final Output

A professional, structured research report with quality feedback.

### Install Dependencies

Install all required Python packages.

```bash
pip install -r requirements.txt
```

### Run the Streamlit Application

```bash
streamlit run app.py
```

# 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| LLM | Mistral AI |
| Framework | LangChain |
| Search Engine | Tavily API |
| Web Scraping | BeautifulSoup |
| HTTP Requests | Requests |
| UI | Streamlit |
| Prompt Engineering | LangChain Prompt Templates |
| Environment Variables | python-dotenv |
| Output Parsing | StrOutputParser |