import json
import os


def get_filepath():
    way_to_file = os.path.abspath(os.curdir) + "\\"
    filepath = way_to_file + input("Введите название файла \n")
    return filepath


def load_data():
    filepath = get_filepath()
    with open (filepath, 'r', encoding='utf-8') as file_handler:
        return json.load(file_handler)


def pretty_json_print():
    data_file = load_data()
    pretty_print = json.dumps(data_file, indent=2, ensure_ascii=False)
    print(pretty_print)


def main():
    pretty_json_print()


if __name__ == "__main__":
    main()

