from collections import namedtuple
from functools import lru_cache

import numpy as np
import pandas as pd

from parse import *

Sample = namedtuple("Sample", "offset lat long alt")


@lru_cache(maxsize=None)
def load_trace(flight_id):
    csv_path = r'..\tmp\{}.csv'.format(flight_id)
    with open(csv_path, 'r') as fi:
        data = fi.read().splitlines()

        # parse sampled trajectories
        trajectory = [Sample(**parse("{offset:d},{lat:f},{long:f},{alt:f}", line).named) for line in data[4:]]

        # attach timedelta index
        df = pd.DataFrame(trajectory, dtype="float32")
        df["offset"] = pd.TimedeltaIndex(df["offset"], unit="s")
        df.set_index("offset", inplace=True)

        # up-sample and interpolate to 1sec intervals
        df = df.resample("1s").asfreq().interpolate("linear")

        df["x"], df["y"], df["z"] = gps_to_ecef(df["lat"], df["long"], df["alt"])

        return {
            "start": data[0],
            "end": data[1],
            "takeoff": int(data[2]),
            "trajectory": df
        }


@np.vectorize
def gps_to_ecef(lat, long, alt):
    # perfect earth sphere with no flattening
    R = 6371000

    cosLat = np.cos(lat * np.pi / 180)
    sinLat = np.sin(lat * np.pi / 180)

    cosLong = np.cos(long * np.pi / 180)
    sinLong = np.sin(long * np.pi / 180)

    c = 1 / np.sqrt(cosLat * cosLat + sinLat * sinLat)
    f = (R * c + alt)

    x = f * cosLat * cosLong
    y = f * cosLat * sinLong
    z = f * sinLat

    return x, y, z
