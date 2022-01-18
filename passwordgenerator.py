import random # Importing random for generating semi-random characters


# Needed to create this as a function so I could easily 
# call back to it so characters would regenerate

def generate_random_letters(): 
    low_letter1 = chr(random.randint(97, 122))
    special_char1 = chr(random.randint(33, 38))
    up_letter1 = chr(random.randint(65, 90))
    num1 = chr(random.randint(48, 57))

    all_chars = [low_letter1, special_char1, up_letter1, num1]
    return all_chars # Returns all possible characters to be used in the generation process

def random_password():
    password = []
    length = input("How long would you like your password to be?: ")
    for x in range(int(length)): 
        password.append(random.choice(generate_random_letters()))
        
    return ("".join(password))
print(random_password())
