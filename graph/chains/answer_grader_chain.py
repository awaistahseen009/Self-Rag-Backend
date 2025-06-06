from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.pydantic_v1 import BaseModel , Field
load_dotenv()

llm = ChatOpenAI(temperature=0.2, model="gpt-4o-2024-08-06")

class AnswerGraderSchema(BaseModel):
    binary_score:str = Field(description="Answer is relevant to the question. 'yes' or 'no'")

structured_llm_parser = llm.with_structured_output(AnswerGraderSchema)

system_prompt = """You are an experience answer grader who checks whether the generated answer addresses/resolves the question of the user. Give a binary score of "yes" if it resolves. Otherwise give "no"
"""

answer_grader_prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "User question: {question}\n\n LLM Generation: {generation}")
])

answer_grader_chain = answer_grader_prompt | structured_llm_parser