from graph.state import GraphState
from langchain_community.tools.tavily_search import TavilySearchResults
from typing import Any , Dict
from langchain.schema import Document

web_tool = TavilySearchResults(max_results = 3)

def web_search(state:GraphState)->Dict[str , Any]:
    print("*** Searching on the web ***")
    question = state['question']
    documents = state['related_documents']
    search_results = web_tool.invoke({"query":question})
    results = "\n".join([
        search_result['content'] for search_result in search_results
    ])
    final_result = Document(page_content=results)
    if documents is not None:
        documents.append(final_result)
    else:
        documents = [final_result]
    return {"related_documents":documents , "question":question}