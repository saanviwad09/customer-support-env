def grade(action, task):
    score = 0.0

    # Category
    if action.category == task["category"]:
        score += 0.3

    # Priority
    if abs(action.priority - task["priority"]) <= 1:
        score += 0.2

    # Response keyword matching
    matches = sum(1 for k in task["keywords"] if k in action.response.lower())
    score += min(0.3, matches * 0.1)

    # Solution correctness
    if task["solution"] in action.response.lower():
        score += 0.2

    return min(score, 1.0)