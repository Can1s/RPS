import random


rps = ["rock", "scissors", "paper"]
rating = 0
rating_list = []
file = open('rating.txt', 'r')


name = input("Enter your name: ")
print(f"Hello, {name}")
for lin in file:
    rating_list.append(lin.replace("\n", "").split(" "))
if rating_list.__contains__(name):
    for obj in rating_list:
        if obj[0][0] == name:
            rating = int(obj[0][1])
            break


while True:
    user = input()
    rnd = random.choice(rps)
    if user.__eq__("!exit"):
        print("Bye!")
        break
    elif user.__eq__("!rating"):
        print(f"Your rating: {rating}")
    elif user.__eq__("rock") or user.__eq__("scissors") or user.__eq__("paper"):
        if user.__eq__(rnd):
            print(f"There is a draw ({user})")
            rating += 50
        else:
            if user.__eq__("rock") and rnd.__eq__("scissors"):
                print(f"Well done. Computer chose {rnd} and failed")
                rating += 100
            elif user.__eq__("scissors") and rnd.__eq__("paper"):
                print(f"Well done. Computer chose {rnd} and failed")
                rating += 100
            elif user.__eq__("paper") and rnd.__eq__("rock"):
                print(f"Well done. Computer chose {rnd} and failed")
                rating += 100
            else:
                print(f"Sorry, but computer chose {rnd}")
    else:
        print("Invalid input")
