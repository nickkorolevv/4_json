import json
import requests

url = "https://devman.org/media/filer_public/1d/32/\
1d32132e-efa4-4a6c-bd32-312acc3710ad/alco_shops.json"


def write_json(data, filename="answer.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def pretty_json_print(url):
    response_object = requests.get(url).json()
    pretty_print = json.dumps(response_object, indent=2, ensure_ascii=False)
    return pretty_print


def main():
    print(pretty_json_print(url))


if __name__ == "__main__":
    main()
