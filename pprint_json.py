import json
import requests

def get_json():
    data_file = "your_json_file"
    response_object = requests.get(data_file).json()
    return response_object


def pretty_json_print():
    pretty_print = json.dumps(get_json(), indent=2, ensure_ascii=False)
    return pretty_print


def main():
    print(pretty_json_print())

    
if __name__ == "__main__":
    main()
