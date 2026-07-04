from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "RED FLAG is FLAGGING AS HELL"}

@app.get("/health")
async def check():
    return {"status" : "HEALTH is HEALTHY"}