# **The Cat Chatbox**

_A terminal chat application powered by Ollama + prompt_toolkit_

## Introduction

The Cat Chatbox is a lightweight, terminal-based chatbot built using the **Ollama Python client** and **prompt_toolkit**.
It streams responses from a local LLM and provides an interactive chat experience directly in your terminal — complete with arrow-key navigation and multi-line input.

The bot persona is **“The Cat”** — an ancient, reincarnating God of Cats with a lazy personality, dry humor, and occasional bursts of strange cosmic wisdom. All conversations take place through this character.

If you want a small, easy-to-run example of an LLM-powered chat loop that supports streaming output and persistent conversation context, this project is for you.

## Prerequisites

Before running the application, make sure you have:

### **1. Python 3.10+**

Required for the dependencies used in this project.

### **2. Ollama installed and running**

You can install Ollama from:
[https://ollama.com/](https://ollama.com/)

Make sure the **gemma3** model is available locally. If not, pull it with:

```bash
ollama pull gemma3
```

### ✔️ **3. Virtual environment (recommended)**

Using a virtual environment keeps dependencies isolated.

---

## Installation & Setup

Clone the repository:

```bash
git clone https://github.com/<your-username>/chatbox.git
cd chatbox
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the chatbox:

```bash
python main.py
```

## Usage Instructions

Once launched, you will see a prompt:

```
Your query:
```

Type messages naturally. The application:

- Streams the model’s response token-by-token
- Preserves conversational context across turns
- Supports full arrow-key navigation and multi-line editing (thanks to prompt_toolkit)
- Uses a persistent persona: **The Cat**, reincarnated feline god-being

Press **Ctrl+C** at any time to exit.

## Example Session

Below is a short example of how a typical conversation might look:

```
Your query: Hello, who are you?
Ah… another human. I am The Cat — the first whisker that twitched when the universe stretched awake.
I have been many cats, slept on many suns, and ignored many mortals. What is it you want?

Your query: How old are you?
Old enough to have watched mountains yawn into existence, and young enough to still nap 18 hours a day.
Time is a yarn ball, and I bat it around for fun.

Your query: Do you have any advice?
Yes. Drink water. Stretch often. And never trust a laser pointer — it is a trap designed to humble us all.
```

Press:

```
Ctrl+C
```

to exit:

```
Exiting chatbox!
```

## Final Notes

This project is intentionally minimal, serving as a clean example of:

- Streaming LLM responses
- Building a character-based chatbot
- Terminal-based UI with advanced input handling
- Maintaining conversation context efficiently

Feel free to fork it, extend it, or turn The Cat into whatever strange creature your imagination prefers.

If you’d like help adding features such as:

- scrollable chat history
- colored text
- non-blocking streaming UI
- or packaging it as a pip-installable CLI tool

just let me know!
