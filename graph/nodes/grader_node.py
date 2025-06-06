from graph.chains.grader_chain import grader_chain
from typing import Any , Dict
from graph.state import GraphState

def grade_documents(state:GraphState)->Dict[str, Any]:
    question = state['question']
    documents = state['related_documents']
    filtered_docs = []
    web_search = False 
    for doc in documents:
        score = grader_chain.invoke(
            {'documents':doc.page_content, "question":question}
        )
        grade = score.binary_score
        if grade.lower() == "yes":
            print("***Document is relevant so adding them to filtered documents***")
            filtered_docs.append(doc)
        else:
            web_search = True
            print("*** Documents is not relevant")
            continue
    return {"related_documents":filtered_docs , "question":question, "web_search":web_search}
