from langchain.tools import tool

class CalculatorTools():
    @tool("Execute a calculation through Python")
    def calculate(operation):
        """Useful to execute a calculation through Python and return the result. Inputs to this tool should be in the form of a Python operation. 
        For example, to add 2 and 2, the input should be `2+2`. For 100 times 7 divided by 5 plus 3, the input should be `100*7/5+3`."""
        return eval(operation)