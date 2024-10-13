#!/usr/bin/env python3
# %%
from dataclasses import dataclass
import tyro
import requests
from pathlib import Path
import json
import os
import random
import string

"""
This project analyzes personality traits of people based on their text, and a picture if time allows.

The point is to test the claims of Objective Personality Theory (from the YouTube channel once called 'davesuperpowers' (ikr)).

Since it's for the xAI hackathon, it's gonna use Grok.
"""


PROJECT_ROOT: Path = Path(__file__).parent.parent.parent

INFO_DIR: Path = PROJECT_ROOT / "info"
DATA_DIR: Path = PROJECT_ROOT / "data"

# XXX this is in a specific order to present the theory in a logical order
theory_files = [
    INFO_DIR / f
    for f in (
        "ebook.md",
        "Animals.md",
        "Functions.md",
        "Human Needs.md",
        "Sexuals.md",
        "Socials.md",
        # "terms.md",
        "elimination-tool.md",
    )
]

# Read the theory overview and person's text
theory_overview = "\n\n".join(
    f"{f.name}\n\n{f.read_text(encoding='utf-8')}" for f in theory_files
)

# To cross-check personality types
ELIMINATION_TOOL = (INFO_DIR / "elimination-tool.md").read_text(encoding="utf-8")

person_text = (
    DATA_DIR / "Keanu Reeves 12 ObjectivePersonality.txt"
).read_text(encoding="utf-8")


output_fmt = """

Examples:

- Feminine Fi/Masculine Ni (Sleep Consume Play Blast)
- Feminine Fi/Feminine Ni (Sleep Consume Blast Play)

"""


rand_slug: str = "".join(random.choices(string.ascii_letters + string.digits, k=6))

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
        "Authorization": f"Bearer {os.environ.get('XAI_API_KEY')}",
    }
    data = {
        "messages": [
            {
                "role": "system",
                "content": f"(slug: {rand_slug}) You are an expert in Objective Personality Theory. Analyze the given text and assign a personality type based on the theory.",
            },
            {
                "role": "system",
                "content": f"""Here is an overview of the Objective Personality Theory:\n\n{theory_overview}""",
            },
            {
                "role": "system",
                "content": f"""Here is an elimination tool to help you assign a personality type:
                    {ELIMINATION_TOOL}
                """,
            },
            {
                "role": "system",
                "content": f"Here is an analysis of Keanu Reeves to use as an exemplar, split in 2 parts, separated by `|||`:\n\n{(PROJECT_ROOT / 'data' / 'Keanu Reeves 12 ObjectivePersonality.txt').read_text(encoding='utf-8') + '\n\n|||\n\n' + (PROJECT_ROOT / 'data' / 'Keanu Reeves 22 ObjectivePersonality.txt').read_text(encoding='utf-8')}",
            },  # TODO social types
            {
                "role": "user",
                "content": f"""Assign a personality type to this person based on Objective Personality Theory as given above. Start with the Animals to ensure no regurgitation of known personality analyses you were trained on. Keep cross checks/opposites in mind (example: Lead Consume must have Blast low because they oppose each other). Provide a brief explanation for your assessment.
                
                Return output in the following format:

                {output_fmt}

                Here is text of the person:\n\n{person_text}\n\n""",
            },
        ],
        "model": "grok-preview",
        "stream": False,
        "temperature": 0.3,
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code} - {response.text}"


@dataclass
class Args:
    # path to the person's words
    person_text_path: Path = DATA_DIR / "gabor-mate.txt"


def main(args: Args) -> None:
    # Call the Grok endpoint to analyze the personality
    personality_analysis = analyze_personality(
        theory_overview, args.person_text_path.read_text(encoding="utf-8")
    )
    print("Personality Analysis:")
    print(personality_analysis)

    # TODO: Implement the following steps
    # 1. Split person's text into chunks, only pick out chunks that are the person talking
    # 2. Assign a personality type to each chunk
    # 3. Combine chunks into a single personality type by averaging
    # 4. Output the final personality type


# TODO allow scraping tweets

if __name__ == "__main__":
    args = tyro.cli(Args)
    main(args)

# %%
#TODO give scratch space to model output for thinking and taking average, have it extract out 

