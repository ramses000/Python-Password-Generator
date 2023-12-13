import random
import string

def generate_password(min_length,upperCase=True, numbers=True, special_characters=True):
    upLetters = string.ascii_uppercase
    lowLetters = string.ascii_lowercase
    digits = string.digits
    special = string.punctuation
    characters = lowLetters
    if upperCase:
       characters+=upLetters
    if numbers:
        characters+=digits
    if special_characters:
        characters+=special
    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False
    has_uppercase = False
    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd+=new_char
        if new_char in upLetters:
            has_uppercase = True
        elif new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True
        meets_criteria = True
        if upperCase:
           meets_criteria = has_uppercase
        if numbers:
            meets_criteria = meets_criteria and has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special
    return pwd 
min_length = 0
max_length = 0
while True:
  try:
    min_length = int(input("Enter the minimum length: "))       
  except ValueError:
     print("Not an integer!")
     continue
  else:
    has_uppercase = input("Do you want to have uppercase (y/n)").lower()=="y"
    has_number = input("Do you want to have numbers (y/n)").lower()=="y"
    has_special = input("Do you want to have special characters (y/n)").lower()=="y"  
    pwd = generate_password(min_length,has_uppercase, has_number,has_special) 
    print("The generated password is: ", pwd) 
    break 

