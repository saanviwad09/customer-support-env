import os
from env.environment import CustomerSupportEnv
from env.models import Action

env = CustomerSupportEnv()

def get_action(observation):
    query = observation.customer_query.lower()

    if "charge" in query:
        return Action(
            category="billing",
            priority=4,
            response="We apologize for the double charge. A refund will be processed."
        )
    elif "crash" in query:
        return Action(
            category="technical",
            priority=5,
            response="Please update or reinstall the app to fix the issue."
        )
    elif "no response" in query:
        return Action(
            category="complaint",
            priority=5,
            response="We are sorry for the delay. Your issue is being escalated."
        )
    else:
        return Action(
            category="general",
            priority=2,
            response="We will assist you shortly."
        )

def run():
    total_score = 0
    num_episodes = 3

    for episode in range(num_episodes):
        print(f"\n🔹 Episode {episode + 1}")

        obs = env.reset()
        done = False
        episode_reward = 0
        step_count = 0

        while not done:
            step_count += 1

            print(f"\nStep {step_count}")
            print("Query:", obs.customer_query)

            action = get_action(obs)
            print("Action:", action)

            obs, reward, done, _ = env.step(action)
            print("Reward:", reward)

            episode_reward += reward

        normalized_score = episode_reward / 4
        print(f"Episode Score: {normalized_score:.3f}")

        total_score += normalized_score

    final_score = total_score / num_episodes

    
    print(f"FINAL SCORE: {final_score:.3f}")
    

    return final_score

if __name__ == "__main__":
    run()