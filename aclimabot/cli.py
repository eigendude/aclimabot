import argparse
import os
from pathlib import Path
from typing import Optional

import openai


DEFAULT_SYSTEM_PROMPT = (
    "You are a compiler that turns English descriptions of "
    "model-view-controller web apps into React applications."
    " Return only code inside markdown fenced code blocks."
)


def call_openai(prompt: str, model: str = "gpt-4o") -> str:
    """Send the prompt to OpenAI and return the generated code."""
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY environment variable not set")
    openai_client = openai.OpenAI(api_key=api_key)

    response = openai_client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": DEFAULT_SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        temperature=0,
    )
    return response.choices[0].message.content


def generate_react_app(prompt_file: Path, output: Optional[Path] = None) -> None:
    """Generate a React app from a natural language prompt."""
    prompt = prompt_file.read_text()
    generated = call_openai(prompt)

    if output is None:
        output = Path("generated-app")
    output.mkdir(parents=True, exist_ok=True)

    (output / "App.jsx").write_text(generated)


def main(argv: Optional[list[str]] = None) -> None:
    parser = argparse.ArgumentParser(description="Generate React code from prompts.")
    parser.add_argument("prompt", type=Path, help="Path to the text prompt file")
    parser.add_argument("-o", "--output", type=Path, help="Output directory")
    parser.add_argument("--model", default="gpt-4o", help="OpenAI model name")
    args = parser.parse_args(argv)

    generate_react_app(args.prompt, args.output)


if __name__ == "__main__":
    main()
