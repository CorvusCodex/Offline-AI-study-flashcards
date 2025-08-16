#!/usr/bin/env python3
"""
Study Flashcards Maker (offline)
Usage:
  python main.py --input "photosynthesis"
"""
import argparse, requests, os, sys

OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434/api/generate")
MODEL = "llama3.2:4b"
TIMEOUT = 120

def run_llama(prompt):
    r = requests.post(OLLAMA_URL, json={"model": MODEL, "prompt": prompt, "stream": False}, timeout=TIMEOUT)
    r.raise_for_status()
    return r.json().get("response","").strip()

def build_prompt(topic):
    return (
        "Create 10 study flashcards for the topic. Format EXACTLY:\n"
        "Q: question\nA: answer\n\n"
        f"Topic: {topic}"
    )

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", "-i", required=True)
    args = p.parse_args()
    print(run_llama(build_prompt(args.input)))

if __name__ == "__main__":
    main()
