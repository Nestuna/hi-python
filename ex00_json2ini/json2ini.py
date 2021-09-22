import json


def create_ini(path):
    with open(ini_file, 'w') as f:
        f.write('')


def write_ini(data_str, path):
    with open(path, 'a') as f:
        f.write(data_str + '\n')


def read_json(path):
    with open(path, 'r') as f:
        return json.load(f)


def parse_data(data, parent=str()):
    if isinstance(data, dict):
        for key, val in data.items():
            if isinstance(val, str):
                keyvalue_str = f'{key}={val}'
                write_ini(keyvalue_str, ini_file)
            if isinstance(val, dict):
                parent_str = str()
                if parent:
                    parent_str = f'{parent}.'
                level_str = f'\n[{parent_str}{key}]'
                write_ini(level_str, ini_file)
                parse_data(val, parent=key)
            if isinstance(val, list):
                for item in val:
                    keyvalue_str = f'{key}[]={str(item)}'
                    write_ini(keyvalue_str, ini_file)


def json_to_ini(json_path, ini_path):
    json_dict = read_json(json_path)
    create_ini(ini_path)
    parse_data(json_dict)


#----- SCRIPT

ini_file = 'test.ini'
json_file = 'test.json'
json_to_ini(json_file, ini_file)
