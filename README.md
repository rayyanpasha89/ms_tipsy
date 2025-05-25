# Ms Tipsy – AI School Assistant

Ms Tipsy is an open-source AI chatbot to answer questions about Indian public schools (admissions, fees, timings, etc.) in English and Kannada.

## Features

- Uses your own large language model (like Mistral-7B) via llama.cpp
- FastAPI Python backend
- Modern, responsive chat interface
- Easy to extend for new school domains

## Quick Start

### 1. Requirements

- Python 3.8+
- Your model file (e.g., mistral-7b-instruct-v0.1.Q4_K_M.gguf)
- llama.cpp compiled (https://github.com/ggerganov/llama.cpp)
- [Optional] Node.js (for advanced frontend dev)

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 3. Place your model and llama.cpp

- Place your model file in `model/`
- Compile llama.cpp and put the `llama-cli` binary in `llama.cpp/build/bin/`

### 4. Start the backend server

```bash
uvicorn app:app --reload
```

This starts your FastAPI backend at `http://localhost:8000`.

### 5. Open the frontend

- Open `frontend/index.html` directly in your browser
  - or serve `frontend/` with any static web server

### 6. Chat!

- Ask questions about admissions, fees, timings, and more—Ms Tipsy will answer using your AI model!

---

## Configuration

- To change your model or binary path, edit `MODEL_PATH` and `LLAMA_CLI` in `rag_engine.py`.

## For Production

- Use a production server for FastAPI (e.g., gunicorn with uvicorn workers)
- Restrict CORS in `app.py` to your domain
- Serve `frontend/` using a secure HTTPS web server

## License

MIT