

def solve(value):
    return sorted(value, key=lambda r: (-r["score"], r["name"]))
