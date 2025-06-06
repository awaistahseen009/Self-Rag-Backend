from dotenv import load_dotenv
from langgraph.graph import END, StateGraph
from graph.nodes import generate , grade_documents , retreive_document , web_search
from graph.chains.answer_grader_chain import answer_grader_chain
from graph.chains.hallucination_chain import hallucination_chain
from graph.state import GraphState
load_dotenv()


def web_enable_or_not(state:GraphState):
    if state['web_search']:
        print("Searching the web")
        return "websearch"
    else:
        print("generating")
        return "generate"

def grade_generation_in_documents(state:GraphState):
    print("***Checking the hallucinations***")
    question = state['question']
    documents = state["related_documents"]
    generation = state["generation"]
    score = hallucination_chain.invoke({"documents":documents, "generation":generation})
    if hal_score := score.binary_score:
        print("***Generation is related to the documents***")
        print("*** Now grading the question vs generation***")
        score = answer_grader_chain.invoke({"question":question, "generation":generation})
        if answer_score := score.binary_score:
            print("*** Generation addresses the question ***")
            return "useful"
        else:
            print("not useful")
    else:
        print("***Answer is not grounded in the documents***")
        return "not supported"



workflow = StateGraph(GraphState)
workflow.add_node("retreive", retreive_document)
workflow.add_node("grade_documents", grade_documents)
workflow.add_node("generate", generate)
workflow.add_node("websearch", web_search)

workflow.set_entry_point("retreive")
workflow.add_edge("retreive", "grade_documents")
workflow.add_conditional_edges(
    "grade_documents", 
    web_enable_or_not, 
)

workflow.add_conditional_edges(
    "generate", 
    grade_generation_in_documents,
    {
        "not supported" : "generate", 
        "useful" : END, 
        "not useful": "websearch"
    }
)
workflow.add_edge("websearch", "generate")
workflow.add_edge("generate", END)

app = workflow.compile()

