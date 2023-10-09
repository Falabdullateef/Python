print("Welcome to my small quiz")
choice = input("Do you want to play my quiz? ")
if choice.lower() == "yes":
    print ("Alright then let's play!")
else:
    print("Alright no problem.")
    quit()
answer = input("What is the most famous programing laungage? ")
if answer == 'python':
    print("Correct!")
else:
    print("Incorrect, nice try.")
answer = input("What is Faisal's school name? ")
if answer == 'x school':
    print("Correct!")
else:
    print("Incorrect, nice try.")
answer = input("What Faisal's best number ")
if answer == '19':
    print("Correct!")
else:
    print("Incorrect, nice try.")
print("Thank you for playing my small quiz, hope you enjoyed :)")