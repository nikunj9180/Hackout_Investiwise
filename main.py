import os
# os.environ["SERPER_API_KEY"] = "67a1a431e0ce8b7c9b7f378c3992b424e8373607"

os.environ['OPENAI_API_KEY'] = "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"
os.environ["SERPAPI_API_KEY"] = "9d04b6ea744f7a1257da76a94a2231b01a0e0080074f5e9a9d17e1ab2267c9ce"
import openai
# from langchain.utilities import GoogleSerperAPIWrapper
from langchain.llms.openai import OpenAI
from langchain.chat_models import ChatOpenAI

from langchain.agents import initialize_agent
from langchain.agents import load_tools

# llm = OpenAI(temperature=0.5)
llm = ChatOpenAI(
    temperature = 0,
    model_name = 'gpt-3.5-turbo'
)
# search = GoogleSerperAPIWrapper()
# tools = [
#     Tool(
#         name="Intermediate Answer",
#         func=search.run,
#         description="useful for when you need to ask with search"
#     )
# ]
tools = load_tools(["serpapi","llm-math","wikipedia"],llm=llm)

print(tools[1].name)
agent = initialize_agent(tools, llm, agent = "zero-shot-react-description", verbose = True)
# # self_ask_with_search = initialize_agent(tools, llm, agent=AgentType.SELF_ASK_WITH_SEARCH, verbose=True)
# result = agent.run("search tcs on https://www.businesstoday.in")
result  = agent.run("suggest me some ideas how can food wastage be prevented using tech?")
print(result)