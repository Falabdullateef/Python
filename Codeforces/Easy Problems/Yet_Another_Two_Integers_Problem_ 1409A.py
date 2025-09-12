iterations = int(input())
for _ in range(iterations):
    a, b = map(int, input().split())
    diff = abs(a - b)
    # Each move can change a by any value 1..10, so number of moves is ceil(diff/10)
    moves = (diff + 9) // 10  # integer ceiling for positive integers
    print(moves)