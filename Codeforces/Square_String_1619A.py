iterations = int(input())

for i in range(iterations):
    stringin = input()
    length = len(stringin)
    if length % 2 == 0:  # Check if the length is even for ex. "aa"
        half = length // 2
        if stringin[:half] == stringin[half:]:  # Compare the two halves
            print("YES")
        else:
            print("NO")
    else:
        print("NO")