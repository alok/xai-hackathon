import xai_sdk
from pathlib import Path
"""
This project analyzes personality traits of people based on their text, and a picture if time allows.

The point is to test the claims of Objective Personality Theory (from the YouTube channel once called 'davesuperpowers' (ikr)).




Since it's for the xAI hackathon, it's gonna use Grok.


Images 

"""
PROJECT_ROOT = Path(__file__).parent

# an image of a face, to get a bounding box
test_image = PROJECT_ROOT / "test_image.jpg"


def main()->None:
    xai_sdk.run(test_image)

