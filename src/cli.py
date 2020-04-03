import os
from pprint import pprint
from collections import namedtuple

import pandas as pd
from parse import *
from contest import solve

FlightEntry = namedtuple("FlightEntry", "id timestamp")


def load(data):
    n = int(data[0])
    template = "{id:d} {timestamp:d}"
    flights = [FlightEntry(**parse(template, line).named) for line in data[1:]]

    return {
        "n": n, "flights": flights
    }


if __name__ == "__main__":
    level, quests = 4, 5
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
