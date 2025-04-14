import os
import json

def save_user_plan(username, plan):
    os.makedirs("plans", exist_ok=True)
    with open(f"plans/{username}_plan.json", "w") as f:
        json.dump(plan, f, indent=4)

def load_user_plan(username):
    try:
        with open(f"plans/{username}_plan.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None
