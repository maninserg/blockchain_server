import json
import os


def write_block(name, amount, to_whom, prev_hash=""):
    blockchain_dir = os.curdir + "/blockchain/"
    list_blocks = os.listdir(blockchain_dir)
    list_blocks = sorted([int(x) for x in list_blocks])
    last_block = list_blocks[-1]
    cur_block = str(last_block + 1)
    data = {"name": name,
            "amount": amount,
            "to_whom": to_whom,
            "hash": prev_hash}
    with open (blockchain_dir + cur_block, "w") as fl:
        json.dump(data, fl, indent=4, ensure_ascii=False)


def main():
    write_block(name="ivan", amount=124, to_whom="serg", prev_hash="3423dfd")

if __name__ == "__main__":
    main()
