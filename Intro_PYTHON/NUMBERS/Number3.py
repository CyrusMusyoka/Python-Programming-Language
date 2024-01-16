Salary= input("Please enter your monthly salary: ")
bonus = input("Please enter your monthly bonus: ")

#monthly paycheckAmount and conversion of datatype since its reading the input as string
payCheckAmount = float(Salary)+float(bonus)
print(payCheckAmount)

#yearly paycheckamount and conversion of datatype since its reading the input as string
YearlyCheckAmount =  (float(Salary) + float(bonus))* 12
print(YearlyCheckAmount)
