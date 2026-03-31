def grade(total_reward: float) -> float:
    """
    Convert raw reward into a normalized score (0.0 to 1.0)
    """
    MIN_REWARD = -1.0
    MAX_REWARD = 1.0

    normalized = (total_reward - MIN_REWARD) / (MAX_REWARD - MIN_REWARD)
    return round(max(0.0, min(1.0, normalized)), 2)