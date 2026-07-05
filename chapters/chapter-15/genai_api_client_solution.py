#!/usr/bin/env python3
"""
Solution: GenAI API Client using Google Gemini API.

This is a more complete version of the genai_api_client.py starter.
It adds error handling, system prompting, and multi-turn conversation.

Requirements:
    pip install google-genai

Authentication:
    Obtain a free API key from Google AI Studio (see Appendix C).
    export GOOGLE_API_KEY="your-key-here"

    To use OpenAI instead:
        pip install openai
        Replace genai.Client with openai.OpenAI and use
        client.chat.completions.create() instead of
        client.models.generate_content().
"""

import os
import sys


def chat(prompt, model="gemini-2.5-flash", system_instruction=None):
    """
    Send a prompt to the Gemini API and return the response.

    Args:
        prompt: The user prompt string.
        model: The Gemini model (default: gemini-2.5-flash).
        system_instruction: Optional system-level instruction for the model.

    Returns:
        The model's response text, or None on error.
    """
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GOOGLE_API_KEY not set.", file=sys.stderr)
        print("See Appendix C for instructions.", file=sys.stderr)
        # To use OpenAI instead, replace the above with:
        # api_key = os.environ.get("OPENAI_API_KEY")
        return None

    try:
        from google import genai

        client = genai.Client(api_key=api_key)
        # To use OpenAI instead, replace the above two lines with:
        # from openai import OpenAI
        # client = OpenAI(api_key=api_key)

        config = {}
        if system_instruction:
            config["system_instruction"] = system_instruction

        response = client.models.generate_content(
            model=model,
            contents=prompt,
            config=config if config else None,
        )
        return response.text
        # To use OpenAI instead, replace the above with:
        # messages = []
        # if system_instruction:
        #     messages.append({"role": "system", "content": system_instruction})
        # messages.append({"role": "user", "content": prompt})
        # response = client.chat.completions.create(
        #     model="gpt-4.1-mini",
        #     messages=messages,
        # )
        # return response.choices[0].message.content

    except ImportError:
        print("Error: google-genai not installed.", file=sys.stderr)
        print("Install: pip install google-genai", file=sys.stderr)
        return None
    except Exception as e:
        print(f"API error: {e}", file=sys.stderr)
        return None


def multi_turn_chat(prompts, model="gemini-2.5-flash"):
    """
    Run a multi-turn conversation with the Gemini API.

    Args:
        prompts: A list of user prompt strings.
        model: The Gemini model to use.

    Returns:
        A list of response strings, one per prompt.
    """
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GOOGLE_API_KEY not set.", file=sys.stderr)
        return []

    try:
        from google import genai

        client = genai.Client(api_key=api_key)
        # To use OpenAI instead:
        # from openai import OpenAI
        # client = OpenAI(api_key=api_key)

        chat_session = client.chats.create(model=model)
        responses = []

        for prompt in prompts:
            response = chat_session.send_message(prompt)
            responses.append(response.text)

        return responses
        # To use OpenAI instead, replace the loop above with:
        # messages = []
        # for prompt in prompts:
        #     messages.append({"role": "user", "content": prompt})
        #     response = client.chat.completions.create(
        #         model="gpt-4.1-mini",
        #         messages=messages,
        #     )
        #     reply = response.choices[0].message.content
        #     responses.append(reply)
        #     messages.append({"role": "assistant", "content": reply})
        # return responses

    except ImportError:
        print("Error: google-genai not installed.", file=sys.stderr)
        return []
    except Exception as e:
        print(f"API error: {e}", file=sys.stderr)
        return []


def ask_genai(user_message: str, history: list[dict[str, str]]) -> str:
    """Compatibility wrapper for labs that expect the starter's ask_genai().

    Converts the starter-client signature (user_message + history) into a
    single prompt string for chat(). Multi-turn conversation state is
    preserved by combining history with the new message.

    Args:
        user_message: The latest user prompt.
        history: Previous conversation turns as {"role", "content"} dicts.

    Returns:
        The model's response text, or an error string on failure.
    """
    parts = []
    for turn in history:
        role = turn.get("role", "unknown")
        content = turn.get("content", "")
        parts.append(f"[{role}]: {content}")
    parts.append(f"[user]: {user_message}")
    combined = "\n".join(parts)

    result = chat(combined)
    if result is None:
        return "Error: API call failed. Check your GOOGLE_API_KEY."
    return result


def main():
    """Demonstrate the chat function with system instruction and multi-turn."""
    print("=" * 60)
    print("GenAI API Client — Solution Demo (Google Gemini)")
    print("=" * 60)

    # --- System instruction demo ---
    print("\n--- System instruction demo ---")
    system = (
        "You are a helpful Python tutor. Always explain concepts "
        "clearly and provide code examples where appropriate."
    )
    response = chat(
        "What is a list comprehension?",
        system_instruction=system,
    )
    if response:
        print(f"Response:\n{response}")
    else:
        print("No response.")

    # --- Multi-turn conversation ---
    print("\n--- Multi-turn conversation ---")
    prompts = [
        "What is the capital of France?",
        "What is the population of that city?",
        "Name one famous landmark there.",
    ]
    responses = multi_turn_chat(prompts)
    for i, (prompt, response) in enumerate(zip(prompts, responses), 1):
        print(f"\nTurn {i}:")
        print(f"  User: {prompt}")
        print(f"  Model: {response}")

    if not responses:
        print("No multi-turn responses received.")


if __name__ == "__main__":
    main()
