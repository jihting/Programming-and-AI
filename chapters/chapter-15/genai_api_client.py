#!/usr/bin/env python3
"""
A simple generative AI API client using the Google Gemini API.

This module demonstrates how to call an LLM from Python code — sending a prompt,
receiving a generated response, and handling the result.

Requirements:
    pip install google-genai

Authentication:
    Obtain a free API key from Google AI Studio (see Appendix C in the book).
    Set it as an environment variable:
        export GOOGLE_API_KEY="your-key-here"

    To use OpenAI instead:
        pip install openai
        Replace the Client creation and API call with:
            from openai import OpenAI
            client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
"""

import os
import sys


def chat(prompt, model="gemini-2.5-flash"):
    """
    Send a single prompt to the Gemini API and return the response text.

    Args:
        prompt: The user prompt string.
        model: The Gemini model to use. Default is gemini-2.5-flash.

    Returns:
        The model's response as a string, or None on error.
    """
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GOOGLE_API_KEY environment variable is not set.", file=sys.stderr)
        print("See Appendix C for instructions on obtaining a free API key.", file=sys.stderr)
        # To use OpenAI instead, replace the above with:
        # api_key = os.environ.get("OPENAI_API_KEY")
        # if not api_key:
        #     print("Error: OPENAI_API_KEY environment variable is not set.", file=sys.stderr)
        return None

    try:
        from google import genai

        client = genai.Client(api_key=api_key)
        # To use OpenAI instead, replace the above two lines with:
        # from openai import OpenAI
        # client = OpenAI(api_key=api_key)

        response = client.models.generate_content(
            model=model,
            contents=prompt,
        )
        return response.text
        # To use OpenAI instead, replace the above with:
        # response = client.chat.completions.create(
        #     model="gpt-4.1-mini",
        #     messages=[{"role": "user", "content": prompt}],
        # )
        # return response.choices[0].message.content

    except ImportError:
        print(
            "Error: The google-genai package is not installed.",
            file=sys.stderr,
        )
        print("Install it with:  pip install google-genai", file=sys.stderr)
        # To use OpenAI instead:
        # print("Install it with:  pip install openai", file=sys.stderr)
        return None
    except Exception as e:
        print(f"API call failed: {e}", file=sys.stderr)
        return None


def main():
    """Demonstrate the chat function with several example prompts."""
    print("=" * 60)
    print("GenAI API Client Demo (Google Gemini)")
    print("=" * 60)

    # --- Example 1: Creative generation ---
    print("\n--- Example 1: Creative generation ---")
    prompt = "Write a haiku about a programmer learning to code."
    response = chat(prompt)
    if response:
        print(f"Prompt: {prompt}")
        print(f"Response:\n{response}")
    else:
        print("No response received.")

    # --- Example 2: Factual question ---
    print("\n--- Example 2: Factual question ---")
    prompt = "In one sentence, what is a transformer in the context of AI?"
    response = chat(prompt)
    if response:
        print(f"Prompt: {prompt}")
        print(f"Response:\n{response}")
    else:
        print("No response received.")

    # --- Example 3: Code help ---
    print("\n--- Example 3: Code help ---")
    prompt = (
        "Write a Python function called fibonacci(n) that returns the nth "
        "Fibonacci number. Include a brief docstring. Return only the "
        "function, without any explanation."
    )
    response = chat(prompt)
    if response:
        print(f"Prompt: {prompt}")
        print(f"Response:\n{response}")
    else:
        print("No response received.")


if __name__ == "__main__":
    main()
