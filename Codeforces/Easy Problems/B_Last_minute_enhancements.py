t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    # a is already sorted from input
    
    if n == 1:
        print(1)
        continue

    diversity = 0
    done = set()
    for j in range(n): #looping thorugh the list
        if a[j] not in done:
            diversity += 1
            done.add(a[j])
        elif a[j] + 1 not in done:
            diversity += 1
            done.add(a[j] + 1)

    print(diversity)
