from fastapi import FastAPI
from env.environment import CustomerSupportEnv

app = FastAPI()
env = CustomerSupportEnv()

@app.post("/reset")
def reset():
    obs = env.reset()
    return obs.dict()

@app.get("/")
def home():
    return {"status": "running"}

# 🔥 REQUIRED by OpenEnv
def main():
    return app
