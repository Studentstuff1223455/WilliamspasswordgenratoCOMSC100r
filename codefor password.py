import random
import string

def password_lover(min_numbers, reckoning=True, you_special=True):
    lett = string.ascii_letters
    num = string.digits
    spec = string.punctuation

    person = lett
    if reckoning:
        person += num
    if you_special:
        person += spec

    pwd = ""
    meets_dof = False
    number = False
    has_spec = False

    while not meets_dof or len(pwd) < min_numbers:
        new = random.choice(person)
        pwd += new

        if new in num:
            number = True
        if new in spec:
            has_spec = True

        meets_dof = True
        if reckoning:
            meets_dof = number
        if you_special:
            meets_dof = meets_dof and has_spec

    return pwd


print("Welcome to the Password Generator! Please leave very happy with your password! Ya!!!!!!!")


min_numbers = int(input("Put in how long you want your password (limit is a secret): "))
reckoning = input("Do you want numbers in it? (y/n): ") == 'y'
has_spec = input("Do you want special characters? (y/n): ") == 'y'


pwd = password_lover(min_numbers, reckoning, has_spec)


print("Your password:", pwd)

