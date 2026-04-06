from fastapi import FastAPI
from env.environment import CustomerSupportEnv

def main():
    app = FastAPI()
    env = CustomerSupportEnv()

    @app.post("/reset")
    def reset():
        obs = env.reset()
        return obs.dict()

    @app.get("/")
    def home():
        return {"status": "running"}

    return app

# expose app
app = main()
