"""
IX-Joey CLI Interface

Provides an interactive command-line interface for natural
language queries routed through JoeyCore to IX-Gibson.
"""

from core.joey_core import JoeyCore

def run_joey_cli():
    core = JoeyCore()
    print("IX-Joey — Natural Language Processor")
    print("Type your input below. Type 'exit' to quit.\n")

    while True:
        user_input = input("Joey> ").strip()
        if user_input.lower() in ("exit", "quit"):
            print("Exiting IX-Joey interface. Have a great day!")
            break
        output = core.interpret(user_input)
        print(f"→ {output}")

if __name__ == "__main__":
    run_joey_cli()
