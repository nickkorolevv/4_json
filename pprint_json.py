import json
import sys
import os


def load_data(filepath):
    with open (filepath, "r", encoding="utf-8") as file_handler:
        try:
            return json.load(file_handler)
        except ValueError:
            return None


def pretty_json_print(decoded_json):
    pretty_print = json.dumps(decoded_json, indent=2, ensure_ascii=False)
    print(pretty_print)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        exit("Файл не выбран, пожалуйста выберите файл")
    if os.path.exists(filepath):
        decoded_json = load_data(filepath)
        if decoded_json is None:
            exit("Файл не является JSON объектом")
        else:
            pretty_json_print(decoded_json)
    else:
        exit("Файла нет в директории")

