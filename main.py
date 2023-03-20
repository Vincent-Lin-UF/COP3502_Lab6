# Written by Vincent Lin

def encode():
    while True:
        userPass = input("Please enter your password to encode: ")
        if len(userPass) != 8 or not userPass.isdigit():
            raise ValueError("Error: Only 8 digits long and contains exclusively integers")
        else:
            break
    
    encPass = ""
    for val in userPass:
        encPass += str((int(val)+3)%10)
    
    return encPass

def menu():
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")

def main():
    
    while True:
        menu()
        
        userInput = int(input("Please enter an option: "))
        if userInput == 1:
            encPass = encode()
            print("Your password has been encoded and stored!\n")
        elif userInput == 2:
            print("decode goes here")
        elif userInput == 3:
            break
        else:
            print("Error: Input Valid Number")
        

if __name__ == '__main__':
    main()