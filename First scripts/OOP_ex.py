class person:
    pass


# MR Fattoh information
yes = ["y", "Y", "yes", "Yes"]
p1 = person()
p1.name = "fattoh"
p1.lastname = "alqurashy"
p1.age = 29
p1.date_of_birth = 1993

###moh information###

p2 = person()
p2.name = "mohammad"
p2.lastname = "alqurashy"
p2.age = 19
p2.date_of_birth = 1999

### Best friends ###

p1.bestfriend = p2.name
p2.bestfriend = p1.name

#############################################################
# PRINTER!!!!!!!!!

people = [p1, p2]
for p in people:
    print(p.name + " is " + str(p.age) + ' old, and born in ' + str(p.date_of_birth))

#####MORE INFO#####################


more_info = input("Do you want more info about them? y/n ")
if more_info == "y":
    print("Dr.fattoh " + p1.lastname + " best friend is " + p1.bestfriend)
    print("Also mohammed " + p2.lastname + " best friend is " + p2.bestfriend)
else:
    print("Ok thank you!")
