from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Account Service")

# In-memory store, stand-in for a database. Fine for a demo microservice.
ACCOUNTS = {
    "ACC1001": {"holder": "A. Sharma", "balance": 48250.75},
    "ACC1002": {"holder": "R. Mehta", "balance": 12900.00},
}


class HealthResponse(BaseModel):
    status: str


@app.get("/health", response_model=HealthResponse)
def health():
    # Liveness/readiness target. Kubernetes will hit this in Block 3.
    return {"status": "ok"}


@app.get("/accounts/{account_id}")
def get_account(account_id: str):
    account = ACCOUNTS.get(account_id)
    if account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    return {"account_id": account_id, **account}