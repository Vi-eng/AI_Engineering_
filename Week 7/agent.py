# agent.py
from tools import weather_tool, currency_tool
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()

TOOLS = [weather_tool, currency_tool]

# 1. Set up the LLM
llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)

# 2. Create the LangGraph tool-calling agent (This fully replaces AgentExecutor!)
agent_executor = create_react_agent(llm, TOOLS)

# Main router function
def run_agent(user_input: str) -> str:
    try:
        # LangGraph expects inputs as a list of messages
        response = agent_executor.invoke({"messages": [("user", user_input)]})
        
        # The final answer is stored in the content of the very last message returned
        return response["messages"][-1].content
    except Exception as e:
        return f"An error occurred: {e}"