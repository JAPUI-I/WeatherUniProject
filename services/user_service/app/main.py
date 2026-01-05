from fastapi import FastAPI

app = FastAPI(title="User Service")

@app.get("/health")
async def healthcheck():
    return {"status": "ok"}
