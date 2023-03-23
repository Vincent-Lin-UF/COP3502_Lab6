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

def decode(encoded_password):
    # Convert the encoded password to a list of integers
    encoded_digits = [int(d) for d in encoded_password]
    
    # Shift each digit down by 3 numbers
    password_digits = [(d - 3) % 10 for d in encoded_digits]
    
    # Convert the password digits back to a string
    password = ''.join(str(d) for d in password_digits)
    
    return password

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
            print(f"The encoded password is {encPass}, and the original password is {decode(encPass)}.\n")
        elif userInput == 3: # Exits the program
            False
            exit()
        else:
            print("Error: Input Valid Number")
        

if __name__ == '__main__':
    main()