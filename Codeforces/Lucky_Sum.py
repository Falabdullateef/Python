sum = int(input())
# Noticed that n(7+4) = sum, then you start with 4s and then 7s

if sum % 11 != 0: # if its not divisible then that number DNE
    print(-1)

n = sum / 11  # solve for n

lucky = ""
for i in range(int(n)):
    lucky = "4" * (i + 1) + "7" * (i + 1)
print(lucky)
