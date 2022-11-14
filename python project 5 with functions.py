# Adam Edwards-Uribe
# section 85214-66
# 11/11/22
# Project 5

#This program will take a user's celcius input and covert it to farenheit.

#function for greeting
def greeting():
    print('This program will convert degrees Celsius to degrees Fahrenheit.')
    print('Please enter the temperature in degrees Celsius; you may use decimals.')
    print()
#function for asking the user if they want to run program again
def runAgain():
    again = input('Would you like to run the program again?(y/n): ').lower()
    print()

    while again != 'y' and again != 'n':
         again = input('INPUT ERROR: Please type a y or n: ').lower()
         print()

    if again =='y':
        run = True
    else:
        run = False

    return run

#--------------------Main-----------------------------

#init runProgram
runProgram = True

#start program loop
while runProgram == True:

#call user greeting
    greeting()

#User input for temperature
    celsius=float(input('Enter a temperature in degrees Celsius: '))
    print()


#Input is converted from celsius to fahrenheit using a formula
    fahrenheit= (celsius * 1.8) + 32

#The fahrenheit degree is printed
    print(celsius, 'degrees Celsius is equal to', format(fahrenheit, ',.1f'), 'degrees Fahrenheit.')
    print()

# call the runAgain function
    runProgram = runAgain()

#Exit message
print('Have a good day!')
