import sys
from .part_01 import get_fuel


def get_total_fuel(mass):
    """
    A module of mass 14 requires 2 fuel. This fuel requires no further
    fuel (2 divided by 3 and rounded down is 0, which would call for
    a negative fuel), so the total fuel required is still just 2.

    >>> get_total_fuel(14)
    2

    At first, a module of mass 1969 requires 654 fuel. Then, this fuel
    requires 216 more fuel (654 / 3 - 2). 216 then requires 70 more fuel,
    which requires 21 fuel, which requires 5 fuel, which requires no further
    fuel. So, the total fuel required for a module of mass 1969 is
    654 + 216 + 70 + 21 + 5 = 966.

    >>> get_total_fuel(1969)
    966

    The fuel required by a module of mass 100756 and its fuel is:
    33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346.

    >>> get_total_fuel(100756)
    50346
    """

    total = get_fuel(mass)
    additional = total

    while additional:
        more = get_fuel(additional)
        additional = more if more > 0 else 0
        total += additional

    return total


def main(input_file):
    total = 0
    for line in input_file:
        total += get_total_fuel(int(line))

    print(total)


if __name__ == '__main__':
    main(sys.stdin)
