#ifstatement userRead

answer = "yes"

userAnswer = input("Would you like exoress shipping? ")
if userAnswer.lower() == answer:
#.lower()/.upper() function allows the user to input the data in any case ,they call for string variables
    print("That will be an extra $10.")
    print("Have a nice day")
