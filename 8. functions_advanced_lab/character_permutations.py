def permute(ind, val):
    if ind == len(val):
        print("".join(val))
        return
    for i in range(ind, len(val)):
        val[i], val[ind] = val[ind], val[i]
        permute(ind+1, val)
        val[i], val[ind] = val[ind], val[i]


values = list(input())
index = 0
permute(index, values)