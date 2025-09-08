iterations = int(input())
for i in range(iterations):
    nums = list(map(int, input().strip().split())) # removes whitespace and splits into list of integers properly
    nums.sort() # sorts in ascending order
    print(nums[1]) # print the middle number
