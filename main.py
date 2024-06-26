from crewai import Crew
from textwrap import dedent

from stock_analysis_agents import StockAnalysisAgent
from stock_analysis_tasks import StockAnalysisTasks

from dotenv import load_dotenv
load_dotenv()

class StockAnalysisCrew:
    def __init__(self, company):
        self.company = company
    
    def run(self):
        agents = StockAnalysisAgent()
        tasks = StockAnalysisTasks()

        research_agent = agents.research_analyst()
        financial_agent = agents.financial_analyst()
        investment_agent = agents.investment_advisor()

        research_task = tasks.research(research_agent, self.company)
        financial_task = tasks.financial_analysis(financial_agent)
        recommendation_task = tasks.recommendation(investment_agent)

        crew = Crew(
            agents=[research_agent, financial_agent, investment_agent],
            tasks=[research_task, financial_task, recommendation_task],
            verbose=True
        )

        result = crew.kickoff()
        return result
    
if __name__ == "__main__":
    print("## Welcome to the Stock Analysis Crew! ##")
    company = input("Enter the company you want to analyze: ")
    crew = StockAnalysisCrew(company)
    result = crew.run()
    print("\n\n##############################################")
    print("## Stock Analysis Crew Task Results ##")
    print("##############################################")
    print(result)