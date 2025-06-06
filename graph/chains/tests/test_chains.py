from retreiver import retriever
from graph.chains.grader_chain import grader_chain
from graph.chains.hallucination_chain import hallucination_chain
from graph.chains.generation_chain import generation_chain
def test_retriever() -> None:
    question = "cyclic assignment approach"
    documents = retriever.invoke(question)
    assert len(documents) > 0

def test_grade_document_yes()->None:
    question = "cyclic assignment approach"
    document = retriever.invoke(question)
    score = grader_chain.invoke({"documents":document[0].page_content, "question":question})
    assert score.binary_score == "yes"

def test_grade_document_no()->None:
    question = "what is pizza"
    document = retriever.invoke(question)
    score = grader_chain.invoke({"documents":document[0].page_content, "question":question})
    assert score.binary_score == "no"

def test_hallucination()->None:
    question = "cyclic assignment approach"
    document = retriever.invoke(question)
    generation = generation_chain.invoke({"context":document[0].page_content, "question":question})
    score = hallucination_chain.invoke({"documents":document[0].page_content, "generation":generation})
    assert score.binary_score == "yes"

 