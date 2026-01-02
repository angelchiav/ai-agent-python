from __future__ import annotations

from functions.get_file_content import get_file_content
from config import MAX_CHARS


def main() -> None:
    # 1) lorem truncation test
    content = get_file_content("calculator", "lorem.txt")
    print('get_file_content("calculator", "lorem.txt") length:', len(content))

    trunc_msg = f'[...File "lorem.txt" truncated at {MAX_CHARS} characters]'
    print("truncation message present:", trunc_msg in content)

    if trunc_msg in content:
        print("endswith truncation message:", content.endswith(trunc_msg))
    print()

    # 2) Print the required test cases
    print('get_file_content("calculator", "main.py")')
    print(get_file_content("calculator", "main.py"))
    print()

    print('get_file_content("calculator", "pkg/calculator.py")')
    print(get_file_content("calculator", "pkg/calculator.py"))
    print()

    print('get_file_content("calculator", "/bin/cat")')
    print(get_file_content("calculator", "/bin/cat"))
    print()

    print('get_file_content("calculator", "pkg/does_not_exist.py")')
    print(get_file_content("calculator", "pkg/does_not_exist.py"))
    print()


if __name__ == "__main__":
    main()