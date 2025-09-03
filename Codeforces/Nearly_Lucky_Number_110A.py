n = input()
n = str(n) # convert to a string so that I loop the numbers within it
lucky = 0

#looping through the string n and checking if its a lucky digit
for i in range(len(n)):
    if n[i] == "4" or n[i] == "7":
        lucky += 1

if lucky == 7 or lucky == 4:
    print("YES")
else:
    print("NO")