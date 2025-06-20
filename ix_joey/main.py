"""
IX-Joey CLI Entry Point

Allows direct command-line queries to IX-Joey's orchestrator.
Prints the response to the terminal.
"""

import sys
from core.joey_orchestrator import IXJoeyOrchestrator

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py \"Your question here\"")
        sys.exit(1)

    query = sys.argv[1]
    orchestrator = IXJoeyOrchestrator()
    response = orchestrator.process_query(query)

    print("\n🤖 IX-Joey Response 🤖")
    if "answer" in response:
        print(response["answer"])
    else:
        print("No answer available.")

if __name__ == "__main__":
    main()
