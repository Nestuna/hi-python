import json
import random


def get_random_item_in_list(_list):
    return _list[random.randrange(len(_list))]


def read_json(path):
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f'Failed to read json {path}: {e}')
