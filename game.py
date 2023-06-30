# Game Descirption: 
# You are starting a landscaping business, but all you have are your teeth.
# Using just your teeth, you can spend the day cutting lawns and make $1. You can do this as much as you want.

# -At any point, if you are currently using your teeth, you can buy a pair of rusty scissors for $5. You can do this once, assuming you have enough money.

# -Using the rusty scissors, you can spend the day cutting lawns and make $5. You can do this as much as you want.

# -At any point, if you are currently using rusty scissors, you can buy an old-timey push lawnmower for $25. You can do this once, assuming you have enough money.

# -Using the old-timey push lawnmower, you can spend the day cutting lawns and make $50. You can do this as much as you want

# -At any point, if you are currently using the old-timey push lawnmower, you can buy a fancy battery-powered lawnmower for $250. You can do this once, assuming you have enough money.

# -Using the the fancy battery-powered lawnmower, you can spend the day cutting lawns and make $100. You can do this as much as you want.

# -At any point, if you are currently using the fancy battery-powered lawnmower, you can hire a team of starving students for $500. You can do this once, assuming you have enough money.

# -Using the the team of starving students, you can spend the day cutting lawns and make $250. You can do this as much as you want.

# -You win the game when you have a team of starving students and $1000. In this situation, send a message to the user telling them, they’ve won.

# Game Flow:
# if users bank balance is below $5 -> run cutGrassTeeth
# if the users bank is above $5 then ask if they want to upgrade to scissors 
#   if yes -> run cutGrassScissors()
#   if no -> keep running cutGrassTeeth()
# if users bank is above $25 then ask if they want to upgrade to an old-timey push mower
#   if yes -> run cutGrassPushMower()
#   if no -> run current cutGrass function
# and continue for each upgrade once cash has hit certain balance.

username = input('What is your name? ')
print('Hello ' + username + ', Welcome to LandScaper!\n')
print('*********************************************')
print('You have decided to start a landscaping business in your city.\n')
print('The only problem is that you dont have any money, so to get started\n')
print('you must use the tools you were born with, your teeth...\n')
print('Since this is very weird you have decided to give customers an attractive quote for $1 a lawn!\n')
print('As you upgrade your tools, prices per lawn will increase due to higher efficiency.\n')
print('Are You ready to get cutting!?\n')
print('*********************************************')


class User:
    cash = 0
    toolProfit = 1
    hasTeeth = True
    hasScissors = False
    hasPushMower = False
    hasPowerMower = False
    hasStudents = False
    hasRobots = False
    gameInProgress = True
    
    # currentTool = cutGrassTeeth()

user = User()

def toolList():
    print('Tool Upgrade List:\n')
    print('1. Scissors - $10\n')
    print('2. Push Mower - $100\n')
    print('3. Power Mower - $250\n')
    print('4. Team of Students - $500\n')
    print('5. Robots - $3000\n')
    print('****************************')
    print('Current balance: $' + str(user.cash))
    print('****************************')
# def cutGrass():
#     user.currentTool

def reset():
    gameReset = input('Are you sure you want to reset the game? (y/n): ')
    if (gameReset == 'y'):
        user.cash = 0,
        user.hasTeeth = True
        user.hasScissors = False
        user.hasPushMower = False
        user.hasPowerMower = False
        user.hasStudents = False
        user.hasRobots = False
        user.toolProfit = 1
        print('\nGame Reset.\n')
    elif (gameReset == 'n'):
      print('\nReset cancelled.\n')


def cutGrass():
    print('You cut a customers lawn with your teeth and made $' + str(user.toolProfit))
    user.cash = user.cash + user.toolProfit
    # print('Balance: $' + str(user.cash))

def upgradeTool():
    toolList()
    #scissors upgrade
    if (user.cash > 10 and user.hasTeeth):
        user_response = input('Do you want to upgrade to scissors? (y/n): ')
        if (user_response.casefold() == 'y'):
            user.cash -= 10
            user.hasTeeth = False

            user.hasScissors = True
            user.toolProfit = 5 
        else:
            print('User does not want to upgrade')
    #push mower upgrade
    if (user.cash > 100 and user.hasScissors):
        user_response = input('Do you want to upgrade to Push mower? (y/n): ')
        if (user_response.casefold() == 'y'):
            user.cash -= 100
            user.hasTeeth = False
            user.hasScissors = False

            user.hasPushMower = True
            user.toolProfit = 25
        else:
            print('User does not want to upgrade')
    #power mower upgrade
    if (user.cash > 250 and user.hasPushMower):
        user_response = input('Do you want to upgrade to power mower? (y/n): ')
        if (user_response.casefold() == 'y'):
            user.cash -= 250
            user.hasTeeth = False
            user.hasScissors = False
            user.hasPushMower = False

            user.hasPowerMower = True
            user.toolProfit = 50 
        else:
            print('User does not want to upgrade')
    #student upgrade
    if (user.cash > 500 and user.hasPowerMower):
        user_response = input('Do you want to hire some students? (y/n): ')
        if (user_response.casefold() == 'y'):
            user.cash -= 500
            user.hasTeeth = False
            user.hasScissors = False
            user.hasPushMower = False
            user.hasPowerMower = False
            user.hasScissors = False

            user.hasStudents = True
            user.toolProfit = 100 
        else:
            print('User does not want to upgrade')
    #robot upgrade
    if (user.cash > 3000 and user.hasStudents):
        user_response = input('Do you want to upgrade to Robots? (y/n): ')
        if (user_response.casefold() == 'y'):
            user.cash -= 3000
            user.hasTeeth = False
            user.hasScissors = False
            user.hasPushMower = False
            user.hasPowerMower = False
            user.hasStudents = False

            user.hasRobots = True
            user.toolProfit = 500 
        else:
            print('User does not want to upgrade')

def menu():
    menuChoice = input('Main Menu: (c)ut grass, (u)pgrade tool, check (b)alance, (r)eset, e(x)it: ')
    if (menuChoice == 'c'):
        cutGrass()
    elif (menuChoice == 'b'):
        print(user.cash)
    elif (menuChoice == 'u'):
        upgradeTool()
    elif (menuChoice == 'r'):
        reset()
    elif (menuChoice == 'x'):
        user.gameInProgress = False
    else:
        print("command not found")

while (user.gameInProgress):
    menu()
    if (user.cash > 5000):
        print("User Wins")
        break

