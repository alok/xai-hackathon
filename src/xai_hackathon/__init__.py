#!/usr/bin/env python3
# %%
import requests
from pathlib import Path
import json
import os

"""
This project analyzes personality traits of people based on their text, and a picture if time allows.

The point is to test the claims of Objective Personality Theory (from the YouTube channel once called 'davesuperpowers' (ikr)).

Since it's for the xAI hackathon, it's gonna use Grok.
"""


PROJECT_ROOT: Path = Path("/Users/alokbeniwal/xai-hackathon")

theory_files = [PROJECT_ROOT / "info" / f for f in ("Animals.md", "Functions.md", "'Human Needs.md'", "Sexuals.md", "Socials.md", "ebook.md", "elimination-tool.md" , "terms.md")]

# Read the theory overview and person's text
theory_overview = "\n\n".join(f"{f.name}\n\n{f.read_text(encoding='utf-8')}" for f in theory_files)

person_text = (PROJECT_ROOT / "data" / "Keanu Reeves 12 ObjectivePersonality.txt").read_text(encoding="utf-8")

def analyze_personality(theory_overview: str, person_text: str) -> str:
    """
    Analyze the personality of a person using Grok via a POST request to the chat completions endpoint.
    
    Args:
        theory_overview (str): The overview of the Objective Personality Theory.
        person_text (str): The text of the person to analyze.
    
    Returns:
        str: Grok's analysis of the person's personality type.
    """
    url = "https://api.x.ai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.environ.get('XAI_API_KEY')}"
    }
    data = {
        "messages": [
            {
                "role": "system",
                "content": "You are an expert in Objective Personality Theory. Analyze the given text and assign a personality type based on the theory."
            },
            {
                "role": "user",
                "content": f"Here is an overview of the Objective Personality Theory:\n\n{theory_overview}\n\nHere is text of a person:\n\n{person_text}\n\nAssign a personality type to this person based on the theory. Make sure to include the Animals and Masculine/Feminine scores. Keep cross checks/opposites in mind (example: Lead Consume must have Blast low becuase they oppose each other). Include social types. Provide a brief explanation for your assessment."
            }
        ],
        "model": "grok-preview",
        "stream": False,
        "temperature": 0
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"Error: {response.status_code} - {response.text}"

def main() -> None:
    # Call the Grok endpoint to analyze the personality
    personality_analysis = analyze_personality(theory_overview, person_text)
    print("Personality Analysis:")
    print(personality_analysis)

    # TODO: Implement the following steps
    # 1. Split person's text into chunks, only pick out chunks that are the person talking
    # 2. Assign a personality type to each chunk
    # 3. Combine chunks into a single personality type by averaging
    # 4. Output the final personality type

if __name__ == "__main__":
    main()
