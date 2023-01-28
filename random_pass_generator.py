import random

print("\n\nWelcome to the Password Generator\n\n")
print("Choose the type of password you want")
print("1. With All Character")
print("2. Letters and Numbers")
print("3. Letters")
print("4. Numbers")

try:
    choice = int(input("\nEnter your choice: "))
except:
    print("\nEnter a valid input")

input
pass_length = int(input("Enter Password length: "))

def random_pass_generator(length):
    password = ''
    for i in range(pass_length):
        password += chr(random.randint(33, 126))
    return password

def random_pass_generator_in_numbers(length):
    password=''
    for i in range(pass_length):
        password+=chr(random.randint(48,57))
    return password

def random_pass_generator_in_letters(length):
    password=''
    for i in range(pass_length):
        password+=chr(random.randint(65,122))
    return password

def random_pass_generator_in_letters_and_numbers(length):
    password=''
    for i in range(pass_length):
        password+=chr(random.randint(33,122))
    return password

if choice == 1:
    print("\nHere is Your Password: {0} ".format(random_pass_generator(pass_length)))
    while True:
        print("\n\nDo you wanna change it?")
        print("1. Yes")
        print("2. No")
        print("3. To change the length")
        print("4. To change the Mood of Password ")

        try:
            choice = int(input("\nEnter your choice: "))
        except:
            print("\nEnter a valid input")

        if choice == 1:
            print("\nHere is Your New Password: {0} ".format(random_pass_generator(pass_length)))
        elif choice == 2:
            break
        elif choice == 3:
            pass_length = int(input("\nEnter Password length: "))
            print("\nHere is Your New Password: {0} ".format(random_pass_generator(pass_length)))
        elif choice == 4:
            print("\nChoose the type of password you want")
            print("1. With All Character")
            print("2. Letters and Numbers")
            print("3. Letters")
            print("4. Numbers")
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                print("\nHere is Your Password: {0} ".format(random_pass_generator(pass_length)))
            elif choice == 2:
                print("\nHere is Your Password: {0} ".format(random_pass_generator_in_letters_and_numbers(pass_length)))
            elif choice == 3:
                print("\nHere is Your Password: {0} ".format(random_pass_generator_in_letters(pass_length)))
            elif choice == 4:
                print("\nHere is Your Password: {0} ".format(random_pass_generator_in_numbers(pass_length)))
            else:
                print("\nInvalid Input")

elif choice == 2:
    print("\nHere is Your Password: {0} ".format(random_pass_generator_in_letters_and_numbers(pass_length)))
    while True:
        print("\n\nDo you wanna change it?")
        print("1. Yes")
        print("2. No")
        print("3. To change the length")
        print("4. To change the Mood of Password ")
        
        try:
            choice = int(input("\nEnter your choice: "))
        except:
            print("\nEnter a valid input")

        if choice == 1:
            print("\nHere is Your New Password: {0} ".format(random_pass_generator_in_letters_and_numbers(pass_length)))
        elif choice == 2:
            break
        elif choice == 3:
            pass_length = int(input("\nEnter Password length: "))
            print("\nHere is Your New Password: {0} ".format(random_pass_generator_in_letters_and_numbers(pass_length)))
        elif choice == 4:
            print("\nChoose the type of password you want")
            print("1. With All Character")
            print("2. Letters and Numbers")
            print("3. Letters")
            print("4. Numbers")
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                print("\nHere is Your Password: {0} ".format(random_pass_generator(pass_length)))
            elif choice == 2:
                print("\nHere is Your Password: {0} ".format(random_pass_generator_in_letters_and_numbers(pass_length)))
            elif choice == 3:
                print("\nHere is Your Password: {0} ".format(random_pass_generator_in_letters(pass_length)))
            elif choice == 4:
                print("\nHere is Your Password: {0} ".format(random_pass_generator_in_numbers(pass_length)))
            else:
                print("\nInvalid Input")

elif choice == 3:
    print("\nHere is Your Password: {0} ".format(random_pass_generator_in_letters(pass_length)))
    while True:
        print("\nDo you wanna change it?")
        print("1. Yes")
        print("2. No")
        print("3. To change the length")
        print("4. To change the Mood of Password ")
        
        try:
            choice = int(input("\nEnter your choice: "))
        except:
            print("\nEnter a valid input")

        if choice == 1:
            print("\nHere is Your New Password: {0} ".format(random_pass_generator_in_letters(pass_length)))
        elif choice == 2:
            break
        elif choice == 3:
            pass_length = int(input("\nEnter Password length: "))
            print("\nHere is Your New Password: {0} ".format(random_pass_generator_in_letters(pass_length)))
        
        elif choice == 4:
            print("\nChoose the type of password you want")
            print("1. With All Character")
            print("2. Letters and Numbers")
            print("3. Letters")
            print("4. Numbers")
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                print("\nHere is Your Password: {0} ".format(random_pass_generator(pass_length)))
            elif choice == 2:
                print("\nHere is Your Password: {0} ".format(random_pass_generator_in_letters_and_numbers(pass_length)))
            elif choice == 3:
                print("\nHere is Your Password: {0} ".format(random_pass_generator_in_letters(pass_length)))
            elif choice == 4:
                print("\nHere is Your Password: {0} ".format(random_pass_generator_in_numbers(pass_length)))
            else:
                print("Invalid Input")

elif choice == 4:
    print("\nHere is Your Password: {0} ".format(random_pass_generator_in_numbers(pass_length)))
    while True:
        print("\n\nDo you wanna change it?")
        print("\n1. Yes")
        print("\n2. No")
        print("3. To change the length")
        print("4. To change the Mood of Password ")
        
        try:
            choice = int(input("Enter your choice: "))
        except:
            print("\nEnter a valid input")

        if choice == 1:
            print("\nHere is Your New Password: {0} ".format(random_pass_generator(pass_length)))
        elif choice == 2:
            break
        elif choice == 3:
            pass_length = int(input("\nEnter Password length: "))
            print("\nHere is Your New Password: {0} ".format(random_pass_generator(pass_length)))
        elif choice == 4:
            print("\nChoose the type of password you want")
            print("1. With All Character")
            print("2. Letters and Numbers")
            print("3. Letters")
            print("4. Numbers")
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                print("\nHere is Your Password: {0} ".format(random_pass_generator(pass_length)))
            elif choice == 2:
                print("\nHere is Your Password: {0} ".format(random_pass_generator_in_letters_and_numbers(pass_length)))
            elif choice == 3:
                print("\nHere is Your Password: {0} ".format(random_pass_generator_in_letters(pass_length)))
            elif choice == 4:
                print("\nHere is Your Password: {0} ".format(random_pass_generator_in_numbers(pass_length)))
            else:
                print("\nInvalid Input")

else:
    print("Invalid Input")


   