# 📝 Notepad-style Task Manager
A simple Flask-based task management app with a nostalgic notepad look. Users can add, complete, update, and delete tasks with priorities and timestamps.

## 🚀 Features
- Add tasks with priorities (High / Medium / Low)
- Toggle task status with a modern switch
- Auto-updating priority dropdown
- Notepad-inspired UI design
- SQLite database backend

## 🖥 Screenshots 
<img width="750" alt="Screenshot 2025-05-12 at 2 53 40 PM" src="https://github.com/user-attachments/assets/394e1f2a-5b1b-4e12-b16f-6e1c490ce18e" />

## 🛠 Tech Stack
- Python 3.11
- Flask
- SQLite
- HTML + CSS (inline Jinja2 templates)
- Docker

## 📦 How to Run

```bash
# Clone the repo
git clone https://github.com/loverui129/Notepad-todo.git
cd Notepad-todo

# Install dependencies
pip install -r requirements.txt

# Run the app
python app_SQL.py
Then open your browser and visit: http://localhost:5000




🐳 Docker Deployment
You can also run this app using Docker:
# Build the Docker image
docker build -t notepad-todo .

# Run the container (port 5050 can be adjusted if needed)
docker run -p 5050:5000 notepad-todo

Or use Docker Compose:
docker compose up
Then visit: http://localhost:5050



