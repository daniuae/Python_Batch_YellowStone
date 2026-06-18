# Essential AI Topics

## Introduction to AI

### What is Artificial Intelligence (AI)?

Artificial Intelligence (AI) is the field of creating systems that can perform tasks that normally require human intelligence.

### Examples

* ChatGPT answering questions
* Self-driving cars
* Face recognition
* Voice assistants (Siri, Alexa)

### Traditional Programming

```text
Input + Rules → Output
```

Example:

```python
age = 18

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
```

---

## What is Machine Learning (ML)?

Machine Learning is a subset of AI where machines learn patterns from data instead of being explicitly programmed.

### Example

Predict employee salary based on experience.

```python
from sklearn.linear_model import LinearRegression
import pandas as pd

data = pd.DataFrame({
    "experience":[1,2,3,4,5],
    "salary":[30000,40000,50000,60000,70000]
})

X = data[["experience"]]
y = data["salary"]

model = LinearRegression()
model.fit(X,y)

prediction = model.predict([[6]])

print(prediction)
```

Output:

```text
80000
```

---

## What is Deep Learning (DL)?

Deep Learning is a subset of Machine Learning that uses Neural Networks with multiple layers.

### Common Applications

* Image Recognition
* Speech Recognition
* Natural Language Processing
* Autonomous Vehicles

### Example

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential([
    Dense(10, activation='relu', input_shape=(5,)),
    Dense(1)
])

model.summary()
```

---

## What is AGI?

AGI (Artificial General Intelligence) refers to a system that can perform any intellectual task a human can perform.

### Current AI

* ChatGPT → Language Tasks
* MidJourney → Image Generation
* AlphaGo → Board Games

### AGI

A single system capable of:

* Learning medicine
* Driving a car
* Writing software
* Making business decisions

> AGI does not currently exist.

---

## AI Hierarchy

```text
Artificial Intelligence
        |
        ├── Machine Learning
        |        |
        |        └── Deep Learning
        |
        └── Generative AI
```

---

# Prompt Engineering & ChatGPT

## What is Prompt Engineering?

Prompt Engineering is the process of designing effective prompts to get better responses from AI models.

### Poor Prompt

```text
Write code
```

### Better Prompt

```text
Write a Python function that reads a CSV file using pandas and returns the average salary grouped by department.
```

---

## Components of a Good Prompt

### 1. Role

```text
Act as a Data Engineer
```

### 2. Task

```text
Generate a PySpark ETL pipeline
```

### 3. Context

```text
Source data is stored in AWS S3
```

### 4. Output Format

```text
Provide code and explanation
```

---

## Prompt Template

```text
Act as a Senior Data Engineer.

Task:
Build a PySpark ETL pipeline.

Requirements:
- Read CSV from S3
- Remove duplicates
- Handle null values
- Write to Parquet

Output:
Provide complete code.
```

---

# ChatGPT Use Cases

## 1. Code Generation

Prompt:

```text
Generate a Python function to remove duplicates from a dataframe.
```

Code:

```python
def remove_duplicates(df):
    return df.drop_duplicates()
```

---

## 2. SQL Generation

Prompt:

```text
Write SQL to find top 5 salaries.
```

Output:

```sql
SELECT *
FROM employees
ORDER BY salary DESC
LIMIT 5;
```

---

## 3. Documentation Generation

Prompt:

```text
Create documentation for a REST API.
```

---

## 4. Unit Test Generation

Prompt:

```text
Generate unit tests for this Python function.
```

---

## 5. Data Analysis

### Load Dataset

```python
import pandas as pd

df = pd.read_csv("employees.csv")
```

### Basic Analysis

```python
print(df.describe())
```

```python
print(df.groupby("department")["salary"].mean())
```

---

# AI for Data Analysis

### Sample Dataset

```python
import pandas as pd

data = {
    "department":["IT","IT","HR","HR"],
    "salary":[70000,80000,50000,60000]
}

df = pd.DataFrame(data)
```

### Analysis

```python
avg_salary = df.groupby("department")["salary"].mean()

print(avg_salary)
```

Output:

```text
HR    55000
IT    75000
```

---

# Building Generative AI Applications

## Typical Architecture

```text
User
 |
Web Application
 |
LLM (OpenAI/Gemini/Claude)
 |
Response
```

---

## Building a Simple AI Application

### Installation

```bash
pip install openai
```

### Example

```python
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role":"user",
            "content":"Explain Machine Learning"
        }
    ]
)

print(response.choices[0].message.content)
```

---

# Building a Document Q&A Application

## Workflow

```text
PDF
 |
Chunking
 |
Embeddings
 |
Vector Database
 |
LLM
 |
Answer
```

---

## Embedding Example

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    'all-MiniLM-L6-v2'
)

embeddings = model.encode([
    "AI is transforming the world"
])

print(embeddings.shape)
```

