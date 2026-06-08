# Essential AI Topics

## Introduction to AI, Prompt Engineering, ChatGPT, Generative AI Applications, and NLP Evaluation

---

# Table of Contents

1. Introduction to AI
2. Artificial Intelligence (AI)
3. Machine Learning (ML)
4. Deep Learning (DL)
5. Artificial General Intelligence (AGI)
6. AI vs ML vs DL vs AGI
7. Prompt Engineering
8. ChatGPT Fundamentals
9. ChatGPT Use Cases
10. Building Generative AI Applications
11. OpenAI API Integration
12. Retrieval Augmented Generation (RAG)
13. Deploying AI Applications
14. NLP Evaluation Techniques
15. End-to-End AI Project
16. Interview Questions
17. Best Practices

---

# 1. Introduction to AI

Artificial Intelligence (AI) is the simulation of human intelligence by machines.

AI systems can:

* Learn
* Reason
* Solve Problems
* Understand Language
* Recognize Images
* Make Decisions

## Real-World Examples

| Application            | Example         |
| ---------------------- | --------------- |
| Chatbots               | ChatGPT         |
| Voice Assistants       | Siri, Alexa     |
| Recommendation Systems | Netflix         |
| Navigation             | Google Maps     |
| Fraud Detection        | Banking Systems |
| Self Driving Cars      | Tesla           |

---

# 2. Artificial Intelligence (AI)

AI is the broad field focused on building intelligent machines.

## Types of AI

### Narrow AI

Designed for specific tasks.

Examples:

* ChatGPT
* Siri
* Alexa
* Google Translate

### General AI (AGI)

Can perform any intellectual task that humans can perform.

Currently not achieved.

### Super AI

Surpasses human intelligence.

Still theoretical.

---

## Basic AI Example

```python
age = 20

if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible")
```

Output:

```text
Eligible to Vote
```

---

# 3. Machine Learning (ML)

Machine Learning is a subset of AI where systems learn patterns from data.

## Traditional Programming

```text
Data + Rules
      ↓
   Output
```

## Machine Learning

```text
Data + Output
      ↓
 Model Learns Rules
```

---

## House Price Prediction Example

```python
from sklearn.linear_model import LinearRegression
import numpy as np

area = np.array([1000, 1500, 2000, 2500]).reshape(-1,1)
price = [20, 30, 40, 50]

model = LinearRegression()
model.fit(area, price)

prediction = model.predict([[1800]])

print(prediction)
```

Output:

```text
[36.]
```

---

# 4. Deep Learning (DL)

Deep Learning is a subset of Machine Learning that uses Artificial Neural Networks.

## Applications

* Image Recognition
* Speech Recognition
* NLP
* Autonomous Vehicles
* Medical Diagnosis
* Generative AI

---

## Neural Network Example

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential()

model.add(Dense(10, input_dim=5, activation='relu'))
model.add(Dense(1))

model.compile(
    optimizer='adam',
    loss='mse'
)

print(model.summary())
```

---

# 5. Artificial General Intelligence (AGI)

AGI refers to a machine capable of performing any intellectual task a human can perform.

Characteristics:

* Learning
* Reasoning
* Planning
* Creativity
* Adaptability

Current AI systems are not AGI.

---

# 6. AI vs ML vs DL vs AGI

| Feature                  | AI        | ML        | DL  | AGI      |
| ------------------------ | --------- | --------- | --- | -------- |
| Broad Field              | Yes       | No        | No  | No       |
| Learns from Data         | Sometimes | Yes       | Yes | Yes      |
| Neural Networks          | Optional  | Sometimes | Yes | Advanced |
| Human-Level Intelligence | No        | No        | No  | Yes      |

---

# 7. Prompt Engineering

## What is Prompt Engineering?

Prompt Engineering is the process of designing instructions that help AI generate better responses.

---

## Poor Prompt

```text
Write Python code.
```

## Better Prompt

```text
Act as a Senior Python Developer.

Write a Python function to reverse a string.

Requirements:
1. Use slicing
2. Explain the code
3. Show example input/output
```

---

## Components of a Good Prompt

### Role

```text
Act as a Data Scientist
```

### Task

```text
Analyze customer churn data
```

### Context

```text
Telecom company with 2 million customers
```

### Output Format

```text
Provide results in Markdown table format
```

---

## Prompt Template

```text
Act as a Senior Data Engineer.

Task:
Analyze sales data.

Requirements:
1. Data Cleaning
2. Exploratory Analysis
3. Visualizations
4. Business Insights

Output:
Provide Python code and explanation.
```

---

# 8. ChatGPT Fundamentals

ChatGPT is a Large Language Model (LLM).

Capabilities:

* Question Answering
* Summarization
* Coding
* Translation
* Data Analysis
* Content Generation

---

# 9. ChatGPT Use Cases for Data Analysis

## SQL Generation

Prompt:

```text
Generate SQL to find top 10 customers by sales.
```

Output:

```sql
SELECT customer_id,
       SUM(amount) AS total_sales
FROM sales
GROUP BY customer_id
ORDER BY total_sales DESC
LIMIT 10;
```

---

## Data Analysis with Pandas

```python
import pandas as pd

df = pd.read_csv("sales.csv")

print(df.head())
print(df.describe())
```

---

## Data Cleaning

```python
df.drop_duplicates(inplace=True)

df.fillna(0, inplace=True)
```

---

## Feature Engineering

```python
df["profit_margin"] = (
    df["profit"] / df["sales"]
) * 100
```

---

## Visualization

```python
import matplotlib.pyplot as plt

