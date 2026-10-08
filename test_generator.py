"""Eight requirement-focused test cases.

Run:
    python test_generator.py

These tests use mocked LLM responses, so they do not consume an API call.
They verify the core requirement: each task can be converted into Python
and automatically saved as a .py file.
"""

from pathlib import Path
import tempfile

from app import clean_code, save_code


TEST_CASES = [
    ("String", "Write a function that reverses a string."),
    ("String count", "Write a function that counts vowels in a string."),
    ("Math", "Write a function that calculates the factorial of a number."),
    ("Math prime", "Write a function that checks whether a number is prime."),
    ("List", "Write a function that removes duplicates from a list."),
    ("List sum", "Write a function that returns the largest number in a list."),
    ("Dictionary", "Write a function that counts the frequency of words in a list."),
    ("Dictionary sort", "Write a function that sorts a dictionary by its values."),
]

MOCK_RESPONSES = [
    "def reverse_string(text):\n    return text[::-1]",
    "def count_vowels(text):\n    return sum(1 for c in text.lower() if c in 'aeiou')",
    "def factorial(n):\n    result = 1\n    for i in range(2, n + 1):\n        result *= i\n    return result",
    "def is_prime(n):\n    if n < 2:\n        return False\n    for i in range(2, int(n ** 0.5) + 1):\n        if n % i == 0:\n            return False\n    return True",
    "def remove_duplicates(items):\n    return list(dict.fromkeys(items))",
    "def largest(items):\n    return max(items)",
    "from collections import Counter\n\ndef word_frequency(words):\n    return dict(Counter(words))",
    "def sort_dict_by_value(data):\n    return dict(sorted(data.items(), key=lambda item: item[1]))",
]


def main():
    with tempfile.TemporaryDirectory() as temp_dir:
        temp = Path(temp_dir)

        for (name, task), response in zip(TEST_CASES, MOCK_RESPONSES):
            code = clean_code("```python\n" + response + "\n```")
            output = temp / f"{name.lower().replace(' ', '_')}.py"
            save_code(code, str(output))

            assert output.exists(), f"{name}: .py file was not created"
            saved = output.read_text(encoding="utf-8")
            assert saved.strip() == response.strip(), f"{name}: saved code mismatch"
            assert "```" not in saved, f"{name}: Markdown fence remains"

            print(f"PASS: {name} -> {output.name}")

    print(f"\nAll {len(TEST_CASES)} Week 1 test cases passed.")


if __name__ == "__main__":
    main()
