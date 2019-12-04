import sys


def parse_input(input_file):
    parts = input_file.read().split('-')
    return int(parts[0]), int(parts[1])


def get_adjacents(digits):
    """
    >>> get_adjacents([1, 2, 3, 4])
    []

    >>> get_adjacents([1, 2, 2, 3])
    [[2, 2]]

    >>> get_adjacents([1, 2, 2, 2, 3])
    [[2, 2, 2]]

    >>> get_adjacents([1, 2, 2, 2, 3, 3])
    [[2, 2, 2], [3, 3]]

    >>> get_adjacents([1, 1, 2, 2, 2, 3, 3])
    [[1, 1], [2, 2, 2], [3, 3]]
    """

    last_digit = None
    result = []
    current = []

    for d in digits:
        if d == last_digit:
            if not len(current):
                current.append(d)
            current.append(d)
        elif len(current):
            result.append(current)
            current = []

        last_digit = d

    if len(current):
        result.append(current)

    return result


def is_valid_password(password):
    """

    111111 meets these criteria (double 11, never decreases).

    >>> is_valid_password(111111)
    True

    223450 does not meet these criteria (decreasing pair of digits 50).

    >>> is_valid_password(223450)
    False

    123789 does not meet these criteria (no double).

    >>> is_valid_password(123789)
    False
    """

    digits = [int(d) for d in list(str(password))]

    # It is a six-digit number.
    if len(digits) != 6:
        return False

    # Two adjacent digits are the same (like 22 in 122345).
    if not len(get_adjacents(digits)):
        return False

    # Going from left to right, the digits never decrease; they only ever
    # increase or stay the same (like 111123 or 135679).
    last_digit = -1
    for d in digits:
        if d < last_digit:
            return False

        last_digit = d

    return True


def validate_passwords(password_range, validator):
    return {p for p in password_range if validator(p)}


def main(input_file):
    min, max = parse_input(input_file)
    passwords = validate_passwords(range(min, max), is_valid_password)
    print(len(passwords))


if __name__ == '__main__':
    main(sys.stdin)
