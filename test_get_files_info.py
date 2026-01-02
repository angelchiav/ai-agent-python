from __future__ import annotations
from functions.get_files_info import get_files_info


def _indent_lines(s: str, spaces: int) -> str:
    prefix = " " * spaces
    return "\n".join(prefix + line for line in s.splitlines()) if s else ""


def _print_case(label: str, directory_label: str, result: str) -> None:
    print(label)
    print(directory_label)
    if result.startswith("Error:"):
        print(_indent_lines(result, 4))
    else:
        print(_indent_lines(result, 2))
    print()


def main() -> None:
    res = get_files_info("calculator", ".")
    _print_case(
        'get_files_info("calculator", "."):',
        "Result for current directory:",
        res,
    )

    res = get_files_info("calculator", "pkg")
    _print_case(
        'get_files_info("calculator", "pkg"):',
        "Result for 'pkg' directory:",
        res,
    )

    res = get_files_info("calculator", "/bin")
    _print_case(
        'get_files_info("calculator", "/bin"):',
        "Result for '/bin' directory:",
        res,
    )

    res = get_files_info("calculator", "../")
    _print_case(
        'get_files_info("calculator", "../"):',
        "Result for '../' directory:",
        res,
    )


if __name__ == "__main__":
    main()
