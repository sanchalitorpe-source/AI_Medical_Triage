TASKS = [
    {
        "id": "easy",
        "name": "Basic Triage",
        "description": "Classify severity and action for simple, obvious symptom cases.",
        "difficulty": "easy",
        "objective": "Correctly identify severity and recommend appropriate action in straightforward scenarios.",
        "evaluation": {
            "criteria": [
                "Correct severity classification",
                "Correct action recommendation"
            ],
            "scoring": "Full score for exact match. Partial score if only severity is correct."
        }
    },
    {
        "id": "medium",
        "name": "Conflicting Symptoms",
        "description": "Handle cases with mixed or ambiguous signals requiring reasoning.",
        "difficulty": "medium",
        "objective": "Balance symptoms, duration, and patient history to make a safe decision.",
        "evaluation": {
            "criteria": [
                "Correct interpretation of risk factors",
                "Appropriate escalation level"
            ],
            "scoring": "Partial credit for safe but suboptimal decisions."
        }
    },
    {
        "id": "hard",
        "name": "Multi-Step Critical Reasoning",
        "description": "Update decisions after receiving additional clinical information.",
        "difficulty": "hard",
        "objective": "Refine initial triage decision using new information across steps.",
        "evaluation": {
            "criteria": [
                "Improvement from initial to final decision",
                "Correct final severity and action",
                "Avoiding dangerous underestimation"
            ],
            "scoring": "Higher reward for correct updates and safe final decisions. Heavy penalty for underestimation."
        }
    }
]