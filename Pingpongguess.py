from random import shuffle
my_list =  ['','O','']
def shuffle_list():
    shuffle(my_list)
    return (my_list)

def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input("Pick a number from 0,1 or 2")
    return int(guess)
     
def check_guess(my_list, guess):
    if my_list[guess] == 'O':
        print("Correct")
    else:
        print("Wrong")
        print(my_list)


my_list
shuffle_list()
guess = player_guess()
check_guess(my_list, guess)
