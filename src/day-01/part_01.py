def get_fuel(mass):
    """
    Fuel required to launch a given module is based on its mass.
    Specifically, to find the fuel required for a module, take its mass,
    divide by three, round down, and subtract 2.

    For example:

    For a mass of 12, divide by 3 and round down to get 4,
    then subtract 2 to get 2.

    >>> get_fuel(12)
    2

    For a mass of 14, dividing by 3 and rounding down still yields 4,
    so the fuel required is also 2.

    >>> get_fuel(14)
    2

    For a mass of 1969, the fuel required is 654.

    >>> get_fuel(1969)
    654

    For a mass of 100756, the fuel required is 33583.

    >>> get_fuel(100756)
    33583
    """

    return int(mass / 3) - 2


def main(input_file):
    total = 0
    for line in input_file:
        total += get_fuel(int(line))

    print(total)


if __name__ == '__main__':
    import sys
    main(sys.stdin)
