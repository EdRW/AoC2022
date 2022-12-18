from argparse import ArgumentParser
import sys


def parse_args(args: list[str]) -> str:
    parser = ArgumentParser()
    parser.add_argument("filename", type=str)
    known_args, _ = parser.parse_known_args(args)
    return known_args.filename


def main(filename: str) -> int:
    with open(filename, mode="r") as file:

        running_total, current_max = 0, 0
        while line := file.readline():
            if line != "\n":
                calories = int(line)
                running_total += calories
            else:
                current_max = max(current_max, running_total)
                running_total = 0

        return current_max


if __name__ == "__main__":
    filename = parse_args(sys.argv[1:])
    output = main(filename)
    print(output)
