import json


def write_block():
    data = {"name": "ivan",
            "amount": 5,
            "to_whom": "vasja",
            "hash": "123"}
    with open ("test", "w") as fl:
        json.dump(data, fl, indent=4, ensure_ascii=False)


def main():
    write_block()

if __name__ == "__main__":
    main()
