from pathlib import Path
import argparse


def manage_args():
    parser = argparse.ArgumentParser(description='Directory Tree Generator', formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('--dir',
                        default=None,
                        help='Directory to parse')

    return parser.parse_args()


def parse_dir(dir_path, tree_str=str(), level=1):
    if not tree_str:
        tree_str += dir_path.__str__()

    indent = '\n' + '|___ ' * level
    for sub_item in dir_path.iterdir():
        tree_str += indent + sub_item.name
        if sub_item.is_dir():
            tree_str = parse_dir(sub_item, tree_str, level + 1)

    return tree_str


# ----------------------- SCRIPT

args = manage_args()
if args.dir is None:
    print('No directory path provided')
    exit(1)

dir_path = Path(args.dir)
if not dir_path.is_dir():
    print(f'{dir_path} is not a directory')

tree_str = parse_dir(dir_path)
print(tree_str)
