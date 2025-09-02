sum = int(input())
# n(7+4) = sum

if sum % 11 != 0: # if its not divisible then that number DNE
    print(-1)

n = sum / 11  # solve for n

# n=2
lucky = ""
for i in range(int(n)):
    lucky = "4" * (i + 1) + "7" * (i + 1)
print(lucky)
