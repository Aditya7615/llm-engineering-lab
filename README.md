# 🧠 LLM Engineering Lab  

![Python](https://img.shields.io/badge/Python-3.10-blue)
![LangChain](https://img.shields.io/badge/LangChain-Framework-green)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

### LangChain • Groq (LLaMA 3) • Hugging Face • Streamlit • Vector Search

A comprehensive hands-on project demonstrating **modern LLM application development**, including prompt engineering, structured outputs, embeddings, and semantic search — forming the foundation of **RAG (Retrieval-Augmented Generation) systems**.

---

## 🚀 Overview

This repository is a **practical LLM engineering playground** that explores:

* 🤖 LLM interaction using Groq (LLaMA 3)
* 🧩 Prompt engineering with dynamic templates
* 📊 Structured outputs using Pydantic & TypedDict
* 📈 Embeddings and vector-based semantic search
* 🎨 Streamlit-based AI applications

---

## 🧠 What This Project Demonstrates

This project is structured to reflect **real-world LLM system design**:

### 🤖 LLM Layer

* Chat model interaction (Groq / LLaMA 3)
* Prompt engineering using LangChain
* Streamlit UI for user interaction

### 📊 Embeddings & Vector Search Layer

* Document embeddings using Hugging Face models
* Query embeddings for semantic understanding
* Cosine similarity for document retrieval

👉 These components together form the **foundation of RAG systems**

---

## 🏗️ Project Structure

```
llm-engineering-lab/
│
├── app/
│   └── app.py                      # Streamlit app (LLM interface)
│
├── notebooks/
│
│   ├── llm/
│   │   ├── llm_basics.ipynb
│   │   ├── groq_llm_demo.ipynb
│   │   └── chatbot_app.ipynb
│
│   ├── embeddings_vector/
│   │   ├── embedding_documents.ipynb
│   │   └── embedding_query.ipynb
│
├── scripts/
│
│   ├── llm/
│   │   └── app.py
│
│   ├── embeddings/
│   │   ├── document_embedding.py
│   │   ├── query_embedding.py
│   │   └── document_similarity.py
│
├── prompts/
│   ├── template.json
│   └── json_schema.json
│
├── data/
│   └── chat_history.txt
│
├── requirements.txt
├── .env.example
├── LICENSE
└── README.md
```

---

## 🛠️ Tech Stack

* **Python**
* **LangChain**
* **Groq API (LLaMA 3.3-70B)**
* **Hugging Face Embeddings**
* **Streamlit**
* **Pydantic / TypedDict**
* **Scikit-learn (cosine similarity)**

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/llm-engineering-lab.git
cd llm-engineering-lab
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Configure Environment Variables

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

### 4️⃣ Run the Application

```bash
streamlit run app/app.py
```

---

## 🧪 Modules Explained

### 📘 LLM Fundamentals

* Basic chatbot creation
* Prompt engineering with templates
* Structured outputs using TypedDict & Pydantic

---

### 📘 Embeddings & Vector Search

* Document embedding generation
* Query embedding
* Semantic similarity using cosine similarity
* Basic retrieval system

---

### 🚀 Applications

* Interactive Streamlit-based AI app
* Research paper summarization tool

---

## 🔮 Future Improvements

* 📄 PDF Upload + RAG pipeline
* 🧠 Vector database integration (FAISS / Pinecone)
* 💬 Conversational memory
* 🌐 Deployment (Streamlit Cloud / Docker)
* 🔁 Multi-model support (OpenAI, Gemini, etc.)

---

## 📸 Demo

> Add screenshots or demo video here (highly recommended)

---

## 💡 Key Learnings

* How LLMs work in real applications
* Importance of prompt design
* Structured output validation
* Embeddings and semantic search fundamentals
* Building end-to-end AI applications

---

## 👨‍💻 Author

**Aditya Goyal**
Data Science Undergraduate | AI/ML Developer | MERN Stack Developer

---

## ⭐ Support

If you find this project useful:

* ⭐ Star this repository
* 🍴 Fork it
* 🤝 Contribute

---

## 📜 License

This project is licensed under the MIT License.
