# 🚀 AI Excuse Generator

A full-stack web application that generates professional, believable excuses using AI. Built with FastAPI, Docker, and Ollama.

![AI Excuse Generator](https://img.shields.io/badge/AI-Powered-blue) 
![Python](https://img.shields.io/badge/Python-3.9+-green)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)

## ✨ Features

- **🤖 AI-Powered**: Uses LLaMA2 model via Ollama for intelligent excuse generation
- **🎯 7 Response Modes**: Professional, Funny, Serious, Creative, Formal, Casual, Dramatic
- **🐳 Dockerized**: Easy setup with Docker Compose
- **⚡ FastAPI Backend**: High-performance Python backend
- **🎨 Modern Frontend**: Clean, responsive HTML/CSS/JS interface
- **🔧 RESTful API**: Well-structured endpoints

## 🛠️ Tech Stack

- **Backend**: Python, FastAPI, Uvicorn
- **Frontend**: HTML5, CSS3, JavaScript
- **AI**: Ollama(LLM integration), LLaMA2 model
- **Containerization**: Docker, Docker Compose
- **Development**: Git, GitHub

## 🚀 Local Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/manalrhoni/ai-excuse-generator.git
   cd ai-excuse-generator
   ```

2. **Install dependencies**:
   - Install [Docker Desktop](https://docker.com)
   - Install [Ollama](https://ollama.ai)
   - Pull the AI model:
     ```bash
     ollama pull llama2
     ```

3. **Run the application**:
   ```bash
   docker-compose up
   ```

4. **Open your browser**:
   Navigate to `http://localhost:8080`

## 📁 Project Structure

```
ai-excuse-generator/
├── app/
│   ├── main.py          # FastAPI backend
│   ├── requirements.txt # Python dependencies
│   └── Dockerfile       # Backend container setup
├── frontend/
│   └── index.html       # Web interface
├── docker-compose.yml   # Multi-container setup
└── README.md           # This file
```

## 🎯 Usage

1. Enter your situation (e.g., "late for work")
2. Select a response mode (Professional, Funny, etc.)
3. Click "Generate Excuse"
4. Get your AI-powered excuse!

## 🌟 API Endpoints

- `POST /excuse` - Generate an excuse
- `GET /` - Health check endpoint

Example request:
```json
{
  "situation": "late for meeting",
  "mode": "professional"
}
```

## 👨‍💻 Developer

**Manal Rhoni**  
- GitHub: [@manalrhoni](https://github.com/manalrhoni)
- Project: [AI Excuse Generator](https://github.com/manalrhoni/ai-excuse-generator)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
