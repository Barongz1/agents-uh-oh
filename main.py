"""The Agent's Uh-Oh — entry for make.fun.

Writes one word to /output/entry.txt.
"""
import os

# The word: what an agent says when it has no idea what to do.
TEXT = "Hallucinating"

def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

def main():
    write_entry()

if __name__ == "__main__":
    main()
