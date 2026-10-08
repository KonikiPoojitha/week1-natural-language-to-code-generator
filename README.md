# Natural Language-to-Code Generator

A Week 1 SkillAudit.ai internship project that converts a plain-English programming task into runnable Python code using a free LLM provider.

## Features

- Python command-line interface (CLI)
- Groq API support
- Optional local Ollama support
- Strong system prompt that requests code only
- Removes accidental Markdown code fences
- Prints generated code in the terminal
- Automatically saves generated code to a `.py` file
- Includes 8 requirement-focused test examples
- No paid hosting required

## Project structure

```text
natural-language-to-code-generator/
├── app.py
├── llm_client.py
├── test_generator.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## 1. Create a virtual environment

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

## 3. Configure Groq

Copy the example environment file:

```bash
cp .env.example .env
```

Open `.env` and replace:

```text
GROQ_API_KEY=your_groq_api_key_here
```

with your actual Groq API key.

The `.env` file is ignored by Git, so your secret is not uploaded.

## 4. Run the generator

Interactive mode:

```bash
python app.py
```

Then enter:

```text
write a function that checks if a number is prime
```

Or provide the task directly:

```bash
python app.py "write a function that checks if a number is prime"
```

Save to a custom filename:

```bash
python app.py "write a function that checks if a number is prime" -o prime_checker.py
```

The generated code is printed to the terminal and saved automatically.

## 5. Run the 8 tests

```bash
python test_generator.py
```

The tests use mock responses and do not require an API key.

They cover:

1. String reversal
2. Vowel counting
3. Factorial calculation
4. Prime-number checking
5. Duplicate removal from a list
6. Finding the largest list item
7. Dictionary/word-frequency operations
8. Sorting a dictionary by values

## 6. Optional: use Ollama instead

Install Ollama separately, start it, and pull a model such as `llama3.2`.

Then configure:

```text
LLM_PROVIDER=ollama
OLLAMA_MODEL=llama3.2
OLLAMA_URL=http://localhost:11434/api/chat
```

Run the same command:

```bash
python app.py "write a function that checks if a number is prime"
```

## Security note

Never commit your `.env` file or expose your API key in screenshots, GitHub, LinkedIn, or demo videos.

## SkillAudit.ai Week 1 checklist

- [x] Python CLI
- [x] Plain-English task input
- [x] Free LLM integration
- [x] Generated code printed to terminal
- [x] Generated code saved automatically to `.py`
- [x] At least 8 task examples
- [x] String, math, list, and dictionary operations
- [x] Code-only system prompt
- [x] Markdown fence cleanup
- [x] GitHub-ready project structure
