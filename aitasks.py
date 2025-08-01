from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:3000"],  # adjust as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/generate-task")
def generate_task():
    # Very simple task generation for now
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    op = random.choice(['+', '-', '*'])
    
    if op == '+':
        answer = a + b
    elif op == '-':
        answer = a - b
    else:
        answer = a * b

    return {
        "question": f"What is {a} {op} {b}?",
        "answer": answer
    }
