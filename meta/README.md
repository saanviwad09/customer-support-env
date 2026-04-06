# Customer Support AI Agent (OpenEnv Environment)

## Overview

This project implements a **real-world Customer Support AI simulation environment** using the OpenEnv specification.

The environment models how an AI agent handles customer queries in a support system by:

* Understanding user complaints
* Classifying issue types
* Assigning priority levels
* Generating appropriate responses
* Deciding whether to resolve or escalate

This environment is designed to evaluate LLM agents on **practical decision-making tasks** rather than synthetic or game-based problems.

---

## Motivation

Customer support is a critical real-world workflow involving:

* Natural language understanding
* Decision-making under uncertainty
* Context awareness (history)
* Communication quality

This environment simulates these challenges in a structured and measurable way, making it ideal for evaluating AI agents.

---

## OpenEnv Interface

The environment follows the OpenEnv standard:

### Methods

* `reset()` → Returns initial observation
* `step(action)` → Returns `(observation, reward, done, info)`
* `state()` → Returns internal state

---

## Observation Space

```json
{
  "customer_query": "string",
  "customer_id": "string",
  "history": ["string"]
}
```

### Description

* **customer_query**: Current user complaint
* **customer_id**: Unique identifier
* **history**: Previous interactions or context

---

## Action Space

```json
{
  "category": "billing | technical | complaint | general",
  "priority": 1-5,
  "response": "string"
}
```

### Description

* **category**: Type of issue
* **priority**: Urgency level (1 = low, 5 = critical)
* **response**: AI-generated reply

---

## Tasks

The environment includes **3 tasks with increasing difficulty**:

### Easy Task

* Simple billing issue (e.g., double charge)
* Goal: Correct classification + basic response

### Medium Task

* Technical issue (e.g., app crash)
* Requires: Problem understanding + troubleshooting

###  Hard Task

* Customer complaint (e.g., no response from support)
* Requires: Empathy + escalation decision

---

##  Reward Function

The reward function provides **dense feedback**:

### Components

*  Category correctness → +0.3
*  Priority accuracy → +0.2
*  Response keyword match → +0.3
*  Correct solution (refund / fix / escalate) → +0.2

### Penalties

*  Step delay penalty → -0.05 × step count
*  Poor or irrelevant responses → reduced score

### Final Reward

```text
reward = max(0, partial_score - penalty)
```

---

##  Grader

Each task has a deterministic grader that:

* Compares action with ground truth
* Scores between **0.0 and 1.0**
* Evaluates semantic correctness using keywords and logic

---

##  Environment Dynamics

This is a **multi-step environment**:

1. Agent receives query
2. Takes action
3. Gets partial reward
4. Continues until max steps reached

This simulates real-world iterative decision-making.

---

##  Baseline Inference

The project includes `inference.py`, which:

* Uses OpenAI API client
* Runs agent across all tasks
* Produces reproducible score
* Uses structured JSON output

### Example Output

```text
Episode 1 Score: 0.82
Episode 2 Score: 0.76
Episode 3 Score: 0.91

Final Score: 0.83
```

---

## 🔧 Setup Instructions

### 1. Clone Repository

```bash
git clone <your-repo-url>
cd customer-support-env
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Set Environment Variables

```bash
export OPENAI_API_KEY=your_key
export API_BASE_URL=https://api.openai.com/v1
export MODEL_NAME=gpt-4o-mini
```

---

### 4. Run Inference

```bash
python inference.py
```

---

##  Docker Setup

### Build

```bash
docker build -t customer-support-env .
```

### Run

```bash
docker run -p 8000:8000 customer-support-env
```

---

##  Hugging Face Deployment

* Create a **Docker Space**
* Upload repository
* Add tag: `openenv`
* Ensure `/reset` endpoint works

---

##  Baseline Performance

| Task Difficulty | Score Range |
| --------------- | ----------- |
| Easy            | 0.8 – 1.0   |
| Medium          | 0.6 – 0.9   |
| Hard            | 0.5 – 0.8   |

**Average Score:** ~0.75–0.85

---

##  Project Structure

```
customer-support-env/
│
├── env/
│   ├── environment.py
│   ├── models.py
│   ├── grader.py
│   ├── tasks.py
│
├── inference.py
├── openenv.yaml
├── Dockerfile
├── requirements.txt
├── app.py
└── README.md
```

---

## OpenEnv Compliance Checklist

* ✔ Typed Observation / Action / Reward models
* ✔ step(), reset(), state() implemented
* ✔ 3 tasks with graders
* ✔ Reward in range [0,1]
* ✔ Baseline inference script
* ✔ Dockerized environment
* ✔ HF Space compatible

---

##  Future Improvements

* Multi-turn conversation memory
* Sentiment analysis for better grading
* Real-world dataset integration
* Advanced semantic evaluation

---

##  Conclusion

This project demonstrates a **real-world AI evaluation environment** where agents are tested on:

* Understanding natural language
* Making structured decisions
* Producing useful responses

It aligns with OpenEnv goals by focusing on **practical, measurable, and scalable AI tasks**.

---
