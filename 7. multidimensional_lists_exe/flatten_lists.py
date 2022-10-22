ll = input().split("|")
ll_flat = []

for i in range(len(ll)-1, -1, -1):
    sublists = ll[i].split()
    ll_flat += sublists

print(' '.join(ll_flat))
