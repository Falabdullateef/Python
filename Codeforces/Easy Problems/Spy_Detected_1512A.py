t = int(input())

for i in range (t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    a_sort = sorted(a)
    # 2 probabillities: its max or min
    find = 0
    if max(a_sort) == a_sort[n-2]: # ex 10 11 11 11
        find = min(a_sort)
    else:
        find = max(a_sort)
    for j in range(n):
        if a[j] == find:
            print(j+1)