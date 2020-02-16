# Generate a random password with or without symbols between 6-20 characters

import random
import string

add_symbols = bool
pass_length = int

def yes_or_no(question):
    while 'invalid response':
        user_input = str(input('Would you like symbols in your passwords?: (y/n): ')).lower().strip()
        if user_input == 'y':
            return True
        if user_input == 'n':
            return False
        else:
            print('Invalid response... Please enter (y/n)\n')
            return yes_or_no(question)


add_symbols = yes_or_no(add_symbols)


def password_length(length):
    password_question = input('How long do you want your password? (6-20) ')
    while 5 < int(password_question) < 21:
        return password_question
    else:
        print('Invalid response... Please enter a number between 6 and 20) ')
        return password_length(length)


pass_length = password_length(pass_length)


def random_string(string_length=int):
    """Generate a random string of letters, digits and special characters """
    if add_symbols:
        password_characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(password_characters) for i in range(string_length))
    else:
        password_characters = string.ascii_letters + string.digits
        return ''.join(random.choice(password_characters) for i in range(string_length))


print("\nGenerating Random String password with letters, digits and special characters ")
print("First Random String ", random_string(int(pass_length)))
print("Second Random String", random_string(int(pass_length)))
print("Third Random String", random_string(int(pass_length)))

# For command prompt terminal
input('Press ENTER to exit')