import asyncio
from asyncua import Client

async def find_vars():
    client = Client(url="opc.tcp://localhost:4840")
    client.set_user("operator")
    client.set_password("Factory2026!")
    
    async with client:
        print("Connected! Searching...\n")
        
        test_paths = [
            "ns=4;s=|var|CODESYS Control Win V3 x64.Application.PLC_PRG.xStart",
            "ns=4;s=|var|CODESYS Control Win V3 x64.Application.PLC_PRG.iCycleCount",
            "ns=4;s=|var|CODESYS Control Win V3 x64.Application.PLC_PRG.rTemperature",
            "ns=4;s=|var|CODESYS Control Win V3 x64.Application.PLC_PRG.sState",
            "ns=4;s=|var|CODESYS Control Win V3 x64.Application.PLC_PRG.xRunning",
            "ns=4;s=|var|CODESYS Control Win V3 x64.Application.PLC_PRG.xStop",
            "ns=3;s=|var|CODESYS Control Win V3 x64.Application.PLC_PRG.xStart",
            "ns=2;s=|var|CODESYS Control Win V3 x64.Application.PLC_PRG.xStart",
        ]
        
        for path in test_paths:
            try:
                node = client.get_node(path)
                val = await node.read_value()
                print(f"✅ FOUND: {path} = {val}")
            except Exception as e:
                print(f"❌ {path}")

asyncio.run(find_vars())