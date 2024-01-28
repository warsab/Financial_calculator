# Calculator

# Import library to use for diving by zero error:
from decimal import DivisionByZero

# Setting program title and style:
calc_title = "Online Pocket Calculator \U0001F5A9"
underline = "=" * len(calc_title)

# Printing the program title:
print(f"{underline}\n{calc_title}\n{underline}\n")

#========================================= Defining 'main_menu' function:
'''
    Displays the main menu options and navigates to the selected functionality
    of a calculator

    Parameters:
    - option (str): This is a default value so when the function is called no
    argument is needed to pass

    Functionality:
    - for options 'c','e', it will call for a specific defined function(created within this program).
    - For option 'v' it will open the equations.txt file and display the user's saved results.
      Using iteration ,it will read each line in the text file and will display chronologically.

    Defensive programming:
    - Using a series of if/elif/else statements to anticipate incorrect entries from user
    - Also using exception to handle if user wants to view file but it has not yet being created.
'''
def main_menu(option = ''):
        if option == '':
            menu = input('''=============== Enter Program: ================
Please select the following options:
Calculator   - enter "c"
View results - enter "v"
Exit         - enter "e"\n>''').lower()
        else:
            menu = option

        if menu=="c":
            my_calculator()

        elif menu=="e":
            exit_menu()

        elif menu == "v":
            my_results = input("\nWhat is the name of the text file you would like to open?\n> ").lower()
            if my_results == "equations":
                try:
                    with open("equations.txt", "r") as f:
                        i = 0
                        file = f.readlines()
                    for lines in file:
                        x = lines.split()
                        i += 1
                        print(f"\n=============== Equation {i}: ================\n{lines}")
                    main_menu(option='')
                except FileNotFoundError: # If file has not been created yet
                    print("\nERROR ====> The 'equations.txt' file was not found.\nPlease add calculations to populate.\n")
                    main_menu(option = '')
            else:
                print("\nERROR ====> Sorry, no such file found.\nPlease try again.\n")
                main_menu(option = 'v')
        else:
            print("Input invalid! Please select a valid entry\n")
            print(main_menu(option = ''))    
#========================================= Defining 'exit_menu' function:
# This code allows user to exit the program:               
def exit_menu():
  print('\nThanks Goodbye!!!')
  exit()

#===================================== Defining 'my_calculator' function:
'''
    This function prompts the user to input two numbers and performs basic calculations.
    The user's input will be saved to variables 'first number,'second_number'

    Defensive programming:
    - Using exception handling to anticipate user's invalid input
'''
def my_calculator():
    print("\n======= Welcome! Let's get calculating! ======")

    try:
        first_number = float(input("Please enter your first number:\n> "))
    except ValueError:
        print("\nERROR ====> Sorry,you have not entered in a number.\nPlease try again\n")
        my_calculator()

    try:
        second_number = float(input("Please enter your second number:\n> "))
    except ValueError:
        print("\nERROR ====> Sorry,you have not entered in a number:\nStart over again!\n")
        my_calculator()

#========================================= User interface calculation:
# For the below code this section will allow the user to do calculations
# All operations will be saved into the list 'my_data'
# Exception handling implemented to anticipate incorrect user values
        
# Printing calculation options:
    print("=============== Operation selection: ===============")
    operation = (input('''Please enter the operation you would like to use:
Multiply:   (select:'x')
Divide:     (select:'/')
Subtract:   (select:'-')
Add:        (select:'+')
Modulo:     (select:'%')
\n>''')).lower()

# Setting 'my_data' as empty list:
    my_data=[]

    # Multiplication calculation:
    if operation == "x": 
        multiply = first_number * second_number
        multiply = round(multiply, 2)
        print("============================= Results:")
        multiply_output=(f"Your result: {first_number} x {second_number} = {multiply}")
        print(multiply_output)
        my_data.append(multiply_output)

    # Division calculation:
    elif operation == "/":
        try:
            divide = first_number / second_number
            divide = round(divide, 2)
            print("============================= Results:")
            div_sum = (f"Your result: {first_number} / {second_number} = {divide}")
            print(div_sum)
            my_data.append(div_sum)

            if first_number/second_number == 0:
                None
        except ZeroDivisionError:
                print("ERROR ====> Sorry, you cant divide your number by 0.\nPlease try again.")
                my_calculator()
    
    # Subtraction calculation:
    elif operation == "-":
        subtract = first_number - second_number
        subtract = round(subtract, 2)
        print("============================= Results:")
        sub_output=(f"Your result: {first_number} - {second_number} = {subtract}")
        print(sub_output)
        my_data.append(sub_output)

    # Adding calculation:
    elif operation == "+":
        sum = first_number + second_number
        sum = round(sum, 2)
        print("============================= Results:")
        sum_output=(f"Your result: {first_number} + {second_number} = {sum}")
        print(sum_output)
        my_data.append(sum_output)

    # Modulus calculation:
    elif operation == "%":
        try:
            modula = first_number % second_number
            print("============================= Results:")
            mod_ouput=(f"Your result: {first_number} % {second_number} = {modula} as the remainder")
            print(mod_ouput)
            my_data.append(mod_ouput)

            if second_number == 0:
                None
        except ZeroDivisionError:
            print("ERROR ====> Sorry, you cant divide your number by 0.\nPlease try again.")
            my_calculator()
    else:
        print("ERROR ====> Sorry, you did not enter a valid input.\nPlease try again.")
        my_calculator()
#==================================================== Writing to file:
# Data saved in list 'my_data' will be written to 'equation.txt'
# Each input of data will be saved on a new line.
    with open("equations.txt", "a") as my_file:
        for lines in my_data:
            my_file.writelines(lines + "\n")

 # This allows user to do another calculation or to exit program:         
    try_again = input("\nWould you like to try again? (y/n) or exit (e):\n> ").lower()
    if try_again == "y":
        my_calculator()
    elif try_again == "n":
        main_menu()
    elif try_again == "e":
        exit_menu()
    elif try_again != "y" or "n":
        print("\nERROR ====> Sorry you did not enter a valid input.\nPlease try again.")
        my_calculator()

# Run the program
main_menu() 
