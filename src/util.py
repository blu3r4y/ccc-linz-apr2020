from parse import *
from collections import namedtuple

Trace = namedtuple("Trace", "offset lat long alt")


def load_trace(flight_id):
    csv_path = r'..\tmp\{}.csv'.format(flight_id)
    with open(csv_path, 'r') as fi:
        data = fi.read().splitlines()

        start = data[0]
        end = data[1]
        takeoff = int(data[2])
        n = int(data[3])

        template = "{offset:d},{lat:f},{long:f},{alt:f}"
        traces = [Trace(**parse(template, line).named) for line in data[4:]]

        return {
            "start": start, "end": end, "takeoff": takeoff, "n": n, "traces": traces
        }
