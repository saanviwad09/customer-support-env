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

def main():
    return app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)
