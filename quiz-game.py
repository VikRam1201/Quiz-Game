print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play : ")


answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
    print("Correct!")

else:
    print("Wrong!") 

print("Next questions coming up!")

answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
    print("Correct!")

else:
    print("Wrong!") 

print("Next questions coming up!")

answer = input("What does GPU stand for? ")

if answer.lower() == "Graphics processing unit":
    print("Correct!")

else:
    print("Wrong!") 

print("Next questions coming up!")

answer = input("What does RAM stand for? ")

if answer.lower() == "Random access memory":
    print("Correct!")

else:
    print("Wrong!") 

print("Next questions coming up!")

answer = input("What does PSU stand for? ")

if answer.lower() == "power supply unit":
    print("Correct!")

else:
    print("Wrong!") 

print("Thanks for playing! Goodbye!")