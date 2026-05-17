import asyncio
from asyncua import Client

OPC_URL      = "opc.tcp://localhost:4840"
OPC_USER     = "operator"
OPC_PASSWORD = "Factory2026!"

BASE = "ns=4;s=|var|CODESYS Control Win V3 x64.Application.PLC_PRG."

NODES = {
    "xStart":       BASE + "xStart",
    "xStop":        BASE + "xStop",
    "xRunning":     BASE + "xRunning",
    "iCycleCount":  BASE + "iCycleCount",
    "rTemperature": BASE + "rTemperature",
    "sState":       BASE + "sState",
}

live_data = {
    "xStart":       False,
    "xStop":        False,
    "xRunning":     False,
    "iCycleCount":  0,
    "rTemperature": 0.0,
    "sState":       "IDLE",
}

async def read_plc_loop():
    while True:
        try:
            client = Client(url=OPC_URL)
            client.set_user(OPC_USER)
            client.set_password(OPC_PASSWORD)

            async with client:
                print(f"✅ Authenticated as '{OPC_USER}' on CODESYS OPC-UA")
                nodes = {
                    key: client.get_node(nid)
                    for key, nid in NODES.items()
                }
                while True:
                    for key, node in nodes.items():
                        live_data[key] = await node.read_value()
                    await asyncio.sleep(0.1)

        except Exception as e:
            print(f"⚠️ Connection error: {e} — retrying in 3s")
            await asyncio.sleep(3)

async def write_tag(tag_name: str, value: bool):
    client = Client(url=OPC_URL)
    client.set_user(OPC_USER)
    client.set_password(OPC_PASSWORD)
    async with client:
        node = client.get_node(NODES[tag_name])
        await node.write_value(value)