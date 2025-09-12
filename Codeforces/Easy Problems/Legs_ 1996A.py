# n = 2chick + 4cow

iterations = int(input())
for i in range(iterations):
    n = int(input())

    cow_number = n // 4 # maximized here to minimize number of animals. // means integer division
    chicken_number = 0

    if n % 4 !=0: # meaning that there must be chickens
        remainder = n % 4
        chicken_number = remainder // 2 # remainder must be a multiple of 2 so we can divide it by 2 to get the number of chickens
    print(chicken_number+cow_number)