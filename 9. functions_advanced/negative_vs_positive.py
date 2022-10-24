def find_bigger_sum(*args):
    positives_sum = sum(x for x in args if x >= 0)
    negatives_sum = sum(x for x in args if x < 0)
    return positives_sum, negatives_sum


nums = list(map(int, input().split()))

result = find_bigger_sum(*nums)

print(result[1])
print(result[0])
if abs(result[1]) > abs(result[0]):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
