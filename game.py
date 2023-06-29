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

# username = input('What is your name? ')
# print('Hello ' + username + ', Welcome to LandScaper!\n')
# print('*********************************************')
# print('You have decided to start a landscaping business in your city.\n')
# print('The only problem is that you dont have any money, so to get started\n')
# print('you must use the tools you were born with, your teeth...\n')
# print('Since this is very weird you have decided to give customers an attractive quote for $1 a lawn!\n')
# print('As you upgrade your tools, prices per lawn will increase due to higher efficiency.\n')
# print('Are You ready to get cutting!?\n')
# print('*********************************************')

gameInProgress = True
class User:
    cash = 0

user = User()
def cutGrassTeeth():
    print('You cut a customers lawn with your teeth and made $1!')
    user.cash = user.cash + 1
    print('Balance: $' + str(user.cash))

def menu():
    menuChoice = input('Main Menu: (c)ut grass, (u)pgrade tool, check (b)alance, (r)eset, e(x)it: ')
    if (menuChoice == 'c'):
        cutGrassTeeth()
    elif (menuChoice == 'b'):
        print(user.cash)
    else:
        print("command not found")

while (gameInProgress):
    menu()