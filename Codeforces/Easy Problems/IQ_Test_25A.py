iterations = int(input())
numbers = list(map(int, input().split()))

even = 0
odd = 0
for i in range(iterations):
    if numbers[i] % 2 == 0: # even
        even += 1
    else:
        odd += 1

# Find and print the index of the unique one
if even == 1:
    for i in range(iterations):
        if numbers[i] % 2 == 0:
            print(i + 1) # 1-based indexing
            break
else:
    for i in range(iterations):
        if numbers[i] % 2 == 1:
            print(i + 1) # 1-based indexing
            break