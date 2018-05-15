import json
import requests


def pretty_json_print(data_file):
    response_object = requests.get(data_file).json()
    pretty_print = json.dumps(response_object, indent=2, ensure_ascii=False)
    return pretty_print


def main():
    data_file = "https://devman.org/media/filer_public/1d/32/\
1d32132e-efa4-4a6c-bd32-312acc3710ad/alco_shops.json"
    print(pretty_json_print(data_file))

    
if __name__ == "__main__":
    main()

