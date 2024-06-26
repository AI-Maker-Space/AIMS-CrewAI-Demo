import json
import os

from serpapi import GoogleSearch
from langchain.tools import tool

class SearchTools():
    @tool("Search the internet")
    def search_internet(query):
        """Useful to search the internet about a given topic and return relevant results."""
        # Set the number of top results to return
        top_results_to_return = 4
        # Get the SERP API key from environment variables
        serp_api_key = os.environ["SERP_API_KEY"]

        # Perform the Google search using SerpAPI
        search_results = GoogleSearch({
            "q": query,
            "api_key": serp_api_key,
        })
        search_results = search_results.get_dict()

        # Initialize an empty string to store the results
        result_string = ""

        # Iterate through the top results and format them
        for result in search_results["organic_results"][:top_results_to_return]:
            try:
                result_string += f"{result['title']}\n{result['snippet']}\n{result['link']}\n\n"
            except KeyError:
                # Skip results that don't have all required fields
                continue

        # If no results were found, return a message
        if result_string == "":
            result_string = "Nothing found."

        return result_string
    
    @tool("Search the internet for news")
    def search_news(query):
        """Useful to search the internet for news about a given topic and return relevant results."""
        # Set the number of top news results to return
        top_results_to_return = 4
        # Get the SERP API key from environment variables
        serp_api_key = os.environ["SERP_API_KEY"]

        # Perform the Google News search using SerpAPI
        search_results = GoogleSearch({
            "q": query,
            "api_key": serp_api_key,
            "tbm" : "nws"  # Set the search type to news
        })
        search_results = search_results.get_dict()

        # Initialize an empty string to store the news results
        result_string = ""

        # Iterate through the top news results and format them
        for result in search_results["news_results"][:top_results_to_return]:
            try:
                result_string += f"{result['title']}\n{result['snippet']}\n{result['link']}\n\n"
            except KeyError:
                # Skip results that don't have all required fields
                continue

        # If no news results were found, return a message
        if result_string == "":
            result_string = "No news found."

        return result_string