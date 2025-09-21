t = int(input()) # test cases
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    for j in range(n):
        if len(a) == 1:
            print (a[0])
            continue

        new = a[0] + a[1] - 1
        a.pop(0)
        a.pop(0)
        a.append(new)
