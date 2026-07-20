
from google.adk.agents.llm_agent import Agent
import datetime

# mock tool implementation
def get_current_time(city: str) -> dict:
    return {
        "Status": "Success",
        "City": city,
        "Time": datetime.date.today().ctime()
    }

root_agent = Agent(
    name = 'agent',
    model = 'gemini-flash-latest',
    description = 'Give answer of a question.',
    instruction = "You are a helpful assistant that gives relevant answer of a question. You can Google search.",
    tools = [get_current_time],
)
