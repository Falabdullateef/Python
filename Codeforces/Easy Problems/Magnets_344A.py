n = int(input()) # number of magnets to test

recent = 0
groups = 1

for i in range (n):
    current_magnet = int(input())
    current_magnet = 1 if current_magnet == 10 else -1 # 1 if last edge is +ve, -1 if last edge is -ve
 
    if i != 0: #accounting for the first iteration
        if current_magnet != recent: #repulsion
            groups += 1
            recent = current_magnet

    else:
        recent = current_magnet

print (groups)