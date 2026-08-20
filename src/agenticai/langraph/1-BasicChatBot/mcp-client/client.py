from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()

import asyncio

import os
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

async def main():
    client = MultiServerMCPClient(
        {
            "math":{
                "command":"python",
                "args":[r"C:\Users\Hp\Downloads\Study_and_Practice\Python\AgenticAI\src\agenticai\langraph\1-BasicChatBot\mcp-server\math_server.py"], # Ensure correct absolute path
                "transport": "stdio"
            },
            "weather":{
                "url": "http://localhost:8000/mcp", # Ensure server is running here
                "transport": "streamable-http"
            }
        }
    )

    tools = await client.get_tools()
    model = ChatGroq(model = "qwen/qwen3.6-27b")
    agent = create_agent(
        model,tools
    )

    math_response = await agent.ainvoke(
        {
            "messages": [{"role": "user", "content": "what's (3+5) x 12"}]
        }
    )

    print("Math Resonse:", math_response['messages'][-1].content)

    weather_response = await agent.ainvoke(
            {
                "messages": [{"role": "user", "content": "what's weather in New yark"}]
            }
        )
    
    print("WEather Resonse:", weather_response['messages'][-1].content)


asyncio.run(main())