# Conversational AI Avatar Demo

A real-time Conversational AI Avatar using **Anam.ai** (for digital human persona), **Zep Cloud** (for long-term memory & knowledge graph), and **Gemini 2.0 / OpenAI** (LLM).

This project demonstrates a split-stack architecture:
- **Frontend**: Streamlit (User Interface & Avatar Rendering)
- **Backend**: FastAPI (Orchestrates Zep, LLM, and Anam logic)

## Architecture

![Architecture](assets/architecture.gif)

1.  **Streamlit Client**: Renders the Anam video stream and handles user sessions.
2.  **FastAPI Backend**:
    *   Receives conversation history.
    *   Stores `user` messages in Zep.
    *   Retrieves context (Knowledge Graph + Memory) from Zep.
    *   Calls LLM (Gemini/OpenAI) with grounded context.
    *   Streams LLM response chunks back to frontend via SSE (Server-Sent Events).
    *   Frontend pipes these chunks to the Anam Persona for lip-synced speech.

---

## 🚀 Deployment Guide

This project is designed to be deployed as two separate services:
1.  **Backend** (FastAPI) on [Render](https://render.com)
2.  **Frontend** (Streamlit) on [Streamlit Community Cloud](https://streamlit.io/cloud)

### 1. Backend Deployment (Render)

1.  Create a new **Web Service** on Render connected to this repository.
2.  **Root Directory**: `.` (current repository root).
3.  **Build Command**:
    ```bash
    pip install .
    ```
    *OR if using uv:* `pip install uv && uv sync`
4.  **Start Command**:
    ```bash
    uvicorn backend:app --host 0.0.0.0 --port $PORT
    ```
5.  **Environment Variables**:
    Add the following variables in the Render Dashboard:

    | Variable | Value / Description |
    | :--- | :--- |
    | `ANAM_API_KEY` | Your Anam.ai API Key |
    | `ZEP_API_KEY` | Your Zep Cloud API Key |
    | `OPENROUTER_API_KEY` | Your LLM provider key (OpenRouter/Gemini) |
    | `ZEP_DOCS_USER_ID` | User ID for Zep Knowledge Graph docs |
    | `ANAM_AVATAR_ID` | `30fa96d0-26c4-4e55-94a0-517025942e18` (or your custom ID) |
    | `ANAM_VOICE_ID` | `6bfbe25a-979d-40f3-a92b-5394170af54b` (or your custom ID) |
    | `FRONTEND_URL` | Check Step 2 (e.g., `https://your-app.streamlit.app`) |

    > **Note**: After the first deployment, Render will give you a backend URL (e.g., `https://project.onrender.com`). You will need this for the Frontend.

### 2. Frontend Deployment (Streamlit Cloud)

1.  Deploy a new app on Streamlit Community Cloud using this repository.
2.  **Main file path**: `app.py`
3.  **Secrets / Environment Variables**:
    Go to **App Settings -> Secrets** and add:

    ```toml
    ZEP_API_KEY = "your_zep_key_here"
    BACKEND_URL = "https://your-project-name.onrender.com"
    ```
    *(Note: `BACKEND_URL` is the URL of your deployed Render service from Step 1)*

### 3. Final Wiring

1.  Copy your **Streamlit App URL** (e.g., `https://my-avatar-demo.streamlit.app`).
2.  Go back to your **Render Dashboard**.
3.  Update the `FRONTEND_URL` environment variable with this Streamlit URL.
4.  **Redeploy** the Release in Render.

---

## 🛠 Local Development

### Prerequisites
- Python 3.12+
- `uv` (recommended) or `pip`
- API Keys for Anam, Zep, and OpenRouter

### Setup

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/hynko431/Conversational-AI-Avatar.git
    cd Conversational-AI-Avatar
    ```

2.  **Install dependencies**:
    ```bash
    uv sync
    # OR
    pip install -r pyproject.toml
    ```

3.  **Environment Setup**:
    Copy `.env.example` to `.env` and fill in your keys:
    ```bash
    cp .env.example .env
    ```

    Ensure your `.env` for local development has:
    ```
    FRONTEND_URL=http://localhost:8501
    BACKEND_URL=http://localhost:8000
    ```

### Running Locally

1.  **Start the Backend**:
    ```bash
    uvicorn backend:app --reload --port 8000
    ```

2.  **Start the Frontend**:
    ```bash
    streamlit run app.py
    ```

3.  Open `http://localhost:8501` in your browser.

---

## License

MIT License