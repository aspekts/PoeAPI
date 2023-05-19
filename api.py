from poe import load_chat_id_map, clear_context, send_message, get_latest_message, set_auth
import os
from typing import Annotated
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Header
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
#--------------------------------------------------------------------------
app = FastAPI(
    title="Free Poe.com API",
    description="This is an API for Poe.com, a chatbot that uses GPT-3 to chat with you.",
    version="0.0.1",
    redoc_url="/docs",
    docs_url=None
)
bots =['capybara','a2','chinchilla']

class Item(BaseModel):
    bot: str
    message: str
    cookie: str
    formkey: str

@app.get(
    "/chat/{bot}",
    response_model=Item,
    summary="Chat",
    description="This endpoint allows you to chat with the chosen bot on Poe.com. The bot will respond to your message. You can choose between the following bots: Sage (OpenAI): `capybara` , Claude-Instant (Anthropic): `a2` , ChatGPT (OpenAI): `chinchilla`",
    responses={
            200: {
                "description": "Success",
                "content": {
                    "application/json": {
                        "example": {
                            "message": "Hello!",
                            "status": "success",
                            "chat_id": "123456789"
                        }
                    }
                }
            },
            400: {
                "description": "Bad Request",
                "content": {
                    "application/json": {
                        "example": {
                            "message": "Bad Request",
                            "details": "The bot you selected is not available. Please choose one of the following bots: capybara, a2, chinchilla",
                            "status": "error",
                        }
                    }
                }
            },
            "422": {
                "description": "Unprocessable Entity",
            },
            500: {
                "description": "Internal Server Error",
                "content": {
                    "application/json": {
                        "example": {
                            "message": "Internal Server Error",
                            "status": "error",
                        }
                    }
                }
            }
        }
    )

async def chat(bot:str, options: Item):
    """
    This is a Python function that allows users to select and chat with a bot from Poe.com.
    """
    if bot not in bots:
        return JSONResponse(status_code=400, content={"message" : "Bad Request", "details":"The bot you selected is not available. Please choose one of the following bots: capybara, a2, chinchilla", "status":"error"})
    if options.cookie is None or options.formkey is None:
        return JSONResponse(status_code=400, content={"message" : "Bad Request", "details":"At least one of the headers is not provided. Please ensure both the formkey and cookie headers are set.", "status":"error"})
    try:
        set_auth('Quora-Formkey',options.formkey)
        set_auth('Cookie',options.cookie)
        chat_id = load_chat_id_map(options.bot)
        clear_context(chat_id)
        send_message(options.message,options.bot,chat_id)
        reply = get_latest_message(options.bot)
        return JSONResponse(status_code=200, content={"message" : reply, "status":"success", "chat_id":chat_id })
    except:
        return JSONResponse(status_code=500, content={"message" : "Internal Server Error", "status":"error"})

@app.get("/")
async def main():

    """
    This function sets up a basic endpoint for the Poe.com API that returns a simple HTML response with
    a link to the API documentation.
    :return: The `main` function is returning an HTML response with a title "Poe.com API" and a
    paragraph with a link to the API documentation. When the user navigates to the root URL ("/"), they
    will see this HTML content.
    """
    content = """
    <body>
    <h1>Poe.com API</h1>
    <p>Go to <a href="/docs">/docs</a> to see the API documentation.</p>
    </body>
    """
    return HTMLResponse(content=content)
