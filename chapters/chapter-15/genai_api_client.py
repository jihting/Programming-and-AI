"""Week 6 Lab 2 starter: generic GenAI API client.

This file is deliberately provider-neutral. Your tutor will tell you which
endpoint and API key to use. Do not hard-code API keys in this file.

The starter uses environment variables:
- GENAI_API_ENDPOINT
- GENAI_API_KEY

If those are not set, the program runs in dry-run mode so you can inspect the
request body without sending anything.
"""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from typing import Any


SYSTEM_PROMPT = "You are a helpful teaching assistant for first-year programming students."


def build_request_body(messages: list[dict[str, str]]) -> dict[str, Any]:
    """Build a common chat-style request body.

    Your tutor may ask you to adjust this shape for the university endpoint.
    """
    return {
        "messages": messages,
        "temperature": 0.3,
        "max_tokens": 200,
    }


def send_request(endpoint: str, api_key: str, body: dict[str, Any]) -> dict[str, Any]:
    """Send a JSON request and return the parsed JSON response."""
    data = json.dumps(body).encode("utf-8")
    request = urllib.request.Request(
        endpoint,
        data=data,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def extract_text(response_json: dict[str, Any]) -> str:
    """Extract text from a typical chat-completion response.

    If your endpoint returns a different JSON shape, adapt this function only.
    """
    try:
        return response_json["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError):
        return json.dumps(response_json, indent=2)


def ask_genai(user_message: str, history: list[dict[str, str]]) -> str:
    """Send one user message while preserving a simple conversation history."""
    endpoint = os.getenv("GENAI_API_ENDPOINT")
    api_key = os.getenv("GENAI_API_KEY")

    messages = [{"role": "system", "content": SYSTEM_PROMPT}] + history
    messages.append({"role": "user", "content": user_message})
    body = build_request_body(messages)

    if not endpoint or not api_key:
        return "DRY RUN: set GENAI_API_ENDPOINT and GENAI_API_KEY to send this request:\n" + json.dumps(body, indent=2)

    try:
        response_json = send_request(endpoint, api_key, body)
    except urllib.error.URLError as error:
        return f"API request failed: {error}"

    return extract_text(response_json)


def run_chat() -> None:
    """Run a small API-backed chat loop."""
    history: list[dict[str, str]] = []
    print("GenAI API chatbot. Type 'quit' to stop.")
    print("Do not paste passwords, API keys, or personal data into prompts.")

    while True:
        user_message = input("You: ")
        if user_message.lower().strip() in {"quit", "exit", "bye"}:
            print("Bot: Goodbye.")
            break
        reply = ask_genai(user_message, history)
        print("Bot:", reply)
        history.append({"role": "user", "content": user_message})
        history.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    run_chat()
