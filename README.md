# 🩺 Clinical Triage Decision Environment (OpenEnv)

## 🚀 Overview

This project implements a **deterministic reinforcement learning environment** that simulates real-world **clinical triage decision-making**.

The agent is tasked with:

* Assessing patient symptoms
* Determining severity level
* Recommending the appropriate next action

⚠️ This is **NOT a medical diagnosis system**.
It is a structured simulation designed for **safe and testable decision-making**.

---

## 🎯 Objective

Given patient data, the agent must:

1. Classify **severity**:

   * low
   * medium
   * high
   * emergency

2. Recommend **next action**:

   * self_care
   * visit_doctor
   * urgent_care
   * go_to_er

---

## 🧠 Environment Design

### 🔁 Multi-Step Interaction

This environment supports **multi-step reasoning**:

* **Step 1:** Initial decision based on symptoms
* **Step 2:** Additional clinical information revealed
* **Step 3:** Final refined decision

This mimics real-world triage workflows.

---

## 📥 Observation Space

```json
{
  "symptoms": ["chest pain"],
  "duration": "30 minutes",
  "age": 55,
  "history": ["hypertension"],
  "step": 1
}
```

---

## 🎮 Action Space

```json
{
  "severity": "emergency",
  "action": "go_to_er"
}
```

---

## 🧩 Tasks

### 🟢 Easy — Basic Triage

* Clear and obvious symptoms
* Direct mapping to severity and action

### 🟡 Medium — Conflicting Signals

* Mixed symptoms and patient history
* Requires contextual reasoning

### 🔴 Hard — Multi-Step Critical Reasoning

* Evolving symptoms across steps
* Requires updating decisions
* Penalizes unsafe underestimation

---

## 🏆 Reward Design

| Component                | Reward |
| ------------------------ | ------ |
| Correct severity         | +0.4   |
| Correct action           | +0.4   |
| Early correct guess      | +0.1   |
| Improvement after update | +0.2   |
| Underestimation          | -0.6   |
| Overestimation           | -0.2   |

👉 Emphasis is placed on **safety and risk-aware decisions**.

---

## 🧪 Grading

Final score is normalized to **0.0 – 1.0**:

* 1.0 → Perfect decision
* 0.7 → Partially correct
* 0.3 → Risky decision
* 0.0 → Unsafe outcome

---

## 🤖 Baseline Agent

A simple rule-based agent is provided:

* Uses symptom matching
* Updates decisions after new information
* Demonstrates partial reasoning capability

---

## ⚙️ Setup & Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run API

```bash
uvicorn app.main:app --reload --port 7860
```

### 3. Open API docs

```
http://localhost:7860/docs
```

---

## 🐳 Docker

```bash
docker build -t triage-env .
docker run -p 7860:7860 triage-env
```

---

## 📊 Baseline Score

Typical baseline performance:

```
~0.55 – 0.70
```

---

## 🌍 Motivation

Clinical triage is a **high-stakes decision-making process** where:

* Underestimating severity can be dangerous
* Overestimating leads to resource misuse

This environment captures these trade-offs in a **safe, deterministic framework**.

---

## ✅ Key Features

* Deterministic and fully testable
* Multi-step reasoning environment
* Risk-sensitive reward design
* Real-world inspired task simulation
* OpenEnv compliant

---

## 🏁 Conclusion

This project demonstrates how reinforcement learning environments can model **real-world decision-making systems** while remaining:

* Safe
* Interpretable
* Evaluatable

---
