def add(s=""):
    delimiter = ','
    if s[:2] == "//":
        delimiter = s[2]
        s = s[4:]
    if not s:
        return 0
    nums = []
    cur_num = ''
    for c in s:
        if c == delimiter or c == '\n':
            nums.append(int(cur_num))
            cur_num = ''
        else:
            cur_num += c
    if cur_num:
        nums.append(int(cur_num))
    return sum(nums)


