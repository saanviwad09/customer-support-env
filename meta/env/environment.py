from env.models import Observation, Action
from env.tasks import TASKS
from env.grader import grade

class CustomerSupportEnv:
    def __init__(self):
        self.task = None
        self.step_count = 0
        self.max_steps = 4

    def reset(self):
        import random
        self.task = random.choice(TASKS)
        self.step_count = 0
        history=self.task["history"] 

        return Observation(
            customer_query=self.task["query"],
            customer_id="CUST123",
            history=self.task["history"] 
        )

    def step(self, action: Action):
        self.step_count += 1

        partial_reward = grade(action, self.task)

        # Penalize useless steps
        penalty = 0.05 * self.step_count

        reward = max(0, partial_reward - penalty)

        done = self.step_count >= self.max_steps

        return self._get_obs(), reward, done, {}

    def _get_obs(self):
        return Observation(
            customer_query=self.task["query"],
            customer_id="CUST123",
            history=self.task["history"] 
        )

    def state(self):
        return {
            "task": self.task,
            "step": self.step_count
        }