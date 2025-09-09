allowed = set("codeforces") # learned what set is, it removes duplicates
iterations = int(input())

for i in range(iterations):
    string = input().strip()
    print("YES" if string[0] in allowed else "NO")
