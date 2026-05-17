# CODESYS OPC-UA IoT Dashboard

![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![CODESYS](https://img.shields.io/badge/CODESYS-V3.5_SP22-blue)
![Python](https://img.shields.io/badge/Python-3.11-yellow)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green)
![OPC--UA](https://img.shields.io/badge/OPC--UA-IEC_62541-orange)

## Overview
A fully functional Industry 4.0 IoT monitoring and control dashboard
connecting a CODESYS SoftPLC to a browser interface via OPC-UA,
Python FastAPI, and WebSockets. Zero physical hardware required.

## Demo
[Watch Demo Video](demo/dashboard_demo.mp4)

## Folder Structure 
```
CODESYS-OPCUA-IoT-Dashboard/
│
├── README.md
├── requirements.txt
│
├── plc/
│   └── IoT_dashboard_with_security_Raj_Bag.project
│
├── backend/
│   ├── main.py
│   ├── opc_client.py
│   └── find_nodes.py
│
├── frontend/
│   └── static/
│       └── index.html
│
├── docs/
│   ├── architecture_diagram.png
│   └── signal_table.md
│
└── demo/
    └── dashboard_demo.mp4
```

## System Architecture
```CODESYS V3.5 SoftPLC
└── IEC 61131-3 Structured Text
└── 6 live process variables
↕ OPC-UA Server (port 4840)
↕ role-based ACL security
Python asyncua Client (100ms polling)
└── FastAPI async backend
└── WebSocket broadcaster
↕ ws://localhost:8000/ws
Browser Dashboard
└── Live state indicator
└── Cycle counter + trend chart
└── Temperature gauge + graph
└── START/STOP PLC control buttons
```
## Technology Stack
| Layer | Technology |
|---|---|
| PLC Runtime | CODESYS Control Win V3.5 SP22 |
| PLC Language | IEC 61131-3 Structured Text |
| OPC-UA Protocol | IEC 62541, port 4840 |
| Python Client | asyncua 1.1.8 |
| Backend | FastAPI + uvicorn |
| Real-time Push | WebSockets (100ms) |
| Frontend | Vanilla JS + Canvas API |

## Security Implementation
- Role-based access control via CODESYS User Management
- Anonymous group: read-only View access
- Operator account: Service group with Modify rights
- Authentication: Username/Password, AUTO_NEGOTIATE encryption
- Plain-text password transmission enabled over local loopback

## How to Run

### 1. Start CODESYS
Open `plc/IoT_dashboard_with_security_Raj_Bag.project`
→ Online → Login → Run

### 2. Install Python dependencies
```bash
pip install -r requirements.txt
```

### 3. Start backend
```bash
cd backend
uvicorn main:app --reload --port 8000
```

### 4. Open dashboard
Navigate to `http://localhost:8000`

## Key Features
- Fully async stack — no blocking, no freezing under load
- Bidirectional control — browser writes commands back to PLC
- Live WebSocket push — no polling, instant updates
- Role-based OPC-UA security — read/write access separation
- 100% virtual — no physical PLC hardware needed

## Author
**Raj Bag**
M.Sc. Robotics Candidate — Germany 2026
[LinkedIn](your-linkedin-url)
[Portfolio](your-portfolio-url)

## License
MIT License
