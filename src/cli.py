import os
from pprint import pprint

from contest import solve


def load(data):
    transfer_range = float(data[0])
    flights = list(map(int, data[2:]))

    return {
        "transfer_range": transfer_range, "flights": flights
    }


if __name__ == "__main__":
    level, quests = 5, 5
    for q in range(1, quests + 1):
        input_file = r'..\data\level{0}\level{0}_{1}.in'.format(level, q)
        output_file = os.path.splitext(input_file)[0] + ".out"

        with open(input_file, 'r') as fi:
            data = load(fi.read().splitlines())
            # pprint(data)

            print("=== Input {}".format(q))
            print("======================")

            result = solve(data)
            pprint(result)

            with open(output_file, 'w+') as fo:
                fo.write(result)
