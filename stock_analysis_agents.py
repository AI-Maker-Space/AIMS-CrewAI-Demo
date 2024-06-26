from crewai import Agent

from tools.search_tools import SearchTools
from tools.calculator_tools import CalculatorTools
from tools.sec_tools import SECTools

from langchain_community.tools.yahoo_finance_news import YahooFinanceNewsTool
from langchain_anthropic import ChatAnthropic

class StockAnalysisAgent:
    def __init__(self):
        # Initialize the language model for all agents
        self.llm = ChatAnthropic(model="claude-3-5-sonnet-20240620")

    def financial_analyst(self):
        # Create and return a financial analyst agent
        return Agent(
            role="A Professional Financial Analyst",
            goal="Provide clean, concise, and actionable financial analysis.",
            backstory="An experienced financial analyst with a strong background in finance and economics. Focused on providing safe and reliable financial advice to clients.",
            verbose=True,
            llm=self.llm,
            tools=[
                SearchTools.search_news,
                CalculatorTools.calculate,
                YahooFinanceNewsTool(),
                SECTools.search_10q
            ]
        )
    
    def research_analyst(self):
        # Create and return a research analyst agent
        return Agent(
            role="A Professional Research Analyst",
            goal="Gather and analyze information to provide insights and recommendations.",
            backstory="A seasoned research analyst with a keen eye for detail and a passion for uncovering valuable insights. Focused on delivering high-quality research to clients.",
            verbose=True,
            llm=self.llm,
            tools=[
                SearchTools.search_internet,
                SearchTools.search_news,
                YahooFinanceNewsTool()
            ]
        )
    
    def investment_advisor(self):
        # Create and return an investment advisor agent
        return Agent(
            role="Private Investment Advisor",
            goal="Provide personalized investment advice and recommendations.",
            backstory="A trusted investment advisor with a proven track record of success. Focused on helping clients achieve their financial goals through strategic investments.",
            verbose=True,
            llm=self.llm,
            tools=[
                SearchTools.search_internet,
                SearchTools.search_news,
                CalculatorTools.calculate,
                YahooFinanceNewsTool()
            ]
        )