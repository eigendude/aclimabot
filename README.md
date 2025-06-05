# aclimabot

`aclimabot` is a simple command-line tool that turns natural-language prompts
into React source code using OpenAI's chat models. It demonstrates a very small
"natural language to framework" compiler pipeline.

## Installation

```bash
pip install openai
```

## Usage

Create one or more text files containing the natural language description of your app. Multiple files are concatenated in the order provided:

```text
Create a todo application. It should display a list of items and allow adding
new ones. Use functional React components.
```

You can also define separate pieces of the application in different files. For
example `examples/Puppy.txt` contains:

```text
Puppy is an object.
It has the following properties:
- an integer to store weight
- a string to store name
It has an initialization function called eat which takes two parameters, weight
and eat.
```

Run the generator:

```bash
export OPENAI_API_KEY=YOUR_KEY
python -m aclimabot.cli prompt.txt examples/Puppy.txt -o my-react-app
```

A deterministic answer is requested by setting `temperature=0`. The generated
React code will be written to `my-react-app/App.jsx`.

The OpenAI API key must be provided via the `OPENAI_API_KEY` environment
variable. The model defaults to `gpt-4o` but can be changed with `--model`.
