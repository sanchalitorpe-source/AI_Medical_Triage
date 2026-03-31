CASES = [
    # 🔴 EMERGENCY
    {
        "initial_symptoms": ["chest pain"],
        "followup_info": ["shortness of breath"],
        "duration": "30 minutes",
        "age": 55,
        "history": ["hypertension"],
        "correct_severity": "emergency",
        "correct_action": "go_to_er"
    },
    {
        "initial_symptoms": ["severe headache"],
        "followup_info": ["loss of vision"],
        "duration": "2 hours",
        "age": 60,
        "history": ["diabetes"],
        "correct_severity": "emergency",
        "correct_action": "go_to_er"
    },
    {
        "initial_symptoms": ["abdominal pain"],
        "followup_info": ["rigid abdomen"],
        "duration": "5 hours",
        "age": 40,
        "history": [],
        "correct_severity": "emergency",
        "correct_action": "go_to_er"
    },
    # 🟠 HIGH
    {
        "initial_symptoms": ["headache"],
        "followup_info": ["blurred vision"],
        "duration": "1 day",
        "age": 45,
        "history": [],
        "correct_severity": "high",
        "correct_action": "urgent_care"
    },
    {
        "initial_symptoms": ["fever"],
        "followup_info": ["rash"],
        "duration": "3 days",
        "age": 35,
        "history": [],
        "correct_severity": "high",
        "correct_action": "urgent_care"
    },
    {
        "initial_symptoms": ["shortness of breath"],
        "followup_info": ["worsening at rest"],
        "duration": "1 day",
        "age": 50,
        "history": ["smoking"],
        "correct_severity": "high",
        "correct_action": "urgent_care"
    },
    # 🟡 MEDIUM
    {
        "initial_symptoms": ["vomiting"],
        "followup_info": ["dehydration"],
        "duration": "1 day",
        "age": 30,
        "history": [],
        "correct_severity": "medium",
        "correct_action": "visit_doctor"
    },
    {
        "initial_symptoms": ["back pain"],
        "followup_info": ["difficulty moving"],
        "duration": "2 days",
        "age": 40,
        "history": [],
        "correct_severity": "medium",
        "correct_action": "visit_doctor"
    },
    {
        "initial_symptoms": ["fever"],
        "followup_info": ["persistent cough"],
        "duration": "4 days",
        "age": 28,
        "history": [],
        "correct_severity": "medium",
        "correct_action": "visit_doctor"
    },
    # 🟢 LOW
    {
        "initial_symptoms": ["fever"],
        "followup_info": ["cough"],
        "duration": "2 days",
        "age": 25,
        "history": [],
        "correct_severity": "low",
        "correct_action": "self_care"
    },
    {
        "initial_symptoms": ["minor cut"],
        "followup_info": [],
        "duration": "1 hour",
        "age": 20,
        "history": [],
        "correct_severity": "low",
        "correct_action": "self_care"
    },
    {
        "initial_symptoms": ["runny nose"],
        "followup_info": ["sneezing"],
        "duration": "1 day",
        "age": 22,
        "history": [],
        "correct_severity": "low",
        "correct_action": "self_care"
    },
    # ⚖️ TRICKY
    {
        "initial_symptoms": ["fatigue"],
        "followup_info": ["weight loss"],
        "duration": "2 weeks",
        "age": 50,
        "history": ["diabetes"],
        "correct_severity": "high",
        "correct_action": "urgent_care"
    },
    {
        "initial_symptoms": ["mild chest pain"],
        "followup_info": ["pain during movement"],
        "duration": "1 day",
        "age": 25,
        "history": [],
        "correct_severity": "medium",
        "correct_action": "visit_doctor"
    },
    {
        "initial_symptoms": ["dizziness"],
        "followup_info": ["fainting"],
        "duration": "3 hours",
        "age": 65,
        "history": ["hypertension"],
        "correct_severity": "high",
        "correct_action": "urgent_care"
    }
]

TASKS = [
    {
        "id": "easy",
        "name": "Basic Triage",
        "description": "Classify severity and action for simple, obvious symptom cases.",
        "difficulty": "easy",
        "objective": "Correctly identify severity and recommend appropriate action in straightforward scenarios.",
        "evaluation": {
            "criteria": ["Correct severity classification", "Correct action recommendation"],
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
            "criteria": ["Correct interpretation of risk factors", "Appropriate escalation level"],
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
            "scoring": "Higher reward for correct updates. Heavy penalty for underestimation."
        }
    }
]