from colors import GREEN,RED,WHITE,YELLOW
def welcome_screen():
    print(YELLOW,'*** WELCOME TO GAME GUESSER ***' )
    user_input = int(input(WHITE+'1. Start Game \n2. About Game Guesser \n3. Exit Application \n\n Choose any valid option: ' ))
    determine_user_option(user_input)

def determine_user_option(user_option):
    if user_option ==1:
        pass
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
    input(WHITE,'1. Beginner (1-10) \n 2. Intermediat(1-100 \n 3. Hard(1-1500)\n 4. Back to menu')



welcome_screen()
