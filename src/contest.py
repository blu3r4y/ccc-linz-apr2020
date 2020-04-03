import numpy as np
import pandas as pd
from util import load_trace


def solve(data):
    flights = data["flights"]

    s = ""

    for flight in flights:
        trace = load_trace(flight.id)
        df = pd.DataFrame(trace["traces"], dtype=np.float32)
        df.sort_values("offset", inplace=True)  # ensure sorted

        value = flight.timestamp - trace["takeoff"]

        # check direct match
        if np.any(df["offset"] == value):
            lat, long, alt = df[df["offset"] == value].iloc[0, :][["lat", "long", "alt"]]
            s += f"{lat} {long} {alt}\n"
        else:
            # find nearest timestamps
            off1, lat1, long1, alt1 = df[df["offset"] < value].iloc[-1, :][["offset", "lat", "long", "alt"]]
            off2, lat2, long2, alt2 = df[df["offset"] > value].iloc[0, :][["offset", "lat", "long", "alt"]]

            lat = interp(value, [off1, off2], [lat1, lat2])
            long = interp(value, [off1, off2], [long1, long2])
            alt = interp(value, [off1, off2], [alt1, alt2])

            s += f"{lat} {long} {alt}\n"

    return s


def interp(x, xs, ys):
    x = float(x)
    x0, x1 = xs
    y0, y1 = ys
    return y0 + (x - x0) * ((y1 - y0) / (x1 - x0))
