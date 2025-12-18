from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import uvicorn

app = FastAPI()
clients = []

print("oui")


@app.websocket("/ws")
async def chat(ws: WebSocket):
    print("NOUVEAU CLIENT")
    await ws.accept()
    print("CONNECTÉ !")
    clients.append(ws)

    try:
        while True:
            print("EN ATTENTE DE MESSAGE...")
            msg = await ws.receive_text()
            print("REÇU :", msg)
            for client in clients:
                await client.send_text(msg)
            print(clients)
    except WebSocketDisconnect:
        print("CLIENT DÉCONNECTÉ !")
        clients.remove(ws)


if __name__ == "__main__":
    uvicorn.run(app, host="172.20.10.11", port=8010)
