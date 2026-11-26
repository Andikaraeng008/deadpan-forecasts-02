#!/usr/bin/env python3
"""Deadpan Forecasts for Cities That Do Not Exist.

Writes a single weather-forecast line for the invented city of
Quibbleford to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt).

The line is one deadpan broadcast sentence: concrete numbers, a vivid
image, and a twist in the final clause, exactly as a straight-faced TV
meteorologist would read it off the map. The gate allows 1-160
characters, so the line is checked before it is written.
"""

import os

# The forecast line (Kandidat 1, 149 characters, verified with len()).
FORECAST = (
    "In Quibbleford, expect 12 centimetres of uphill rain, winds of "
    "70 kilometres an hour, and one postman still delivering letters "
    "the rain already read."
)


def main() -> None:
    assert 1 <= len(FORECAST) <= 160, "forecast line must be 1-160 chars"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(FORECAST)


if __name__ == "__main__":
    main()
