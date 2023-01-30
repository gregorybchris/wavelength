from dataclasses import dataclass
from pathlib import Path
from typing import List

import numpy as np
import pandas as pd

RANGE_SIZE = 12

@dataclass
class Pair:
    low: str
    high: str


def get_pairs(filepath: Path):
    df = pd.read_csv(filepath, header=None)
    return [Pair(low, high) for low, high in df.to_records(index=False)]


def play(pairs: List[Pair]):
    print("Press ENTER to start")

    seen = set()
    while True:
        # Pause for input
        input()

        # Stop if all extremes have been used
        if len(seen) == len(pairs):
            break

        # Get a random pair of extremes that have not been seen
        while True:
            n = np.random.randint(len(pairs))
            if n not in seen:
                seen.add(n)
                break

        pair = pairs[n]
        print(f"From [{pair.low}] to [{pair.high}]")

        k = np.random.randint(RANGE_SIZE) + 1
        print(f"Should be a [{k}] on a scale from 1-{RANGE_SIZE}")

    print("Game Over")


if __name__ == "__main__":
    filepath = Path(__file__).parent / "extremes.csv"
    pairs = get_pairs(filepath)
    play(pairs)
