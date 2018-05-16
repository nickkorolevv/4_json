import json
import sys


def load_data(filepath):
    with open (filepath, 'r', encoding='utf-8') as file_handler:
        return json.load(file_handler)


def pretty_json_print(filename):
    pretty_print = json.dumps(filename, indent=2, ensure_ascii=False)
    print(pretty_print)


def main():
    dataname = load_data(filepath)
    pretty_json_print(dataname)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        filepath = format(sys.argv[1])
    else:
        filepath = input("Укажите путь до json файла: ")
    main()

