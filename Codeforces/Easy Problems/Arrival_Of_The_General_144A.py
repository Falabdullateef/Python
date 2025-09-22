def swap(i, j, lst):
    lst[i], lst[j] = lst[j], lst[i]
    return lst

n = int(input())
a = list(map(int, input().split()))

maxi = 0
mini = 0
swaps = 0

max_val = a[0]
min_val = a[0]

for i in range(n):
    if a[i] > max_val:
        max_val = a[i]
        maxi = i
    if a[i] <= min_val:
        min_val = a[i]
        mini = i
if maxi > mini:
    swaps = maxi + (n - 1 - mini) - 1
else:
    swaps = maxi + (n - 1 - mini)
print(swaps)