---

# Retrieval-Augmented Generation (RAG)

## Why RAG?

### Without RAG

```text
LLM answers only from training data.
```

### With RAG

```text
LLM + Enterprise Documents
```

---

## RAG Workflow

```text
Question
   |
Embedding
   |
Vector Search
   |
Relevant Documents
   |
LLM
   |
Answer
```

---

## Simple Vector Search Example

```python
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    'all-MiniLM-L6-v2'
)

documents = [
    "Python is a programming language",
    "Spark is used for big data processing"
]

doc_vectors = model.encode(documents)

query = "What is Spark?"

query_vector = model.encode([query])

similarity = cosine_similarity(
    query_vector,
    doc_vectors
)

print(similarity)
```

---

# Generative AI Application Lifecycle

```text
Idea
 |
Prototype
 |
Prompt Design
 |
Evaluation
 |
Deployment
 |
Monitoring
```

---

# Deployment Options

## Flask

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "AI App Running"

app.run()
```

---

## Streamlit

```python
import streamlit as st

st.title("AI Chatbot")

question = st.text_input("Ask Question")

if question:
    st.write("Processing...")
```

Run:

```bash
streamlit run app.py
```

---

# Evaluation Techniques for NLP Models

Evaluating AI models is critical before deployment.

---

## 1. Accuracy

```python
from sklearn.metrics import accuracy_score

actual = [1,1,0,1]
predicted = [1,1,0,0]

accuracy = accuracy_score(
    actual,
    predicted
)

print(accuracy)
```

---

## 2. Precision

```python
from sklearn.metrics import precision_score

precision = precision_score(
    actual,
    predicted
)

print(precision)
```

---

## 3. Recall

```python
from sklearn.metrics import recall_score

recall = recall_score(
    actual,
    predicted
)

print(recall)
```

---

## 4. F1 Score

```python
from sklearn.metrics import f1_score

f1 = f1_score(
    actual,
    predicted
)

print(f1)
```

---

## 5. BLEU Score

Used for Machine Translation Evaluation.

```python
from nltk.translate.bleu_score import sentence_bleu

reference = [
    ['the','cat','is','on','the','mat']
]

candidate = [
    'the','cat','sat','on','the','mat'
]

score = sentence_bleu(
    reference,
    candidate
)

print(score)
```

---

## 6. ROUGE Score

Used for Summarization Evaluation.

```python
from rouge import Rouge

rouge = Rouge()

scores = rouge.get_scores(
    "AI is transforming industries",
    "AI transforms industries"
)

print(scores)
```

---

## 7. Perplexity

Measures how confidently a language model predicts text.

Formula:

```text
Perplexity = exp(Cross Entropy)
```

Lower values indicate better performance.

---

## 8. Human Evaluation

Humans evaluate:

* Accuracy
* Relevance
* Fluency
* Helpfulness
* Hallucinations

### Sample Rubric

| Score | Meaning   |
| ----- | --------- |
| 1     | Poor      |
| 2     | Fair      |
| 3     | Good      |
| 4     | Very Good |
| 5     | Excellent |

---

# LLM Evaluation Framework Example

```python
evaluation = {
    "relevance":4,
    "accuracy":5,
    "hallucination":1,
    "fluency":5
}

overall_score = sum(
    evaluation.values()
)/len(evaluation)

print(overall_score)
```

---

# End-to-End Generative AI Mini Project

## AI Resume Analyzer

### Features

* Upload Resume
* Extract Text
* Generate Summary
* Skill Matching
* Candidate Scoring

### Technology Stack

```text
Python
OpenAI API
Pandas
Streamlit
FAISS
LangChain
```

### Workflow

```text
Resume PDF
    |
Text Extraction
    |
Prompt Engineering
    |
GPT
    |
Summary + Score
```

---

# Key Takeaways

| Topic              | Key Concept                                 |
| ------------------ | ------------------------------------------- |
| AI                 | Machines performing intelligent tasks       |
| ML                 | Learning patterns from data                 |
| DL                 | Neural Networks and representation learning |
| AGI                | Human-level intelligence                    |
| Prompt Engineering | Designing effective prompts                 |
| ChatGPT            | Large Language Model (LLM)                  |
| Generative AI      | AI that creates content                     |
| RAG                | LLM + External Knowledge                    |
| NLP Evaluation     | Accuracy, Precision, Recall, BLEU, ROUGE    |
| Deployment         | Flask, Streamlit, APIs                      |

---

## Recommended Learning Path

```text
AI Fundamentals
        ↓
Machine Learning
        ↓
Deep Learning
        ↓
Prompt Engineering
        ↓
ChatGPT for Data Analysis
        ↓
Embeddings
        ↓
Vector Databases
        ↓
RAG Applications
        ↓
LLM Evaluation
        ↓
Deployment & Monitoring
```
