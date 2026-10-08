import argparse
from pathlib import Path

from llm_client import generate_code


def clean_code(text: str) -> str:
    """Remove accidental Markdown fences from an LLM response."""
    text = text.strip()
    if text.startswith("```"):
        lines = text.splitlines()
        if lines and lines[0].strip().startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        text = "\n".join(lines).strip()
    return text


def save_code(code: str, output_file: str) -> Path:
    output_path = Path(output_file)
    if output_path.suffix != ".py":
        output_path = output_path.with_suffix(".py")
    output_path.write_text(code.rstrip() + "\n", encoding="utf-8")
    return output_path


def main():
    parser = argparse.ArgumentParser(
        description="Natural-language-to-Python code generator"
    )
    parser.add_argument(
        "task",
        nargs="*",
        help="Plain-English programming task. If omitted, you will be prompted.",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="generated_code.py",
        help="Output .py filename (default: generated_code.py)",
    )
    args = parser.parse_args()

    task = " ".join(args.task).strip()
    if not task:
        task = input("Describe the Python task: ").strip()

    if not task:
        raise SystemExit("No task supplied.")

    print("\nGenerating Python code...\n")
    raw_code = generate_code(task)
    code = clean_code(raw_code)

    print("----- GENERATED CODE -----")
    print(code)
    print("--------------------------")

    path = save_code(code, args.output)
    print(f"\nSaved to: {path.resolve()}")


if __name__ == "__main__":
    main()
