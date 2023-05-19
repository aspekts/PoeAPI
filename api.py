from poe import load_chat_id_map, clear_context, send_message, get_latest_message, set_auth
import os
from typing import Annotated
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Header
from fastapi.responses import HTMLResponse
#--------------------------------------------------------------------------
app = FastAPI(
    title="Free Poe.com API",
    description="This is an API for Poe.com, a chatbot that uses GPT-3 to chat with you.",
    version="0.0.1"
)
bots =['capybara','a2','chinchilla']


@app.get("/chat/{bot}")
async def chat(bot: str, cookie: Annotated[str | None, Header()], formkey: Annotated[ str | None, Header()], message: str):
    set_auth('Quora-Formkey',formkey)
    set_auth('Cookie',cookie)
    chat_id = load_chat_id_map(bot)
    clear_context(chat_id)
    if message =="!clear":
        clear_context(chat_id)
        print("Context is now cleared")
    if message =="!break":
            return { "message" : "Conversation ended" }
    send_message(message,bot,chat_id)
    reply = get_latest_message(bot)
    print(f"{bot} : {reply}")
    return { "message" : reply, "status": "success", "chat_id":chat_id }
@app.get("/")
async def main():
    content = """
    <body>
    <h1>Poe.com API</h1>
    <p>Go to <a href="/docs">/docs</a> to see the API documentation.</p>
    </body>
    """
    return HTMLResponse(content=content)
