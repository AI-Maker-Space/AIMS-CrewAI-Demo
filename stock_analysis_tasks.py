from crewai import Task
from textwrap import dedent

class StockAnalysisTasks():
    def research(self, agent, company):
        # Create a research task for the given company
        return Task(
            description=dedent(f"""\
                Collect and summarize recent news articles, press releases, and market analyses related to the 
                company's stock and industry.
                
                Pay attention to recent trends, and sentiments. 
                Also include any major upcoming events or planned announcements.
                                            
                Your final answer MUST be a report that includes a comprehensive summary of the latest news, 
                any notable shifts in market sentiment, and potential impacts on the stock.
                                            
                Also ensure to return the Stock Ticker.
                                            
                {self.__tip_section()}

                Selected company by the customer: {company}
                """),
            expected_output=dedent("""\
                A detailed report that includes a comprehensive summary of the latest news, any notable shifts in market sentiment, and potential impacts on the stock.
                """),
            agent=agent
        )

    def financial_analysis(self, agent):
        # Create a financial analysis task
        return Task(
            description=dedent(f"""\
                Conduct a thorough analysis of the stock's financial performance, including key financial metrics, and ratios. 
                
                Also consider the company's financial health, profitability, and growth prospects.
                                        
                Additionally, do a comparative analysis with industry peers and provide insights on the stock's valuation.
                                            
                Your final answer MUST be a detailed financial analysis report that includes key financial metrics,
                profitability ratios, growth prospects, and valuation analysis.

                {self.__tip_section()}                           
                """),
            expected_output=dedent("""\
                A detailed financial analysis report that includes key financial metrics, profitability ratios, growth prospects, and valuation analysis.
                """),
            agent=agent
        )

    def recommendation(self, agent):
        # Create an investment recommendation task
        return Task(
            description=dedent(f"""\
                Review the financial analysis and research findings to provide a detailed investment recommendation.
                
                You must consider the company's financial health, growth prospects, and valuation - as well as recent news and market sentiment.
                                            
                Your final answer must be a recommendation for your customer. It should be a detailed report, providing a clear investment stance and strategy with supporting evidence.
                                        
                Use Markdown formatting to make your report visually appealing and easy to read.

                {self.__tip_section()}                           
                """),
            expected_output=dedent("""\
                A well formatted and detailed investment recommendation report that provides a clear investment stance and strategy with supporting evidence.
                """),
            agent=agent
        )

    def __tip_section(self):
        # Private method to add a motivational tip to task descriptions
        return "If you do an amazing job, you'll receive $25,000 comission!"