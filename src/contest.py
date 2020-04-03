import pandas as pd
import numpy as np

import pyproj
from pyproj.crs.datum import CustomDatum, CustomEllipsoid


def solve(data):
    flights = data["flights"]

    df = pd.DataFrame(flights)

    s = ""
    for i, row in df.iterrows():
        x, y, z = gps_to_ecef(row["lat"], row["long"], row["altitude"])
        s += f"{x} {y} {z}\n"

    return s


def gps_to_ecef(latitude, longitude, altitude):
    # perfect sphere
    R, f = 6371000, 0

    cosLat = np.cos(latitude * np.pi / 180)
    sinLat = np.sin(latitude * np.pi / 180)

    cosLong = np.cos(longitude * np.pi / 180)
    sinLong = np.sin(longitude * np.pi / 180)

    c = 1 / np.sqrt(cosLat * cosLat + (1 - f) * (1 - f) * sinLat * sinLat)
    s = (1 - f) * (1 - f) * c

    x = (R * c + altitude) * cosLat * cosLong
    y = (R * c + altitude) * cosLat * sinLong
    z = (R * s + altitude) * sinLat

    return x, y, z
