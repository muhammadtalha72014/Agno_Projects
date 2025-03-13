import os
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools

os.environ["GROQ_API_KEY"] = "Enter your API key"

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGoTools()],
    markdown=True
)
agent.print_response("Give me latest news about agentic AI?", stream=True)