n = int(input())

parts = []

for i in range(n):
    if i % 2 != 0: 
        parts.append("I love")
    else:
        parts.append("I hate")
    
    if i != n-1:
        parts.append("that")

parts.append("it")

print(" ".join(parts))