"""
IX-Joey REST API Server

Provides HTTP API endpoint for IX-Joey generalist sibling AI.
Handles incoming user queries and returns responses from IX-Joey orchestrator.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from core.joey_orchestrator import IXJoeyOrchestrator

app = FastAPI()
joey_orchestrator = IXJoeyOrchestrator()

class QueryRequest(BaseModel):
    query: str

@app.post("/query")
async def handle_query(request: QueryRequest):
    if not request.query or request.query.strip() == "":
        raise HTTPException(status_code=400, detail="Query must not be empty.")
    try:
        response = joey_orchestrator.process_query(request.query)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)
