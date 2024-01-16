#combining both "and" and "or" in a single statement

teams = input("What is your EPL Team? ").upper()
sport = input("What is your favourate sport? ").upper()

if teams == "CHELSEA" and sport == "FOOTBALL" or sport == "RUGBY" :
    print("Good luck getting to win cup this year.")

else:
    print("Try again next time, you missed !!!!")

# anotherway is

teamisCorrect = False
if teams == "CHELSEA" :
    teamisCorrect = True

sportisCorrect = False
if sport == "FOOTBALL" :
    sportisCorrect = True
    print("Good luck getting to win cup this year.")

else:
    print("Try again next time, you missed !!!!")
