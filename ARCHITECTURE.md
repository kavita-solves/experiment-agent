# Architecture

## Flow
User
│
├──► Streamlit UI (app.py) ──┐
│ │
└──► FastAPI (api.py) ───────┤
▼
LangChain Agent (agent.py)
│
┌────────────┼────────────┐
▼ ▼ ▼
Deterministic LLM-Reasoned Historical
Tools Tools Lookup
(sample size, (metric/guard- (stub, real
opp. cost) rail recs, retrieval in
hypothesis) Week 3-4)