#!/usr/bin/python3
import random

def bulls_vs_eyes(user_guess,computer_generated_guess):
    bulls = 0
    eyes = 0
    for i in range(len(computer_generated_guess)):
        if user_guess[i] == computer_generated_guess[i]:
            bulls += 1
        elif user_guess[i] in computer_generated_guess:
            eyes += 1
    
    return bulls,eyes

comp_guess = ''.join(str(random.randrange(0,10)) for i in range(4))

#print(comp_guess)
while(True):
    users_guess = input('Enter four digit guess: ')
    bulls,eyes = bulls_vs_eyes(users_guess,comp_guess)
    if bulls == 4:
        print ('you have won!\nthe correct answer is indeed %s'%comp_guess)
        break
    else:
        print ('bulls: %d, eyes: %d '%(bulls,eyes))
