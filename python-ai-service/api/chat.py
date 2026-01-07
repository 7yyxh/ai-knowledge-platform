from fastapi import APIRouter
from schemas.chat import ChatRequest, ChatResponse
from service.llm_service import chat_with_llm

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    answer = chat_with_llm(req.query)
    return ChatResponse(answer=answer)
