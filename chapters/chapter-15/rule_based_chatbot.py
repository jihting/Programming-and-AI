"""Week 6 Lab 1 starter: a deliberately simple rule-based chatbot.

This bot is intentionally limited. The point is to experience how brittle
keyword-matching systems can be before comparing them with GenAI systems.
"""

from __future__ import annotations

import json
import random
from pathlib import Path

RESPONSES_FILE = Path("keyword_responses.json")


def load_responses(path: Path = RESPONSES_FILE) -> dict[str, list[str]]:
    """Load keyword-response mappings from a JSON file."""
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def normalise(text: str) -> str:
    """Return a simpler version of user input for keyword matching."""
    return text.lower().strip()


def find_keyword(message: str, responses: dict[str, list[str]]) -> str:
    """Return the first keyword found in the message, or 'default'."""
    cleaned = normalise(message)
    for keyword in responses:
        if keyword == "default":
            continue
        if keyword in cleaned:
            return keyword
    return "default"


def choose_response(keyword: str, responses: dict[str, list[str]]) -> str:
    """Choose one response for a keyword."""
    options = responses.get(keyword, responses["default"])
    return random.choice(options)


def update_state(message: str, state: dict[str, str]) -> None:
    """Update simple conversation state.

    TODO: In the lab, extend this so the bot can remember a user's name.
    For example, if the user types 'my name is Asha', store 'Asha'.
    """
    cleaned = normalise(message)
    if cleaned.startswith("my name is "):
        state["name"] = message[11:].strip()


def build_reply(message: str, responses: dict[str, list[str]], state: dict[str, str]) -> str:
    """Build a reply using keyword matching and simple state."""
    update_state(message, state)

    if "name" in state and "name" in normalise(message):
        return f"I will try to remember that your name is {state['name']}."

    keyword = find_keyword(message, responses)
    reply = choose_response(keyword, responses)

    if "name" in state and keyword != "default":
        reply = f"{state['name']}, {reply}"

    return reply


def run_chatbot() -> None:
    """Run the chatbot until the user types quit."""
    responses = load_responses()
    state: dict[str, str] = {}

    print("Rule-based chatbot. Type 'quit' to stop.")
    while True:
        message = input("You: ")
        if normalise(message) in {"quit", "exit", "bye"}:
            print("Bot: Goodbye.")
            break
        print("Bot:", build_reply(message, responses, state))


if __name__ == "__main__":
    run_chatbot()
