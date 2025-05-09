import argparse
from .core import get_quote
from .ai import get_ai_quote

def main():
    parser = argparse.ArgumentParser(description="Get a random dev quote.")
    parser.add_argument("category", nargs="?", default="motivation")
    parser.add_argument("--ai", help="Use AI to generate a custom quote", action="store_true")
    args = parser.parse_args()

    if args.ai:
        print(get_ai_quote(f"Give me a {args.category} quote"))
    else:
        print(get_quote(args.category))
