from colors import GREEN,RED,WHITE,YELLOW
from random import randint
def welcome_screen():
    print(YELLOW,'*** WELCOME TO GAME GUESSER ***' )
    user_input = int(input(WHITE+'1. Start Game \n2. About Game Guesser \n3. Exit Application \n\nChoose any valid option: ' ))
    determine_user_option(user_input)

def determine_user_option(user_option):
    if user_option ==1:
        difficulty()
    elif user_option ==2:
            about_game()
    elif user_option ==3:
        exit_app()
    else:
        invalid_option()

def exit_app():
    print("Thanks for using our app😁")
    exit()

def about_game():
    print('This app was developed in 1990 to help entertain users.')
    welcome_screen()

def invalid_option():
    print(RED,'Invalid Option!!Please try again')
    welcome_screen()


def difficulty():
    print(YELLOW,'*** Choose Level ***')
    user_response=int(input(WHITE+' 1.Beginner (1-10)\n 2.Intermediate (1-100)\n 3.Hard (1-1500)\n\n 4.Back to menu\n Enter a valid number: '))
    validate_user_response(user_response)

def validate_user_response(user_response):
    if user_response ==1:
        start_game(10,2)
    elif user_response ==2:
        start_game(100,5)
    elif user_response ==3:
        start_game(500,6)
    elif user_response ==4:
        welcome_screen()
    else:
         invalid_option()

def generate_random_number(endpoint):
    return randint(1,endpoint)

def start_game(user_level,user_attempt):
    generated_number = generate_random_number(user_level)

    for trial in range(user_attempt):
        user_guess=int(input('\nYou have 2 guess in this difficulty...\nGuess a number: '))
        if user_guess == generated_number:
            print(GREEN ,'Hurray!! You guess right.👏🎊')
            break
        elif user_guess > generated_number:
            print(RED,'You guessed Too high.Try again😒')
        elif user_guess < generated_number:        
            print(RED,'Sorry guess too low.Try again.😒')





welcome_screen()
