from retreiver import retriever
from graph.state import GraphState
from typing import Any , Dict
from retreiver import retriever


def retreive_document(state:GraphState)->Dict[str, Any]:
    print("***RETREIVING THE DOCUMENTS***")
    question = state['question']
    documents = retriever.invoke(question)
    return {'related_documents':documents, 'question':question}