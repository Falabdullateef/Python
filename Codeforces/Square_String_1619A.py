import math

iterations = int(input())

for i in range(iterations):
    stringin = input()
    sqrt_len = math.sqrt(len(stringin))
    if sqrt_len.is_integer():  # Check if sqrt_len is an integer
        substring = stringin[:int(sqrt_len)]
        if substring * int(sqrt_len) == stringin:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")