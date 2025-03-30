from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/echo")
def echo(state: str, fuel: str, sector: str, tone: str):
    return {"message": f"State: {state}, Fuel: {fuel}, Sector: {sector}, Tone: {tone}"}