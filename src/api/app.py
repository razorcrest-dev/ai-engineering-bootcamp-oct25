from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from src.api.core.config import config
from src.api.api.endpoints import api_router
from src.api.api.middleware import RequestIDMiddleware

import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


app = FastAPI()

app.add_middleware(RequestIDMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)



@app.get("/")
async def root():
    """ Root Endpoint that returns a welcome message."""
    return {"message": "API"}

# def run_llm(provider, model_name, messages, max_tokens=500):

#     if provider == "OpenAI":
#         client = OpenAI(api_key=config.OPENAI_API_KEY)
#     elif provider == "Groq":
#         client = Groq(api_key=config.GROQ_API_KEY)
#     else:
#         client = genai.Client(api_key=config.GOOGLE_API_KEY)


#     if provider == "Google":
#         return client.models.generate_content(
#             model=model_name, 
#             contents=[message["content"] for message in messages],
#         ).text
#     else:
#         return client.chat.completions.create(
#             model=model_name, 
#             messages=messages,
#             max_tokens=max_tokens
#         ).choices[0].message.content


# class ChatRequest(BaseModel):
#     provider: str
#     model_name: str
#     messages: list[dict]


# class ChatResponse(BaseModel):
#     message: str


# @app.post("/chat")
# def chat(
#     request:Request,
#     payload: ChatRequest
# ) -> ChatResponse:

    # result = run_llm(payload.provider, payload.model_name, payload.messages)
    # return ChatResponse(message=result)


