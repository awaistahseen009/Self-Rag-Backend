from graph.graph import app as graph_app
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from models import UserQuery

load_dotenv()

app = FastAPI()

@app.post("/api/v1/query")
async def answer_query(data: UserQuery):
    return graph_app.invoke({"question": data.query})
    


if __name__== "__main__":
    print("*** MAIN FUNCTION ***")
    print(app.invoke({"question": "What is pizza ? "}))