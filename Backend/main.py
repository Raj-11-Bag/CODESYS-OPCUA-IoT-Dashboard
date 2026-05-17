import asyncio
import json
from contextlib import asynccontextmanager
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from opc_client import read_plc_loop, live_data, write_tag

@asynccontextmanager
async def lifespan(app: FastAPI):
    task = asyncio.create_task(read_plc_loop())
    yield
    task.cancel()

app = FastAPI(title="PLC IoT Dashboard", lifespan=lifespan)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("🔌 Browser connected")
    try:
        while True:
            payload = {
                "xRunning":     bool(live_data["xRunning"]),
                "iCycleCount":  int(live_data["iCycleCount"]),
                "rTemperature": round(float(live_data["rTemperature"]), 2),
                "sState":       str(live_data["sState"]),
            }
            await websocket.send_text(json.dumps(payload))
            await asyncio.sleep(0.1)
    except WebSocketDisconnect:
        print("❌ Browser disconnected")

@app.post("/control/start")
async def start_machine():
    await write_tag("xStart", True)
    await asyncio.sleep(0.2)
    await write_tag("xStart", False)
    return {"status": "started"}

@app.post("/control/stop")
async def stop_machine():
    await write_tag("xStop", True)
    await asyncio.sleep(0.2)
    await write_tag("xStop", False)
    return {"status": "stopped"}

@app.get("/")
async def get_dashboard():
    with open("static/index.html") as f:
        return HTMLResponse(f.read())