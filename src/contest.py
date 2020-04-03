import pandas as pd


def solve(data):
    flights = data["flights"]

    df = pd.DataFrame(flights)

    # ensure unique
    df.drop_duplicates(["start", "destination", "takeoff"], inplace=True)
    # group by start, dest and count
    groups = df.groupby(["start", "destination"]).size().reset_index(name="counts")
    # sort by start, then by dest
    groups.sort_values(by=["start", "destination"], inplace=True)

    lines = [f"{row['start']} {row['destination']} {row['counts']}" for i, row in groups.iterrows()]
    return "\n".join(lines)
