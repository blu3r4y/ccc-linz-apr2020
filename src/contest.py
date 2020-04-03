import numpy as np
import pandas as pd

from util import load_trace


def solve(data):
    min_range, max_range, max_height = 1000, data["transfer_range"], 6000
    flights = data["flights"]

    # pre-cache all flight trajectories
    for flight in flights:
        load_trace(flight)

    for current in flights:
        for partner in flights:
            pass  # TODO

    return ""
