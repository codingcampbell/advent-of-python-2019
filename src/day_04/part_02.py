import sys

from .part_01 import parse_input, validate_passwords
from .part_01 import is_valid_password, get_adjacents


def strict_validator(password):
    """
    An Elf just remembered one more important detail: the two adjacent
    matching digits are not part of a larger group of matching digits.


    112233 meets these criteria because the digits never decrease and all
    repeated digits are exactly two digits long.

    >>> strict_validator(112233)
    True

    123444 no longer meets the criteria (the repeated 44 is part of a larger
    group of 444).

    >>> strict_validator(123444)
    False

    111122 meets the criteria (even though 1 is repeated more than twice, it
    still contains a double 22).

    >>> strict_validator(111122)
    True
    """

    if not is_valid_password(password):
        return False

    digits = [int(d) for d in list(str(password))]
    return any(len(adj) == 2 for adj in get_adjacents(digits))


def main(input_file):
    min, max = parse_input(input_file)
    passwords = validate_passwords(range(min, max), strict_validator)
    print(len(passwords))


if __name__ == '__main__':
    main(sys.stdin)
