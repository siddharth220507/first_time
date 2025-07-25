import random
print("Welcome to Number Battle \n Here you have to guess a number in limited trials according to your chosen difficulty level")
difficulty=input("Choose your difficulty level here: \n1.Easy\n2.Medium\n3.Hard\nInput here:").lower()
attempts=0
if difficulty=="easy":
    print("You have 8 attempts to guess the right number.")
    attempts+=8
elif difficulty=="medium":
    print("You have 6 attempts to guess the right number.")
    attempts+=6
elif difficulty=="hard":
    print("You have 4 attempts to guess the right number.")
    attempts+=4        
else:
    print("Choose from the listed options..")

score=100
print('''__        _______ _     ____ ___  __  __ _____       _   _ ____  _____ ____  
\ \      / / ____| |   / ___/ _ \|  \/  | ____|     | | | / ___|| ____|  _ \ 
 \ \ /\ / /|  _| | |  | |  | | | | |\/| |  _|       | | | \___ \|  _| | |_) |
  \ V  V / | |___| |__| |__| |_| | |  | | |___   _  | |_| |___) | |___|  _ < 
   \_/\_/  |_____|_____\____\___/|_|  |_|_____| ( )  \___/|____/|_____|_| \_|
                                                |/                           


      ''')

print(''' ____        __  _____
|    \|  |  | |     /  _/ ___/
|  D  |  |  | |    /  [(   \_ 
|    /|  |  | |___|    _\__  |
|    \|  :  |     |   [_/  \ |
|  .  |     |     |     \    |
|__|\_|\__,_|_____|_____|\___|
\n      1.Your default score is 100. If you guessed  wrong then your score will be deducted depending on difficulty level
\n      2.If score becomes 0 then you lose.
\n      3.If you guessed correctly in minimum attempts then you will get bonus score.\n
         ENJOY THE GAME
''')

numbers=""
if difficulty=="easy":
    numbers==random.randint(1,10)
elif difficulty=="medium":
    numbers==random.randint(1,50)
elif difficulty=="hard":
    numbers==random.randint(1,100)       
else:
    print("Choose from the listed options..")
   

guess=int(input("Guess the number:"))




while guess!= numbers:
    
    attempts-=1

    if attempts==0:
        print("You lost all your chances :(")
        break
    elif difficulty=="easy" and attempts>5:
        print("You gets a bonus score of 50")
        score+=50
    elif difficulty=="medium" and attempts>4:
        print("You gets a bonus score of 50")
        score+=50
    elif difficulty=="hard" and attempts>3:
        print("You gets a bonus score of 50")
        score+=50