df.groupby("region")["sales"].sum().plot(kind="bar")

plt.show()
```

---

## Report Generation

Prompt:

```text
Generate executive summary for quarterly sales report.
```

Output:

```text
Sales increased by 12%.
South region contributed 40% of total revenue.
```

---

# 10. Building Generative AI Applications

## Architecture

```text
User
 ↓
Frontend
 ↓
Backend API
 ↓
LLM
 ↓
Response
```

---

## Components

1. Frontend
2. Backend
3. LLM
4. Database
5. Monitoring

---

# OpenAI API Example

Install SDK:

```bash
pip install openai
```

---

## Basic Chatbot

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY"
)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role":"user",
            "content":"Explain AI"
        }
    ]
)

print(
    response.choices[0].message.content
)
```

---

# 11. Retrieval Augmented Generation (RAG)

RAG combines:

```text
LLM
+
External Knowledge
```

---

## RAG Workflow

```text
User Query
      ↓
Vector Database
      ↓
Relevant Documents
      ↓
LLM
      ↓
Response
```

---

## Popular Tools

* LangChain
* LlamaIndex
* Pinecone
* ChromaDB
* FAISS

---

## FAISS Example

```python
from langchain.vectorstores import FAISS

vector_db = FAISS.from_texts(
    texts,
    embeddings
)

results = vector_db.similarity_search(
    "What is AI?"
)

print(results)
```

---

# 12. Deploying AI Applications

## Streamlit Deployment

Install:

```bash
pip install streamlit
```

Application:

```python
import streamlit as st

st.title("AI Assistant")

question = st.text_input(
    "Ask a Question"
)

if question:
    st.write("Response generated here")
```

Run:

```bash
streamlit run app.py
```

---

## FastAPI Deployment

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message":"AI API Running"
    }
```

Run:

```bash
uvicorn app:app --reload
```

---

# 13. NLP Evaluation Techniques

Evaluation helps measure model quality.

---

## Accuracy

Formula:

Accuracy = Correct Predictions / Total Predictions

```python
from sklearn.metrics import accuracy_score

actual = [1,0,1,1]
pred = [1,0,1,0]

print(
    accuracy_score(actual,pred)
)
```

---

## Precision

```python
from sklearn.metrics import precision_score

precision_score(actual,pred)
```

---

## Recall

```python
from sklearn.metrics import recall_score

recall_score(actual,pred)
```

---

## F1 Score

```python
from sklearn.metrics import f1_score

f1_score(actual,pred)
```

---

## Confusion Matrix

```python
from sklearn.metrics import confusion_matrix

print(
    confusion_matrix(actual,pred)
)
```

---

## BLEU Score

Used in Machine Translation.

```python
from nltk.translate.bleu_score import sentence_bleu

reference = [['this','is','good']]
candidate = ['this','is','good']

score = sentence_bleu(
    reference,
    candidate
)

print(score)
```

---

## ROUGE Score

Used in Summarization.

```python
from rouge_score import rouge_scorer

scorer = rouge_scorer.RougeScorer(
    ['rouge1']
)

scores = scorer.score(
    "AI is powerful",
    "AI is very powerful"
)

print(scores)
```

---

## Perplexity

Measures uncertainty of language models.

```text
Lower Perplexity = Better Model
```

---

## Human Evaluation Metrics

* Fluency
* Relevance
* Accuracy
* Helpfulness
* Safety

---

# 14. End-to-End Generative AI Project

## AI Resume Analyzer

### Features

* Resume Upload
* Text Extraction
* Skill Identification
* Job Matching
* Recommendation Generation

---

## Technology Stack

```text
Frontend:
Streamlit

Backend:
Python

AI:
OpenAI API

Database:
PostgreSQL

Deployment:
Docker
```

---

## Project Workflow

```text
Resume Upload
      ↓
Text Extraction
      ↓
Skill Detection
      ↓
Job Matching
      ↓
AI Recommendations
      ↓
Final Report
```

---

# 15. Interview Questions

## Basic

1. What is AI?
2. What is Machine Learning?
3. What is Deep Learning?
4. What is AGI?
5. What is Prompt Engineering?

## Intermediate

6. What is RAG?
7. What are embeddings?
8. What is a vector database?
9. Explain BLEU and ROUGE.
10. How do you evaluate NLP models?

## Advanced

11. Explain Hallucination.
12. How do you reduce hallucinations?
13. Explain Fine-Tuning.
14. Explain RLHF.
15. Explain Agentic AI.

---

# 16. Best Practices

## Prompt Engineering

* Provide Context
* Define Role
* Specify Output Format
* Use Examples

## Generative AI Development

* Use RAG
* Validate Responses
* Log Interactions
* Monitor Costs
* Evaluate Performance
* Protect Sensitive Data

---

# Learning Roadmap

## Week 1

* AI Fundamentals
* ML Basics
* Prompt Engineering

## Week 2

* ChatGPT
* OpenAI APIs
* Embeddings

## Week 3

* LangChain
* RAG
* Vector Databases

## Week 4

* AI Application Development
* Deployment
* NLP Evaluation

## Week 5

* Capstone Project
* Interview Preparation

---

# Summary

This guide covered:

* Artificial Intelligence (AI)
* Machine Learning (ML)
* Deep Learning (DL)
* Artificial General Intelligence (AGI)
* Prompt Engineering
* ChatGPT for Data Analysis
* Generative AI Application Development
* Retrieval Augmented Generation (RAG)
* Deployment using Streamlit and FastAPI
* NLP Evaluation Metrics
* End-to-End AI Project Development
* Interview Preparation
