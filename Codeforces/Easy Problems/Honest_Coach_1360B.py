
t = int(input())
for _ in range(t):
    n = int(input())
    strengths = list(map(int, input().split())) #ex. 4 1 8 7
    strengths.sort() # 1 4 7 8
    # start with a large number so first comparison works.
    min_diff = float('inf')
    for i in range(1, n):
        diff = strengths[i] - strengths[i - 1]
        if diff < min_diff:
            min_diff = diff
    print(min_diff)