

addr = [
    "C6",
    "19",
    "88",
    "8A",
    "8C",
    "8E",
    "98",
    "9A",
    "9C",
    "9E",
    "A8",
    "AA",
    "AC",
    "AE",
    "B8",
    "BA",
    "BC",
    "BE",
    "C8",
    "CA",
    "CC",
    "CE",
    "D8",
    "DA",
    "DC",
    "DE",
    "E8",
    "EA",
    "EC"
    ]

for a in addr:
    value = int(a, 16)
    print("{:02X} -> {:02X}".format(value, int(float(value)/2)))