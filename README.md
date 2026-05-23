# 🎓 SkillWiz AI Learning Agent

> AI-powered learning assistant that helps students decide what to study next — built for the SkillWiz AI Agent Development Assignment.

---

## 📌 Overview

The SkillWiz AI Agent is a conversational learning coach that:
- Fetches a student's progress from a **SQLite database**
- Understands their current learning phase and pending topics
- Suggests a **meaningful, context-aware next step**
- Remembers conversation context across turns (memory)

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| LLM | Claude Sonnet (Anthropic) via `langchain-anthropic` |
| Agent Framework | LangChain (CHAT_CONVERSATIONAL_REACT) |
| Database | SQLite (auto-created, no setup needed) |
| Memory | `ConversationBufferMemory` |
| Language | Python 3.10+ |

---

## 📁 Project Structure

```
skillwiz-agent/
├── agent.py            # Main agent + entry point
├── tools.py            # Custom LangChain tools
├── database.py         # SQLite setup & helpers
├── students.db         # Auto-generated on first run
├── requirements.txt    # Dependencies
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/lavishsaini136-rgb/skillwiz-agent.git
cd skillwiz-agent
```

### 2. Create & activate virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set your Anthropic API key
```bash
export ANTHROPIC_API_KEY=sk-ant-...   # Windows: set ANTHROPIC_API_KEY=sk-ant-...
```

### 5. Run the agent
```bash
python agent.py
```

> The SQLite database (`students.db`) is created and seeded **automatically** on first run. No extra setup needed.

---

## 🤖 Tools Implemented

### `fetch_student_progress`
Queries the SQLite database and returns the student's full learning record — goal, current phase, completed topics, pending topics, and streak.

### `suggest_next_topic`
Applies branching logic to recommend the right next action:
- ✅ All topics done → suggest a project challenge
- 📈 70%+ done → suggest mini-project + next topic
- 📚 In progress → suggest the next pending topic with streak motivation

---

## 💬 Sample Interaction

```
You: What should I do today?

SkillWiz: Great work keeping your 5-day streak alive! Today I'd recommend
diving into Promises — it's the foundation for all asynchronous JavaScript.
Try building a small fetch-based app once you're comfortable with the syntax.
You're 33% through JavaScript Basics. Keep going!

You: I already finished Promises last night.

SkillWiz: That's fantastic progress! Since you've knocked out Promises, your
next focus should be Async/Await — it's essentially syntactic sugar on top
of Promises, so the concepts will feel very natural. Aim for 45 minutes
today and you'll be well on your way.
```

---

## 📦 requirements.txt

```
langchain>=0.2.0
langchain-anthropic>=0.1.0
anthropic>=0.28.0
```

---

## 👤 Author

**Lavish Saini**  
B.Tech Student | Aspiring AI/ML Engineer  
[LinkedIn](https://linkedin.com/in/lavish-saini-1a5997382) • [GitHub](https://github.com/lavishsaini136-rgb)
