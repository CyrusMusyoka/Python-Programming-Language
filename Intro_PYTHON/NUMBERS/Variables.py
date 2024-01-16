#collect name from user
firstName = input("Enter your first name:")
lastName = input("Enter your last name:")
country = input("What is your country:")
country = country.upper()

#display on screen by combining fname and lname by concatination sign "+"
print("Hello "+firstName+" " + lastName+" " +'You live in'+ country)