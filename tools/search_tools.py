import json
import os

from serpapi import GoogleSearch
from langchain.tools import tool

class SearchTools():
    @tool("Search the internet")
    def search_internet(query):
        """Useful to search the internet about a given topic and return relevant results."""
        top_results_to_return = 4
        serp_api_key = os.environ["SERP_API_KEY"]

        search_results = GoogleSearch({
            "q": query,
            "api_key": serp_api_key,
        })
        search_results = search_results.get_dict()

        result_string = ""

        for result in search_results["organic_results"][:top_results_to_return]:
            try:
                result_string += f"{result['title']}\n{result['snippet']}\n{result['link']}\n\n"
            except KeyError:
                continue

        if result_string == "":
            result_string = "Nothing found."

        return result_string
    
    @tool("Search the internet for news")
    def search_news(query):
        """Useful to search the internet for news about a given topic and return relevant results."""
        top_results_to_return = 4
        serp_api_key = os.environ["SERP_API_KEY"]

        search_results = GoogleSearch({
            "q": query,
            "api_key": serp_api_key,
            "tbm" : "nws"
        })
        search_results = search_results.get_dict()

        result_string = ""

        for result in search_results["news_results"][:top_results_to_return]:
            try:
                result_string += f"{result['title']}\n{result['snippet']}\n{result['link']}\n\n"
            except KeyError:
                continue

        if result_string == "":
            result_string = "No news found."

        return result_string

