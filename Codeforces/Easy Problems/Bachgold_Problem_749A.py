n = int(input())
# 5
# 2 3
# 2n + 3n = 5
# simple maximize minimize problem
# max: 2s min: 3s to increase k

# 64
# 63

if n % 2 == 0:
    array_primes = [2] * (n // 2)
else:
    array_primes = [2] *((n-3)//2)
    array_primes.append(3)

print(len(array_primes))
print(*array_primes)