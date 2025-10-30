# DevOps Demo Project

Hey there! 👋  
This is a small Flask app I built to learn and practice DevOps basics — like testing, Docker, CI/CD, and cloud deployment.

## How to run it locally

1. Clone the repo:
   ```
   git clone https://github.com/<your-username>/devops-demo.git
   cd devops-demo
   ```

2. Set up a virtual environment:
   ```
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Start the app:
   ```
   python app.py
   ```

Then open your browser and go to `http://localhost:5000/health` — you should see a little JSON response saying everything’s healthy ✅

## What’s inside

- A basic Flask app with a `/health` route
- A couple of tests using `pytest`
- GitHub Actions workflow for CI
- Dockerfile to containerize the app
- Auto-deployment setup using Render

## Why I made this

I wanted to understand how DevOps works in real life — not just theory. So I built this project to connect the dots between coding, testing, automation, and deployment.

---

Feel free to fork it, play around, or use it as a starting point for your own DevOps experiments!
```

