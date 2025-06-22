# 🔗 Smart URL Answer Bot

A **Retrieval-Augmented Generation (RAG)**-powered chatbot that reads the content of web pages and answers natural language questions from it. This tool is ideal for researchers, journalists, analysts, or anyone who needs to extract insights quickly from multiple sources.

---

## 💼 Real-World Applications

### 📊 Financial Analysis
- Input multiple mortgage rate articles or market reports
- Instantly query: *“What was the 30-year fixed mortgage rate on August 13?”*
- Saves time compared to reading each article manually

### 📰 News Summarization
- Add URLs of multiple news articles and ask:  
  *“What are the key takeaways from today’s headlines?”*
- Great for journalists, content curators, and analysts

### 🧾 Government or Policy Research
- Scrape official sites for recent updates and ask:  
  *“What’s the latest change in taxation for real estate investors?”*

### 📚 Academic and Blog Mining
- Load multiple blogs or papers and ask:  
  *“What are the common themes in AI ethics articles?”*

### 🧠 Personal Knowledge Assistant
- Input your favorite knowledge blogs or resources  
- Get quick summaries and Q&A in plain language

> ⚡️**Automates reading + comprehension at scale** — freeing you to focus on decision-making.

---

## 🚀 Features

- 🌐 Input up to 3 URLs and extract clean content
- 🧬 Embed documents using HuggingFace GTE model
- 🔍 Ask any natural language query — get accurate answers with source references
- 📦 Vector DB (Chroma) allows fast, intelligent retrieval
- 🤖 Powered by **Groq’s LLaMA 3.3-70B** for high-quality, blazing-fast answers
- 🎨 Easy-to-use Streamlit interface

---

## 🛠️ Tech Stack

| Component         | Tool/Library                                     |
|------------------|--------------------------------------------------|
| LLM               | [Groq - LLaMA 3.3-70B Versatile](https://console.groq.com/) |
| Embeddings        | [HuggingFace - GTE Base v1.5](https://huggingface.co/Alibaba-NLP/gte-base-en-v1.5) |
| Vector DB         | [Chroma](https://www.trychroma.com/)            |
| RAG Pipeline      | [LangChain](https://www.langchain.com/)         |
| URL Parsing       | `UnstructuredURLLoader` from `langchain_community` |
| Frontend          | [Streamlit](https://streamlit.io/)              |

---

## 🧪 How It Works

1. **User provides URLs**
2. **Text is scraped and cleaned using UnstructuredURLLoader**
3. **Content is split into chunks and embedded**
4. **Vector embeddings are stored in ChromaDB**
5. **When a user asks a question**, the bot:
   - Retrieves relevant content
   - Sends it to Groq LLaMA 3.3-70B for response generation
   - Returns the answer + source links
