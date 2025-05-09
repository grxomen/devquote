import json
import random
from pathlib import Path

def get_quote(category="motivation"):
    path = Path(__file__).parent / "quotes.json"
    with open(path, "r") as f:
        data = json.load(f)
    return random.choice(data.get(category, ["No quotes found."]))
