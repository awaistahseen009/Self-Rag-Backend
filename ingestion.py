from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_pinecone import PineconeVectorStore
from uuid import uuid4
from index import vector_store
load_dotenv()
FILE_NAME = "test.pdf"

def add_documents_to_db(filename:str):
    # Defining the loader 
    loader = PyPDFLoader(filename, mode='single')

    docs = loader.load()
    # Split the document
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 500, 
        chunk_overlap = 80, 
        length_function = len,

    )
    text_docs = splitter.split_documents(docs)
    vector_store.add_documents(text_docs)
if __name__=="__main__":
    id = uuid4()
    add_documents_to_db(FILE_NAME)
    print("Document added successfully")