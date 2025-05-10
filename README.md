
# 🧠 AI-Based Study Planner

![Streamlit](https://img.shields.io/badge/Built%20With-Streamlit-ff4b4b?logo=streamlit)
![TinyLlama](https://img.shields.io/badge/LLM-TinyLlama-blue)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

An intelligent and personalized exam preparation assistant built with **Streamlit** and powered by **TinyLlama** via `Ollama`. This tool helps you create study plans, get AI-powered suggestions, and stay on track with your goals.

---

## 🚀 Features

- 🔐 **Login system** (Demo-based)
- 🧠 **AI Study Suggestions** (TinyLlama-powered)
- 📅 **Custom Study Plan Generator**
- 📊 **Visual Study Analytics**
- 💾 **Save/Load/Delete Plans**
- 🔔 **Notification Alerts**
- ☁️ *(Coming Soon)* Calendar Sync with Google

---

## 🛠️ Tech Stack

- **Frontend/UI:** Streamlit
- **Backend Logic:** Python
- **LLM:** TinyLlama (via [Ollama](https://ollama.com))
- **Data Storage:** JSON (local)

---

## 📁 Project Structure

```
.
├── app.py                   # Main application code
├── user_data/               # Folder to store user study plans
└── README.md
```

---

## ✅ Demo Login

> 🔑 Use these credentials to test the app:
- **Username:** `user`
- **Password:** `pass`

---

## 💻 Getting Started Locally

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/ai-study-planner.git
cd ai-study-planner
```

### 2. Install Requirements
```bash
pip install streamlit requests
```

### 3. Run TinyLlama via Ollama
Make sure you have [Ollama installed](https://ollama.com) and run:
```bash
ollama run tinyllama
```

### 4. Launch the App
```bash
streamlit run app.py
```

---

## ☁️ Streamlit Cloud Deployment

To deploy this on [Streamlit Community Cloud](https://streamlit.io/cloud):

1. Push your code to a **GitHub** repository.
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo and deploy.
4. Note: Since Ollama/TinyLlama runs locally, AI features won't work on cloud unless you connect to a cloud-hosted LLM endpoint.

---

## 🐳 Docker Setup (Optional)

Create a `Dockerfile`:

```dockerfile
FROM python:3.10

WORKDIR /app
COPY . /app

RUN pip install streamlit requests

EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]
```

Then build and run:
```bash
docker build -t ai-study-planner .
docker run -p 8501:8501 ai-study-planner
```

---

## 🧪 AI Prompt Example

```text
I am preparing for exams. I have the following subjects: Math, Science.
I can study 4 hours per day. Suggest some effective study techniques.
```

---

## 📌 To-Do

- [ ] Replace dummy auth with secure login (e.g., Firebase Auth)
- [ ] Add export to calendar (.ics file or Google API)
- [ ] Enable cloud LLM fallback for deployment

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).
