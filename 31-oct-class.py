import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import ConversationChain

load_dotenv()

#------------------------------------------------------------------
# Load API key and base URL from env variables
api_key = os.getenv("OPENROUTER_API_KEY")
base_url = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")

# Check if API key is missing
if not api_key:
    raise ValueError("OPENROUTER_API_KEY not found in .env file")

# Initializing the language model
llm = ChatOpenAI(
    model="mistralai/mistral-7b-instruct",
    temperature=0.4,
    max_tokens=256,
    api_key=api_key,
    base_url=base_url,
)

# Initializing conversation memory
memory = ConversationBufferMemory(return_messages=True)
conversation = ConversationChain(
    llm=llm,
    memory=memory
)

# Start chat session
print("\n=== Start chatting with the Agent ===")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() == "exit":
        print("\nConversation ended.")
        break
    try:
        res = conversation(user_input)
        print("Agent:", res['response'])
    except Exception as e:
        print("Error:", e)


import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
import litellm

# ---------------------------------------------------------------------
# 1. Load environment variables
# ---------------------------------------------------------------------
load_dotenv()
os.environ["OPENROUTER_API_KEY"] = os.getenv("OPENROUTER_API_KEY")

# ---------------------------------------------------------------------
# 2. Configure LiteLLM globally for OpenRouter
# ---------------------------------------------------------------------
litellm.api_key = os.getenv("OPENROUTER_API_KEY")
litellm.api_base = "https://openrouter.ai/api/v1"
model_name = "openrouter/mistralai/mistral-7b-instruct"

# ---------------------------------------------------------------------
# 3. Define Agents
# ---------------------------------------------------------------------
planner = Agent(
    role="Planner",
    goal="Create a structured 3-step plan with goals and deliverables.",
    backstory="A strategic AI project planner who designs clear blueprints.",
    allow_delegation=True,
    llm=model_name,
)

specialist = Agent(
    role="Specialist",
    goal="Execute the Planner’s 3-step plan and summarize the results clearly.",
    backstory="A detail-oriented AI engineer capable of executing complex plans.",
    llm=model_name,
)

# ---------------------------------------------------------------------
# 4. Define Tasks
# ---------------------------------------------------------------------
plan_task = Task(
    description="Given the topic, create a 3-step plan with goals and deliverables.",
    expected_output="A structured plan with 3 steps, each having a goal and deliverable.",
    agent=planner,
)

execute_task = Task(
    description="Take the Planner’s 3-step plan and write a short summary of what was achieved.",
    expected_output="A 3-point summary explaining the outcomes for each step.",
    agent=specialist,
)

# ---------------------------------------------------------------------
# 5. Create and Run the Crew
# ---------------------------------------------------------------------
crew = Crew(
    agents=[planner, specialist],
    tasks=[plan_task, execute_task],
    process=Process.sequential,
    verbose=True,
)

if __name__ == "__main__":
    topic = "Developing an AI-based document summarization system"
    print(f"\n--- Running CrewAI Planner–Specialist Workflow ---\nTopic: {topic}\n")
    result = crew.kickoff(inputs={"topic": topic})
    print("\n--- FINAL OUTPUT ---\n")
    print(result)