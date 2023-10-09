# Creator: William Horowitz
# Date: 10/09/2023
# Description: This program will prompt a user to enter a mathematical operation then ask for two numbers to perform
#              the operation on


# Main Function
def main():
    
   setupMenu()
    


# Function for setting up menu
def setupMenu():
    
     print("--------------\n  CALCULATOR\n--------------\n")
     print("1.) Add\n2.) Subtract\n3.) Multiply\n4.) Divide")
     
# Function for obtaining user input
def getInput():
    
    userInput = input("Enter the number for the operation you would like to perform")

# Call main function
if __name__ == "__main__":
    
    main()