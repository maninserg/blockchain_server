import json
import os
import hashlib


blockchain_dir = os.curdir + "/blockchain/"


def get_blocks():
    list_blocks = os.listdir(blockchain_dir)
    return sorted([int(x) for x in list_blocks])


def get_hash(filename):
    fl = open(blockchain_dir + filename, "rb").read()
    return hashlib.sha256(fl).hexdigest()


def check_blocks():
    list_blocks = get_blocks()
    results = []
    for block in list_blocks[1:]:
        hash_read = json.load(open(blockchain_dir + str(block)))["hash"]
        prev_block = str(block - 1)
        hash_calc = get_hash(prev_block)
        if hash_read == hash_calc:
            result = "Ok"
        else:
            result = "Corrupted"
        results.append({"block": prev_block, "result": result})
    return results


def write_block(name, amount, to_whom, prev_hash=""):
    list_blocks = get_blocks()
    prev_block = list_blocks[-1]
    cur_block = str(prev_block + 1)
    prev_hash = get_hash(str(prev_block))
    data = {"name": name,
            "amount": amount,
            "to_whom": to_whom,
            "hash": prev_hash}
    with open(blockchain_dir + cur_block, "w") as fl:
        json.dump(data, fl, indent=4, ensure_ascii=False)


def main():
    write_block(name="vladimir", amount=210, to_whom="kukuz")


if __name__ == "__main__":
    # main()
    check_blocks()
