def solve(data):
    flights = data["flights"]

    minTimestamp = min([f.timestamp for f in flights])
    maxTimestamp = max([f.timestamp for f in flights])
    minLat = min([f.lat for f in flights])
    maxLat = max([f.lat for f in flights])
    minLong = min([f.long for f in flights])
    maxLong = max([f.long for f in flights])
    maxAltitude = max([f.altitude for f in flights])

    return f"{minTimestamp:.0f} {maxTimestamp:.0f}\n" + \
           f"{minLat} {maxLat}\n" + \
           f"{minLong} {maxLong}\n" + \
           f"{maxAltitude}\n"
