def grade(total_reward):
    return round(max(0.0, min(1.0, total_reward)), 2)