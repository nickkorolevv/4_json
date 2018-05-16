import json


def open_json(filepath="alco_shops.json"):
    with open (filepath, 'r', encoding='utf-8') as file_handler:
        return json.load(file_handler)

def pretty_json_print():
    pretty_print = json.dumps(open_json(), indent=2, ensure_ascii=False)
    print(pretty_print)


def main():
    pretty_json_print()

    
if __name__ == "__main__":
    main()

