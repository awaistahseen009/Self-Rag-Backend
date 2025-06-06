from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel , Field
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
llm = ChatOpenAI(temperature=0.2, model="gpt-4o-2024-08-06")

class DocumentGrader(BaseModel):
    binary_score:str = Field(description="Documents are relevant to the question or not, ouput 'yes' or 'no'")


structured_llm_grader = llm.with_structured_output(DocumentGrader)

system_prompt = """You are a professional grader whos job is to grade the relevance of the documents to the question of the user. If the document contains the keyword , semantic meaning , or any facts related to the question, Grade it relevant. Give a binary score of "yes" or "no" to indicate the relevance of the document with the question.
"""

grader_prompt = ChatPromptTemplate.from_messages([
    ('system', system_prompt), 
    ("human", "Retreived documents: {documents}\n\n User question: {question}")
])

grader_chain = grader_prompt | structured_llm_grader