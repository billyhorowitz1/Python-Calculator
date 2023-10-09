# Creator: William Horowitz
# Date: 10/09/2023
# Description: This program will prompt a user to enter a mathematical operation then ask for two numbers to perform
#              the operation on


# Main Function
def main():
    
    # Display the menu to the user
    setupMenu()

    # Find out what operation the user requested
    requestedOperation = getOperation()

    # Request and store numbers entered from user
    numbersEntered = getNumbers()

    # Perform the requested operation
    if requestedOperation == "Add":

        print(f"{numbersEntered[0]} + {numbersEntered[1]} is equal to {numbersEntered[0] + numbersEntered[1]}")
    
    elif requestedOperation == "Subtract":

        print(f"{numbersEntered[0]} - {numbersEntered[1]} is equal to {numbersEntered[0] - numbersEntered[1]}")

    elif requestedOperation == "Multiply":

        print(f"{numbersEntered[0]} * {numbersEntered[1]} is equal to {numbersEntered[0] * numbersEntered[1]}")
    
    elif requestedOperation == "Divide":

        print(f"{numbersEntered[0]} / {numbersEntered[1]} is equal to {numbersEntered[0] / numbersEntered[1]}")

    


# Function for setting up menu
def setupMenu():
    
     print("--------------\n  CALCULATOR\n--------------\n")
     print("1.) Add\n2.) Subtract\n3.) Multiply\n4.) Divide")
     
# Function for obtaining user input on what operation to perform
def getOperation():
    
    while True:
        
    try:
        userInput = int(input("Enter the number for the operation you would like to perform:"))

        if userInput == 1:
            return "Add"
        elif userInput == 2:
            return "Subtract"
        elif userInput == 3:
            return "Multiply"
        elif userInput == 4:
            return "Divide"
        else:
            print("Please enter a number between 1 and 4")

    except:

        print("Please enter a valid number\n")

# Function for obtaining the two numbers to perform the operation on

def getNumbers():
    while True:
        
        try:
            
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return [num1, num2]
            
        except ValueError:
            
            print("Please enter valid numbers.")
 
# Call main function
if __name__ == "__main__":
    
    main()