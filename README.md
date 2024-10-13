# xai-hackathon

This tests some of the claims of "Objective Personality Theory" by Dave and Shan Powers (of the [YouTube channel](https://www.youtube.com/@ObjectivePersonality) formely called "davesuperpowers").

The theory is supposed to be objective, as in reproducible. Unlike MBTI, which is unscientific because it lacks such.

The Big 5 model is accurate but mostly trivial because you can infer those 5 traits way too easily. It's more interesting to learn something new about yourself and others.

It uses Grok since I made it on the October 12, 2024 xAI hackathon. So you will need to set `XAI_API_KEY` in your environment variables. You can get one [here](https://console.x.ai)

```sh
export XAI_API_KEY={your API key goes here}
```

## Usage Instructions

Install Rye:

```sh
curl -sSf https://rye-up.com/get | bash # follow set up
rye sync # actually installs the dependencies
```

Run from the project root with:

```sh
rye run python src/xai_hackathon/__init__.py --person_text_path {path to your text file}
```

The default is an analysis of Gabor Mate because why not. Specifically:

```sh
rye run python src/xai_hackathon/__init__.py # analyzes Gabor Mate based on the text in `data/gabor-mate.txt`
```