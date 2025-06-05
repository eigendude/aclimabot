# aclimabot

`aclimabot` is a simple command-line tool that turns natural-language prompts
into React source code using OpenAI's chat models. It demonstrates a very small
"natural language to framework" compiler pipeline.

## Installation

```bash
pip install openai
```

## Usage

Create a text file containing the natural language description of your app:

```text
Create a todo application. It should display a list of items and allow adding
new ones. Use functional React components.
```

Run the generator:

```bash
export OPENAI_API_KEY=YOUR_KEY
python -m aclimabot.cli prompt.txt -o my-react-app
```

A deterministic answer is requested by setting `temperature=0`. The generated
React code will be written to `my-react-app/App.jsx`.

The OpenAI API key must be provided via the `OPENAI_API_KEY` environment
variable. The model defaults to `gpt-4o` but can be changed with `--model`.
