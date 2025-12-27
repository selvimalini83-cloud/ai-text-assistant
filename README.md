# 🤖 AI Text Assistant

This project is a **multi‑feature AI Text Assistant** built as part of my learning and career‑oriented development journey.
The goal of this project is to provide **text intelligence features** such as **Spam Detection** and **Grammar Correction**, which can later be integrated into a web or mobile application.

---

## 🎯 Project Objectives

* Detect whether a message is **Spam or Not Spam**
* Correct **grammatical mistakes** in English sentences
* Build ML models from scratch using real datasets
* Expose these models through backend APIs (future step)
* Keep the project modular and scalable

---

## 🧠 Features Implemented

### 1️⃣ Spam Detection (Primary Module)

* Classifies messages as **Spam** or **Ham (Not Spam)**
* Uses classical Machine Learning algorithms
* Trained on the **SMS Spam Collection Dataset**
* Lightweight and fast for real‑time usage

**Tech Stack:**

* Python
* Scikit‑learn
* CountVectorizer / TF‑IDF
* Naive Bayes

---

### 2️⃣ Grammar Correction (Secondary Module)

* Converts **incorrect English sentences → correct sentences**
* Uses a **Transformer‑based model (T5)**
* Trained on a custom dataset created manually

**Tech Stack:**

* Python
* PyTorch
* Hugging Face Transformers
* SentencePiece

---

## 📁 Project Structure

```
ai_text_assistant/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── ml_models/
│   ├── spam/
│   │   ├── spam_dataset.csv
│   │   ├── train_spam.py
│   │   ├── spam_model.pkl
│   │   └── vectorizer.pkl
│   │
│   └── grammar/
│       ├── grammar_dataset.csv
│       ├── train_grammar.py
│       ├── grammar_model.pkl
│       ├── grammar_vectorizer.pkl
│       └── grammar_model/   # saved transformer model
│
├── venv/
├── app.py
├── requirements.txt
└── README.md

```

---

## 📊 Dataset Details

### 🟢 Spam Detection Dataset

| Column  | Description     |
| ------- | --------------- |
| `text`  | Message content |
| `label` | spam / ham      |

Example:

```csv
label,text
spam,Win a free iPhone now!!!
ham,Are you coming to class today?
```

---

### 🟡 Grammar Correction Dataset

| Column   | Description        |
| -------- | ------------------ |
| `input`  | Incorrect sentence |
| `output` | Correct sentence   |

Example:

```csv
input,output
She go to school everyday.,She goes to school every day.
For not use car.,Do not use the car.
```

---

## 🏋️ Training Instructions

### Activate Virtual Environment

```bash
.venv\Scripts\activate
```

### Train Spam Detection Model

```bash
python train_spam.py
```

### Train Grammar Correction Model

```bash
python train_grammar.py
```

---

## 💾 Why Trained Models Are Saved

* CSV dataset = **raw knowledge**
* Trained model = **learned intelligence**
* Saved models allow:

  * Instant predictions
  * No retraining every time
  * Easy deployment

⚠️ **Do not delete trained model files**

---
## 📸 Project Screenshots

### Spam Detection Output
![Spam Detection](![alt text](image-1.png))

### Grammar Correction Output
![Grammar Correction](![alt text](image.png))

### Frontend UI
![Frontend UI](![alt text](image-2.png))

## 🚀 Future Enhancements

* REST API using Flask / Express
* Web UI for live text correction
* Combined endpoint: Spam + Grammar check
* Performance optimization
* Deployment on cloud

---

## 👩‍💻 Author

**D Selvi**
Full‑Stack & AI Developer (Learning Phase)

---

## 📌 Note

* Spam Detection is the **core module**
* Grammar Correction is an **advanced enhancement**
* Training transformer models may take time on CPU

Learning step by step 🚀
