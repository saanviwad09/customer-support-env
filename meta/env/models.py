from pydantic import BaseModel

class Observation(BaseModel):
    customer_query: str
    customer_id: str
    history: list[str]

class Action(BaseModel):
    category: str        # billing / technical / complaint / general
    priority: int        # 1 (low) to 5 (urgent)
    response: str        # generated reply

class Reward(BaseModel):
    score: float