n = int(input())

welfare = list(map(int, input().strip().split()))
welfare.sort()
max = max(welfare)

s = 0 #minimum number of burles to spend

for i in range (len(welfare)):
    if welfare[i] == max:
        continue
    s += max-welfare[i]

print(s)