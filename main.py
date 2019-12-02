from importlib import import_module
import argparse
import shutil
import requests
from os import path, makedirs
from secrets import AOC_SESSION_ID


def download_input(day, file_name, session_id=AOC_SESSION_ID):
    url = 'https://adventofcode.com/2019/day/{}/input'.format(day)
    cookies = {'session': AOC_SESSION_ID}
    with requests.get(url, cookies=cookies, stream=True) as r:
        r.raise_for_status()
        r.raw.decode_content = True  # Content is gzip-encoded
        with open(file_name, 'wb') as f:
            shutil.copyfileobj(r.raw, f)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--day', type=int, required=True)
    parser.add_argument('-p', '--part', type=int, action='append')
    args = parser.parse_args()

    day = args.day
    default_parts = [1, 2]
    parts = args.part or default_parts
    parts = list({p for p in parts if p in default_parts}) or default_parts
    parts.sort()

    input_dir = path.join(path.realpath(path.dirname(__file__)), 'input')
    makedirs(input_dir, exist_ok=True)

    input_file = path.join(input_dir, 'day-{:02d}.txt'.format(day))
    if not path.isfile(input_file):
        print('{} not cached. Downloading...'.format(input_file))
        download_input(day, input_file)
    else:
        print('Using cached input: {}'.format(input_file))

    print('')
    print('Day {:02d}'.format(day))
    print('===')

    for part in parts:
        print('')
        print('Part {:02d}:'.format(part))
        with open(input_file) as f:
            mod = 'src.day_{:02d}.part_{:02d}'.format(day, part)
            import_module(mod).main(f)


if __name__ == '__main__':
    main()
