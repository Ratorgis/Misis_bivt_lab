import argparse
from pathlib import Path

from lab_03.text_stats import stdin_info, stdout_text_info

def main():
    parser = argparse.ArgumentParser(description = "CLI‑utils for lab №6")
    subparsers = parser.add_subparsers(dest = "command")

    cat_parser = subparsers.add_parser("cat", help = "Print file content")
    cat_parser.add_argument("--input", required = True, type = Path)
    cat_parser.add_argument("-n", action = "store_true", help = "Numerate lines in output")

    stats_parser = subparsers.add_parser("stats", help = "Word frequency in text")
    stats_parser.add_argument("--input", type = str, required = True)
    stats_parser.add_argument("--top", type = int, default=5)
    stats_parser.add_argument("-p", action = 'store_true', help = "Output in table form")

    args = parser.parse_args()

    if not args.command:
        parser.error('You')

    if args.command == "cat":
        with args.input.open('r', encoding = 'utf-8') as f:
            for number, text in enumerate(f):
                if args.n:
                    print(f'{number + 1}: {text.strip()}')
                else:
                    print(text.strip())
    elif args.command == "stats":
        info = stdin_info(args.input)
        stdout_text_info(info, args.p)

if __name__ == '__main__':
    main()
