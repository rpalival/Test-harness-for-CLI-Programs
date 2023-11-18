#!/opt/homebrew/bin/python3
import json
import argparse
import sys

def flatten_json(obj, name='json'):
    def recurse(t, parent_key=''):
        if isinstance(t, dict):
            if not parent_key:
                print(f"{name} = {{}};")
            else:
                print(f"{name}{parent_key} = {{}};")
            for key, value in t.items():
                recurse(value, f"{parent_key}.{key}" if parent_key else f".{key}")
        elif isinstance(t, list):
            print(f"{name}{parent_key} = [];")
            for i, item in enumerate(t):
                recurse(item, f"{parent_key}[{i}]")
        else:
            print(f"{name}{parent_key} = {json.dumps(t)};")

    recurse(obj)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', nargs='?')
    #EXTENSION #3: to allow for different base object other than default json.
    parser.add_argument('--obj', default='json', help='Specify a different base object name')
    args = parser.parse_args()

    try:
        if args.filename:
            with open(args.filename, 'r') as file:
                json_data = json.load(file)
        else:
            json_data = json.load(sys.stdin)

        flatten_json(json_data, name=args.obj)
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()