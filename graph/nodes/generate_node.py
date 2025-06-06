from graph.state import GraphState
from graph.chains.generation_chain import generation_chain
from typing import Dict , Any
def generate(state:GraphState)->Dict[str , Any]:
    question = state['question']
    documents = state['related_documents']
    generation = generation_chain.invoke({"context":documents, "question":question})
    return {"generation":generation, "related_documents":documents , "question":question}
