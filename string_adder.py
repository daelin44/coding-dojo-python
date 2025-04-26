def add(s=""):
    if not s:
        return 0
    nums = []
    cur_num = ''
    for c in s:
        if c == ',' or c == '\n':
            nums.append(int(cur_num))
            cur_num = ''
        else:
            cur_num += c
    if cur_num:
        nums.append(int(cur_num))
    return sum(nums)


