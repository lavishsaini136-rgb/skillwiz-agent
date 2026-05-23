import os
from langchain_anthropic import ChatAnthropic
from langchain.agents import initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory
from database import init_db
from tools import fetch_student_progress, suggest_next_topic

# ── Setup ────────────────────────────────────────────────────────────────────
init_db()

llm = ChatAnthropic(
    model="claude-sonnet-4-20250514",
    anthropic_api_key=os.environ["ANTHROPIC_API_KEY"],
    temperature=0.3,
)

tools = [fetch_student_progress, suggest_next_topic]

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True,
)

SYSTEM_PROMPT = """You are SkillWiz, a friendly and motivating AI learning coach.
You have access to a student's learning database through your tools.
Always fetch the student's progress before making suggestions.
Give specific, encouraging advice tailored to their exact situation.
Be concise but warm. The default student ID is 'user_123'."""

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,
    verbose=True,
    agent_kwargs={"system_message": SYSTEM_PROMPT},
)

# ── Main loop ────────────────────────────────────────────────────────────────
def chat(user_input: str) -> str:
    return agent.run(user_input)

if __name__ == "__main__":
    print("SkillWiz Agent ready. Type 'quit' to exit.\n")
    while True:
        query = input("You: ").strip()
        if query.lower() in ("quit", "exit"):
            break
        if not query:
            continue
        response = chat(query)
        print(f"\nSkillWiz: {response}\n")
