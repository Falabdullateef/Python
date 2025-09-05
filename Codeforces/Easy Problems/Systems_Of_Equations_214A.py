import math

# given n,m both positive\
# system a^2+b=n ; a+b^2=m

n, m = map(int, input().split())

total_solutions=0

# we iterate over all possible values of a
# realizing that a^2 must be <= n
for a in range(int(math.sqrt(n))+1): 
    b = n - a**2 # because b =n-a^2 from eq. 1
    if b >= 0 and a + b**2 == m: #check if b is valid from the eq. 2
        total_solutions += 1



print(total_solutions)