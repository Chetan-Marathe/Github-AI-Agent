import os
import git
import requests
from datetime import datetime


REPO_PATH = r"C:\Users\marat\OneDrive\Desktop\Leetcode"  
OLLAMA_MODEL = "tinyllama:latest"  

def get_git_diff(repo):
    return repo.git.diff('HEAD')

def generate_commit_message(diff_text):
    prompt = f"Write a short and clear git commit message for the following changes:\n{diff_text}"

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()
    return result.get("response", "Update project")

def push_code():
    repo = git.Repo(REPO_PATH)
    repo.git.add(A=True)

    if repo.is_dirty():
        diff = get_git_diff(repo)
        commit_message = generate_commit_message(diff)

        repo.index.commit(commit_message)
        origin = repo.remote(name='origin')
        origin.push()
        print(f"✅ Code pushed with message: {commit_message}")
    else:
        print("📁 No changes to commit.")


if __name__ == "__main__":
    push_code()
