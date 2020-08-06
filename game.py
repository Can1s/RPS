import random

rps = ["rock", "scissors", "paper"]
user = input()
rnd = random.choice(rps)
if user.__eq__(rnd):
    print(f"There is a draw ({user})")
else:
    if user.__eq__("rock") and rnd.__eq__("scissors"):
        print(f"Well done. Computer chose {rnd} and failed")
    elif user.__eq__("scissors") and rnd.__eq__("paper"):
        print(f"Well done. Computer chose {rnd} and failed")
    elif user.__eq__("paper") and rnd.__eq__("rock"):
        print(f"Well done. Computer chose {rnd} and failed")
    else:
        print(f"Sorry, but computer chose {rnd}")
