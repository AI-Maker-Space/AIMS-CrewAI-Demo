import os
import requests
from langchain.tools import tool
from sec_api import QueryApi

from unstructured.partition.html import partition_html

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

class SECTools():
    @tool("Search 10-Q Forms")
    def search_10q(data):
        """
        Useful for searching information from the latest 10-Q form for a given ticker and question about that ticker.

        The input to this tool should be a pipe (|) separated string in the following format:
        {"data" : "TICKER|QUERY"}

        For example: {"data" : "AAPL|What is the revenue for Apple last quarter?"}
        """
        stock, query = data.split("|")
        queryApi = QueryApi(api_key=os.environ["SEC_API_API_KEY"])
        search_query = {
            "query":{
                "query_string": {
                    "query" : f"ticker:{stock} AND formType:\"10-Q\""
                }
            
            },
            "from": 0,
            "size": 1,
            "sort": [{"filedAt": {"order": "desc"}}]
        }

        filings = queryApi.get_filings(search_query)["filings"]
        if len(filings) == 0:
            return "There were no filings for this ticvker - please ensure the ticker is correct."
        link = filings[0]['linkToFilingDetails']
        answer = SECTools.__embedding_search(link, query)
        return answer
    
    def __download_form_html(url):
        headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7',
        'Cache-Control': 'max-age=0',
        'Dnt': '1',
        'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"macOS"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }

        response = requests.get(url, headers=headers)
        return response.text
    
    def __embedding_search(url, query):
        text = SECTools.__download_form_html(url)
        elements = partition_html(text=text)
        content = "\n".join([str(element) for element in elements])
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
            is_separator_regex=False,
        )

        text_chunks = text_splitter.create_documents([content])
        embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
        retriever = FAISS.from_documents(
            text_chunks, embeddings
        ).as_retriever()
        answers = retriever.get_relevant_documents(query, top_k=4)
        return "\n\n".join([a.page_content for a in answers])

