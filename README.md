# AutoPush AI Agent (Free & Offline)

This tool automatically commits and pushes your code to GitHub with AI-generated commit messages — using a **free local LLM model** via Ollama.

## Features
- Detects code changes
- Uses a local model (e.g., TinyLlama) to generate commit messages
- Pushes commits to your GitHub repository
- No OpenAI API key required!

## Requirements

1. Python 3
2. GitPython
3. Ollama (https://ollama.com)
4. A cloned GitHub repo

## Setup Instructions

1. Install Python packages:
```bash
pip install GitPython requests
```

2. Install and run Ollama:
```bash
ollama run tinyllama
```

3. Edit `autopush.py` and set your local Git repository path.

4. Run the script:
```bash
python autopush.py
```

5. (Optional) Add to a cron job or task scheduler to run it daily.

Enjoy automated coding with AI 🚀
