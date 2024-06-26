from crewai import Crew
from textwrap import dedent

from stock_analysis_agents import StockAnalysisAgent
from stock_analysis_tasks import StockAnalysisTasks

from dotenv import load_dotenv
load_dotenv()

class StockAnalysisCrew:
    def __init__(self, company):
        # Initialize the crew with a company to analyze
        self.company = company
    
    def run(self):
        # Create instances of agents and tasks
        agents = StockAnalysisAgent()
        tasks = StockAnalysisTasks()

        # Create specific agent instances
        research_agent = agents.research_analyst()
        financial_agent = agents.financial_analyst()
        investment_agent = agents.investment_advisor()

        # Create specific task instances
        research_task = tasks.research(research_agent, self.company)
        financial_task = tasks.financial_analysis(financial_agent)
        recommendation_task = tasks.recommendation(investment_agent)

        # Create a Crew instance with the agents and tasks
        crew = Crew(
            agents=[research_agent, financial_agent, investment_agent],
            tasks=[research_task, financial_task, recommendation_task],
            verbose=True
        )

        # Execute the crew's tasks and return the result
        result = crew.kickoff()
        return result
    
if __name__ == "__main__":
    print("## Welcome to the Stock Analysis Crew! ##")
    # Get user input for the company to analyze
    company = input("Enter the company you want to analyze: ")
    # Create and run the StockAnalysisCrew
    crew = StockAnalysisCrew(company)
    result = crew.run()
    # Print the results
    print("\n\n##############################################")
    print("## Stock Analysis Crew Task Results ##")
    print("##############################################")
    print(result)