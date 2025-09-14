t = int(input())

def area(a, b):
    d = abs(a - b)
    return d * d

for i in range(t):
    points = [tuple(map(int, input().split())) for j in range(4)] # tuples makes it ordered
    x_vals = {p[0] for p in points}
    y_vals = {p[1] for p in points}
    # Side is difference between distinct x's (or y's)
    if len(x_vals) == 2:
        x_list = list(x_vals)
        print(area(x_list[0], x_list[1]))
    else:
        y_list = list(y_vals)
        print(area(y_list[0], y_list[1]))