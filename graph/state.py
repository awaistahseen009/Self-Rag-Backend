from typing import List , TypedDict

class GraphState(TypedDict):
    question:str
    generation:str
    related_documents:List[str]
    web_search:bool