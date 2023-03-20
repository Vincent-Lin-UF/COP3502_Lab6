# Written by Vincent Lin

def encode(): # Encodes the password
    while True: # Loop to get valid input
        userPass = input("Please enter your password to encode: ")
        if len(userPass) != 8 or not userPass.isdigit(): # Checks length and to see if it is integers
            raise ValueError("Error: Only 8 digits long and contains exclusively integers")
        else:
            break
    
    encPass = ""
    for val in userPass: # adds 3 and mod 10 for edge cases
        encPass += str((int(val)+3)%10)
    
    return encPass

def menu(): # Menu
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")

def main():
    
    while True:
        menu()
        
        userInput = int(input("Please enter an option: "))
        if userInput == 1: # Encodes the password
            encPass = encode()
            print("Your password has been encoded and stored!\n")
        elif userInput == 2: # Decodes the password
            print("decode goes here")
        elif userInput == 3: # Exits the program
            break
        else:
            print("Error: Input Valid Number")
        

if __name__ == '__main__':
    main()