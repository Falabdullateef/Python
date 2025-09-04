import math

iterations = int(input())

for i in range(iterations):
    stringin = input() #aa
    sqrt_len = math.sqrt(len(stringin))
    if sqrt_len - int(sqrt_len) == 0:
        # Check if the string is made of repeated substrings of length sqrt
        if stringin[0:int(sqrt_len)] * int(sqrt_len) == stringin:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")