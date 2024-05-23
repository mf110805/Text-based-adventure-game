import random
print("this is working")
user_input = ""
user_input = input()
if user_input == "1":
    print("you died! don't shoot a nuclear bomb next time")
elif user_input == "2":
    print("placeholder")
    randomNumber = random.randint(0,1000000000)
    if randomNumber <= 500000000:
        print("they nuked you game over")
    else:
        print("you escaped their nuclear attack and have made it to the airport good job")
else:
    print("1 or 2, call it")