#!/usr/bin/python3
# 0-fizzbuzz.py

import sys


def fizzbuzz(n: int) -> None:
    out = []
    for i in range(1, n + 1):
        label = ""
        if i % 3 == 0:
            label += "Fizz"
        if i % 5 == 0:
            label += "Buzz"
        out.append(label or str(i))
    print(" ".join(out))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be an integer")
        sys.exit(1)

    fizzbuzz(N)
