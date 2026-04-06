from fastapi import FastAPI
from env.environment import CustomerSupportEnv

app = FastAPI()
env = CustomerSupportEnv()

@app.post("/reset")
@app.get("/reset")
def reset():
    obs = env.reset()
    return obs.dict()
