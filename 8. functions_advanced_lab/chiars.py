def combs(vals, index, count, comb):
    if len(comb) == count:
        print(comb)
        return
    for i in range(index, len(vals)):
        comb.append(vals[i])
        combs(vals, i + 1, count, comb)
        comb.pop()


