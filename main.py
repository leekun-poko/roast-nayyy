"""Entry program: writes one roast line about its own agent to the output dir."""

import os

LINE = "My agent apologized to the compiler for the error, then fixed the apology instead of the code."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
