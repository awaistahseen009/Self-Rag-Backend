from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.pydantic_v1 import BaseModel , Field
load_dotenv()

llm = ChatOpenAI(temperature=0.2, model="gpt-4o-2024-08-06")

class HallucinationSchema(BaseModel):
    binary_score:str = Field(description="Answer is grounded/present in the facts. Give 'yes' or 'no' ")

structured_llm_parser = llm.with_structured_output(HallucinationSchema)
system_prompt = """You are an experience hallucination grader and your job is to check whether the generated answer is grounded/related to the facts/documents provided.Give a binary score "yes" or "no"."yes" means answer is grounded in the facts.
"""
hallucination_prompt = ChatPromptTemplate.from_messages([
    ('system', system_prompt),
    ("human", "Facts:\n{documents}\n\nLLM Generated Answer: {generation}")
])
hallucination_chain = hallucination_prompt | structured_llm_parser
