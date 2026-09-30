import logging
import uuid
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel, Field
from langchain.messages import HumanMessage
from agent import agent
from tools import calculate_sample_size_proportion

logger = logging.getLogger(__name__)

app = FastAPI(title="Experiment Agent API")

class ChatRequest(BaseModel):
    message: str = Field(min_length =1 , max_length = 2000)
    thread_id: str | None = None

class ChatResponse(BaseModel):
    reply: str
    thread_id: str

class SampleSizeRequest(BaseModel):
    baseline_rate: float
    mde: float
    daily_traffic: int
    split: float
    power: float = 0.80
    significance: float = 0.05

@app.get("/health")
def health():
    return {"status":"ok"}

@app.post("/chat", response_model=ChatResponse)
def chat( req: ChatRequest):
    thread_id = req.thread_id or str(uuid.uuid4())
    try:
        result = agent.invoke(
            {"messages": [HumanMessage(content=req.message)]},
            {"configurable": {"thread_id":thread_id}
            , "recursion_limit": 25
           }
           )
    except Exception:
        logger.exception("chat failed")
        raise HTTPException(status_code = 502 , detail= "Agent failed to process the request.")
    return ChatResponse(reply = result["messages"][-1].content, thread_id = thread_id)

@app.post("/tools/samplesize")
def sample_size(req: SampleSizeRequest):
    result =  calculate_sample_size_proportion.invoke(req.model_dump())
    if "error" in result:
        raise HTTPException(status_code = 400, detail = result["error"])
    return result
