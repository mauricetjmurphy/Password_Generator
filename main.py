# Import module
import random

# Greeting message
print('Welcome to the passwrod generator!')

# Create lists
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+']
capLetters = []
password = []

def alfaCapLetters (l, nl):
    for e in l:
        nl.append(e.upper())
    return nl


# Create a function that shuffles a list and then converts it to a string
def shuffledListToString(s):
    random.shuffle(password)
    strLi = ''
    return (strLi.join(s))
    

# Ask user questions
ans1 = int(input('How many letters?\n'))

ans2 = int(input('How many numbers?\n'))

ans3 = int(input('How many symbols?\n'))

alfaCapLetters(letters, capLetters)

for char in range(0, int(ans1/2)):
    randCapLetter = random.choice(capLetters)
    password.append(randCapLetter)

for char in range(0, int(ans1/2)):
    randLetter = random.choice(letters)
    password.append(randLetter)

for num in range(0, ans2):
    randNum = random.choice(numbers)
    password.append(randNum)

for sym in range(0, ans2):
    randSym = random.choice(symbols)
    password.append(randSym)


newPassword = shuffledListToString(password)

print(f'Your new password is {newPassword}')

