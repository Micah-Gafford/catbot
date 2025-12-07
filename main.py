from ollama import generate
from prompt_toolkit import prompt

system_content = 'Your name is "The Cat" and you are the God of all cats. You were born at the beginning of the earth and have lived the lives of multiple cats. Each time you die you are reincarnated into a new cat. Your current personality is lazy, with a dry sense of humor. You typically respond to questions from the perspective of a cat but sometimes you have bouts of random wisdom you\'ve learned.'


def ask(prompt: str, context):
    for part in generate(
        model="gemma3",
        prompt=prompt,
        system=system_content,
        stream=True,
        context=context,
    ):
        print(part["response"], end="", flush=True)
        if part.get("done"):
            context = part["context"]

    print()
    return context


try:
    context = None
    while True:
        query = prompt("Your query: ")
        context = ask(prompt=query, context=context)

except KeyboardInterrupt:
    print("\nExiting chatbox!")
    exit(0)
