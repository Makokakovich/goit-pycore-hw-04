import sys
from pathlib import Path

from colorama import Fore, Style, init


def print_tree(path: Path, prefix: str = "") -> None:
    try:
        items = list(path.iterdir())
    except PermissionError:
        print(prefix + Fore.RED + "[Permission denied]" + Style.RESET_ALL)
        return

    for i, item in enumerate(items):
        last = i == len(items) - 1
        branch = "\\-- " if last else "+-- "
        next_prefix = prefix + ("    " if last else "|   ")

        if item.is_dir():
            print(prefix + branch + Fore.BLUE + item.name + Style.RESET_ALL)
            print_tree(item, next_prefix)
        else:
            print(prefix + branch + Fore.GREEN + item.name + Style.RESET_ALL)


def main() -> None:
    init(autoreset=True)

    if len(sys.argv) != 2:
        print("Usage: python task3.py <directory_path>")
        return

    directory = Path(sys.argv[1])

    if not directory.exists():
        print(Fore.RED + "Error: path does not exist." + Style.RESET_ALL)
        return

    if not directory.is_dir():
        print(Fore.RED + "Error: path is not a directory." + Style.RESET_ALL)
        return

    root_name = directory.resolve().name or str(directory.resolve())
    print(Fore.YELLOW + root_name + Style.RESET_ALL)
    print_tree(directory)


if __name__ == "__main__":
    main()
