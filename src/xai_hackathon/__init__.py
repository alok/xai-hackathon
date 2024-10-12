import xai_sdk
from pathlib import Path
"""
~This module makes a heatmap of gazes on a room. It extracts faces from an image, and then uses a gaze estimation model to estimate the gaze direction of each face.~

Scratch that, Grok doesn't OUTPUT images. 


Since it's for the xAI hackathon, it's gonna use Grok.


Images 

"""
PROJECT_ROOT = Path(__file__).parent

# an image of a face, to get a bounding box
test_image = PROJECT_ROOT / "test_image.jpg"


def main()->None:
    xai_sdk.run(test_image)

