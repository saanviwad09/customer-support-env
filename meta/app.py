from fastapi import FastAPI
from env.environment import CustomerSupportEnv

app = FastAPI()
env = CustomerSupportEnv()

@app.get("/reset")
@app.post("/reset")
def reset():
    obs = env.reset()
    return obs.dict()
