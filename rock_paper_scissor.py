import random, time


print("Game Play Starts......")
time.sleep(1)
    
print("1. Rock \t  2. Paper\t 3. Scissor")
map = {
    1: 'Rock',
    2: 'Paper',
    3: 'Scissor'
}

player = {
    'user':"You",
    'computer':"Computer"
}

user= int(input("Enter Your Choice: "))  # user input
if user not in [1,2,3]:
    print("--Enter valid Option--")
else:
    
    print("Your Choice: ", map[user])
    print("Thinking........")
    time.sleep(1)
    computer = random.randint(1,3) # computer input
    print("computer: ", map[computer])

    if user == computer:
        win = ''
        print("DRAW!!!!!!")

    elif user ==1 and computer ==2:
        win = 'computer'

    elif user ==2 and computer ==1:
        win = 'user'

    elif user ==1 and computer ==3:
        win = 'user'

    elif user ==3 and computer ==1:
        win = 'computer'

    elif user ==2 and computer ==3:
        win = 'computer'

    elif user ==3 and computer ==2:
        win = 'user'

    else:
        print("Some Error Occured:(")
    if win!='':
        time.sleep(0.5)
        print("< ",player[win], "won >")