# 🧑‍💻 User-Persona-Builder

This project **scrapes posts and comments from a user's Reddit profile** to **automatically generate a persona for them**.

The repository contains results from **two different approaches**:

- `kojied.txt`: Created by `scraper.py` using **offline LLM (Ollama's Phi model)**.
- `Hungry-Move-6603.txt`: Created by `scraper_api.py` using **Gemini API**.

---

## 🚀 Features

✅ Scrapes **posts and comments** from **any Reddit user** (public data).  
✅ **Chunking + Embeddings + RetrievalQA** to generate structured persona.  
✅ **Two options to run:**
- **Offline** using Ollama (Phi).
- **Online** using Gemini API.

---

## 🛠️ Methods

### 1️⃣ Using Ollama's Phi Model (Offline)

**File:** `scraper.py`

#### Steps:

1. **Install Ollama** from [official website](https://ollama.com/) and **launch it**.
2. Pull the Phi model by running:
   ```bash
   ollama pull phi
