# https://codeforces.com/problemset/problem/1593/A
n = int(input())

for i in range(n):
    contestants = list(map(int, input().split()))
    min_votes = max(contestants) + 1
    # simply realize that each contestant needs to have at least one vote more than the current winner
    results = []
    max_votes = max(contestants)
    for j in range(len(contestants)):
        if contestants[j] == max_votes and contestants.count(max_votes) == 1: #important to check if there is a tie
            results.append('0')
        else:
            results.append(str(max_votes - contestants[j] + 1))
    print(' '.join(results))