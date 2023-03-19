#Capstone Task:
#This project is based on creating a program for a financial company to determine input from their users.

#----Setting variables to be used for this program----:
company_title="Welcome to Prodigy Financial Services Ltd."  
empty_string=" "
menu_title="Please select either 'investment' or 'bond' from the menu to proceed:"
menu_selection="investment     -to calculate the amount of interest you'll earn on interest\nbond           -to calculate the amount you'll have to pay on a home loan"

#------Print variables as menu title-----------
print(company_title.center(90,"~"))
print(menu_title)
print(empty_string)
print(menu_selection)
print(empty_string)
user_input=input()
print(empty_string)

#---------------The below code determines the user's total interest (Simple and Compound interest)------------
#The code function 'len' executes the user's input NOT to be case sensitive
#The code function elif executes the flow of logic and prints the total using the appropriate formula's
import math
if len(user_input)==10:
    deposit_amount=float(input("How much money are you depositing in rands?\n"))
    interest_rate=float(input("What is the interest rate % ?\n"))
    nr_years_invest=float(input("How many years would you like to invest for?\n"))
    interest=input("Would you like simple or compound interest? (please choose either 'simple' or 'compound')\n")
    if len(interest)==6:
        interest_simple=((deposit_amount)*(1+(interest_rate/100)*(nr_years_invest)))
        print("\nYour total investment amount will be: R{}".format(round(interest_simple,2)))
    elif len(interest)==8:
        interest_compound=(deposit_amount*math.pow((1+(interest_rate/100)),nr_years_invest))
        print("\nYour total investment amount will be: R{}".format(round(interest_compound,2)))
    else:
        print("Input error: Please ensure you choose the correct input ('simple' or 'compound'.)")    

#-------------------The below code determines the user's bond repayment---------------------------
#The code executes the flow of logic and prints the total using the appropriate formula
elif len(user_input)==4:
        house_value=float(input("What is the present value of your house in rands?\n"))
        interest_rate2=float(input("What is the interest rate in %?\n"))
        bond_months=float(input("How many months do you plan to take to repay your bond?\n"))
        interest_bond=(((interest_rate2/12)*(house_value))/(1-(1+(interest_rate2/12)*(-bond_months))))
        print("The total amount you will need to repay each month is R{}".format(round(interest_bond),2))
else:
    print("Input error: Please ensure you choose the correct input ('bond' or 'investment'.)")

#---------Print end message after calculations----------
print(empty_string)
print("Thanks for choosing Prodigy Financial Services Ltd!".center(80,"~"))
