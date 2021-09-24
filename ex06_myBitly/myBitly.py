import json
from pathlib import Path
import argparse
import string
from random import randrange

REDIRECTION_FILENAME = Path('redirections.json')
BASE_SHORT_URL = 'https://my-shortener/'
URL_PATH_LENGTH = 8


def read_redirections(path):
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except IOError:
        data = dict()
        write_redirections(data)
        return data
    except Exception as e:
        print(f'Failed to read json {path}: {e}')


def write_redirections(data):
    try:
        with open(REDIRECTION_FILENAME, 'w') as f:
            json.dump(data, f)
    except Exception as e:
        print(f'Failed to write redirections file {REDIRECTION_FILENAME}: {e}')


def manage_args():
    parser = argparse.ArgumentParser(description='URL shortener', formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('--url',
                        default=None,
                        help='add custom config file.')

    return parser.parse_args()


def short_url(url):
    short_url = str()
    if url:
        short_url = BASE_SHORT_URL + generate_random_path()
    return short_url


def generate_random_path():
    path = str()
    chars = string.ascii_letters + string.digits
    for _ in range(URL_PATH_LENGTH):
        path += chars[randrange(len(chars))]
    return path


# ----------------------- SCRIPT

args = manage_args()
if args.url is None:
    print('No url provided')
    exit(1)
else:
    long_url = args.url
    redirections = read_redirections(REDIRECTION_FILENAME)
    if long_url not in redirections.keys():
        print('Url not in database. Computing short url.')
        redirections[long_url] = short_url = short_url(args.url)
        write_redirections(redirections)
    else:
        print('Found url redirection.')
        short_url = redirections[long_url]

    print(f'Short url : {short_url}')
