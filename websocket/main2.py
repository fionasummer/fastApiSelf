from fastapi import FastAPI
# 基于类的视图模式来处理HTTP方法和WebSocket会话
from starlette.endpoints import WebSocketEndpoint, HTTPEndpoint
from starlette.responses import HTMLResponse
from starlette.routing import Route, WebSocketRoute
from websocket.database import info

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


class Homepage(HTTPEndpoint):
    async def get(self, request):
        return HTMLResponse(html)


class Echo(WebSocketEndpoint):
    encoding = "text"

    # 连接
    async def on_connect(self, websocket):
        await websocket.accept()
        info.append(websocket)
        print(info)

    # 收发
    async def on_receive(self, websocket, data):
        for wbs in info:
            await wbs.send_text(f"Message text was: {data}")

    # 断开
    async def on_disconnect(self, websocket, close_code):
        info.remove(websocket)
        print(info)
        pass


routes = [
    Route("/", Homepage),
    WebSocketRoute("/ws", Echo)
]

app = FastAPI(routes=routes)
