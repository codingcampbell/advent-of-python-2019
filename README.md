# advent of code 2019 - Python 3

Because I've been writing JavaScript for nearly 20 years and I should get comfortable with modern Python I guess

This was written with Python 3.6.9 (PyPy 7.2.0) with absolutely no regard for backwards compatibility

## Getting Started

Likely in a virtualenv:

1. `pip install -r requirements.txt`
2. Set AOC_SESSION_ID in `secrets.py`
3. `python main.py -d 1`


This will download Day #1's input from Advent of Code and then run Day #1's code.

Each day has 2 parts (they both run by default). But you can specify a single part if you want:

```
# Just run Part 2 of Day 1
python main.py -d 1 -p 2
```

The individual scripts just read input from `stdin`, so if you don't want to use the magical fun things above, you can just invoke python manually and pass a file handle:

```
python -m src.day_01.part_02.py < day-01-input.txt
```


## Testing

Advent of Code practically phrases their story arc as a collection of unit tests. So each day is developed by converting their story blurb into doctests before attempting to process the real input.

I'm using pytest even though most tests will probably remain as standard doctests. Mostly because pytest has nice integration with VSCode

You can run the test suite like so:

```
pytest .
```

## I have no idea what I'm doing

I'm still learning, so don't assume anything you see here is idiomatic or intelligent. If you're able to help me, please send improvements in PRs or slide into my DMs if we're tight like that.

## Links

- [Advent of Code 2019](https://adventofcode.com/2019)
- [Python 3](https://docs.python.org/3/)
- [PyPy](https://pypy.org/)
- [pip and virtualenvs](https://docs.python.org/3/installing/index.html)
- [doctests](https://docs.python.org/3/library/doctest.html)
- [pytest](https://docs.pytest.org/en/latest/)
- [VSCode](https://code.visualstudio.com/)
- [Me](https://mattcampbell.net)
