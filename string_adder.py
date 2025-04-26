def add(s=""):
    if not s:
        return 0
    return sum([int(x) for x in s.split(",")])


