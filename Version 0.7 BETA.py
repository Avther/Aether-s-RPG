import random
import time

def enemy(ename,attackType,title,estrength,ehealth,edefence,coinRange0,coinRange1,strength,health,defence,pot,coins,kill):
        emaxhealth = ehealth
        if title is not None:
            print(title)
        print("----A",ename,"appears!-----")
        print("\n--"+ename+"'s Stats--")
        print("Strength:", estrength, "\nHealth:", ehealth,"/",emaxhealth, "\nDefence:", edefence, )
        print("\n--", name, "the", adj, hero, cre, "'s Stats--")
        print("Strength:", strength, "\nHealth:", round(health, 1),"/",maxhealth, "\nDefence:",defence, "\nPotions:", pot, )
        while ehealth >= 0 and health >= 0:
            move = str.title(input("\ndo you want to ATK, HEAL or RUN?\n"))
            if move == ("Atk"):
                dmgdone = strength * (1 - edefence / 10)
                ehealth -= strength * (1 - (edefence / 10))
                print("You hit the",ename,"for", round(dmgdone, 1), "! Its health is now", round(ehealth, 1),"/",emaxhealth)
                if ehealth <= 0:
                    coinsget = int(random.randint(coinRange0,coinRange1))
                    coins += coinsget
                    kill += 1
                    print("You killed the",ename,"! You got", coinsget, "coins! You now have", coins, "coins!")
                    time.sleep(3)
                    return health,coins,pot,kill
                    break
                dmgtake = estrength * (1 - (defence / 10))
                health -= estrength * (1 - (defence / 10))
                print("The",ename,attackType,"for", round(dmgtake, 1),"! Your health is now", round(health,1),"/",maxhealth )
                if round(health, 1) <= 0:
                    print("The",ename,"killed you! Game over :)")
                    return health,coins,pot,kill
                    break
            elif move == ("Run"):
                esc = int(random.randint(1, 10))
                if esc >= 4:
                    print("You Escaped! you will be awarded no coins, but you made it out with your life!")
                    return health,coins,pot,kill
                    break
                else:
                    print("You couldn't manage to get away this time!")
                    dmgtake = estrength * (1 - (defence / 10))
                    health -= estrength * (1 - (defence / 10))
                    print("The",ename,attackType,"for", round(dmgtake,1), "! Your health is now",round(health, 1),"/",maxhealth  )
                    if round(health, 1) <= 0:
                        print("The",ename,"killed you! Game over :)")
                        return health,coins,pot,kill
                        break
            elif move == ("Heal"):
                if pot >= 1:
                    pot -= 1
                    if health != maxhealth:
                        if maxhealth - health >= 8:
                            health += 8
                            print("You heal for 8 health points, your health is now", round(health, 1),"/", maxhealth,". You have", pot, "health potions left")
                        elif maxhealth - health < 8:
                            health = maxhealth
                            print("You heal for 8 health points, your health is now", round(health, 1),"/", maxhealth, ". You have",pot,"health potions left")
                    else:
                        print("Oops! You are already on max health")

                else:
                    print("Oops! You have no potions left!")
                dmgtake = estrength * (1 - (defence / 10))
                health -= estrength * (1 - (defence / 10))
                print("The",ename,attackType,"for", round(dmgtake, 1),"! Your health is now",round(health, 1),"/",maxhealth  )
                if round(health, 1) <= 0:
                    print("The",ename,"killed you! Game over :)")
                    return health,coins,pot,kill
                    break


#INTRO----------
print("Game created by Aether")
time.sleep(.999)
print("Welcome to")
time.sleep(.999)
print("....###....########.########.##.....##.########.########..####..######.....########..########...######..")
print("...##.##...##..........##....##.....##.##.......##.....##.####.##....##....##.....##.##.....##.##....##.")
print("..##...##..##..........##....##.....##.##.......##.....##..##..##..........##.....##.##.....##.##.......")
print(".##.....##.######......##....#########.######...########..##....######.....########..########..##...####")
print(".#########.##..........##....##.....##.##.......##...##..............##....##...##...##........##....##.")
print(".##.....##.##..........##....##.....##.##.......##....##.......##....##....##....##..##........##....##.")
print(".##.....##.########....##....##.....##.########.##.....##.......######.....##.....##.##.........######..")
print("Version 0.5 BETA")
time.sleep(.999)
ckill = 0
curse = 0
kill = 0
name = str.title(input("Please enter your name:\n"))
print("Ok,",name,)
adj = str.title(input("Please enter a title or adjective\n"))
hero = str.title(input("What class would you like to be:\n\
--Warrior-- \nStrength: 7\nHealth: 18 / 24\nDefence: 4\nHealth Potions: 3\n\n\
--Battlemage-- \nStrength: 10\nHealth: 14 / 20\nDefence: 3\nHealth Potions: 5\n"))
while hero != "Battlemage" and hero != "Warrior":
    hero = str.title(input("That is not a class type. Please choose one of the listed classes\n"))
if hero == ("Warrior"):
    strength = 7
    health = 18
    defence = 4
    coins = 5
    pot = 3
elif hero == ("Battlemage"):
    strength = 10
    health = 13
    defence = 3
    coins = 5
    pot = 5
maxhealth = health + 6
cre = input("Great. And finally, tell me what species you identify as\n")
print("I announce you,", name ,"the", adj , hero , cre ,"")
print("Ok,",name,)
decision = str.title(input("Are you ready to fight?\n"))
#INTRO----------


# enemy(ename,attackType,title,estrength,ehealth,edefence,coinRange0,coinRange1,strength,health,defence,pot,coins)

if decision != ("No"):
    while health > 0 and ckill != 3:
        num = int(random.randint(1, 10))
        #TESTING VARIABLE- CHANGE THIS TO FORCE AN ENEMY OR EVENT OUTCOME
        #num = 1
        #TESTING VARIABLE- CHANGE THIS TO FORCE AN ENEMY OR EVENT OUTCOME
        if num >= 10:  #range of 10-10 1/10 chance
            health,coins,pot,kill = enemy(" (∩｀-´)⊃━☆ﾟ.*･｡ﾟ Manic Cultist","hurls a spectral fireball at you","-MINIBOSS-",10,26,4,15,30,strength,health,defence,pot,coins,kill)
        elif num >= 7: #range of 7-9, 3/10 chance
            health,coins,pot,kill = enemy("[¬º-°]¬ Risen Corpse","swings a rotten limb at you",None,6,12,1,6,10,strength,health,defence,pot,coins,kill)
        elif num >= 4: #range of 4-6, 3/10 chance
            health,coins,pot,kill = enemy("٩(̾●̮̮̃̾•̃̾)۶ Charred Skeleton","rattles his bones at you",None,7,16,2,8,12,strength,health,defence,pot,coins,kill)
        elif num >=2:  #range of 2-3 2/10 chance
            chestChoice = str.title(input("You stumble upon a small, wooden chest. Do you OPEN it, or LEAVE?"))
            while chestChoice != "Open" and chestChoice != "Leave":
                chestChoice = str.title(input("Invalid choice.  Do you OPEN it, or LEAVE?"))
            if chestChoice == "Open":
                if int(random.randint(1,5)) >= 3:
                    prize = int(random.randint(10,45))
                    coins += prize
                    print("You open the chest to find...",prize,"coins!!")
                    time.sleep(2)
                else:
                    print("As you reach forward to open the chest... a pair of massive, gleaming teeth begin biting at you; it's a Mimic!!")
                    time.sleep(2)
                    health,coins,pot,kill = enemy("Chest Mimic","throws a pile of coins at you","----------",6,15,2,20,45,strength,health,defence,pot,coins,kill)
            else:
                print("You walk away, never truly knowing the contents of that box...")
                time.sleep(2)
        elif num >= 0: #range of 0-1, 2/10 chance
            print("$-----------$")
            print("$-Item Shop-$")
            print("$-----------$")
            print("Items:\n1. -Burning Blade-\n'The perfect tool for a warrior'\nPrice:30\n\n2. -Lightning Staff-\n'The perfect tool for a battlemage'\nPrice:30\n\n3. -Polished Steel armour-\n'Tough and strong'\nPrice:28\n\n4. -3 Health Potions-\n'Hits the spot in a pinch'\nPrice:16\n\n5. -Cursing Powder-\n'Who knows what this will do to your enemies?'\nPrice:120")
            print("You have",coins,"coins")
            print("Welcome,", name ,"the", adj , hero , cre ,"! This is my store.")
            purchase = str.title(input("Please enter the number for what item you would like to purchase, or type LEAVE if you wish to re-enter the battle!\n"))
            while purchase != "1" and purchase != "2" and purchase != "3" and purchase != "4" and purchase != "5" and  purchase != "Leave":
                purchase = str.title(input("Please enter a different item, or type LEAVE if you wish to re-enter the battle!\n"))
            buyfail = 1
            while buyfail == 1:
                if purchase == "1":
                    if coins >= 30:
                        if hero == "warrior":
                            coins = (coins - 30)
                            strength = (strength + 4)
                            print("Nice! You purchased the Burning Blade, good choice.")
                            buyfail = 0
                        elif hero == "battlemage":
                            coins = (coins - 20)
                            strength = (strength + 1)
                            print("Ummm... You purchased the Burning Blade, not really sure why but whatever floats your boat...")
                            buyfail = 0
                    else:
                        buyfail = 1
                        purchase = input("You Don't Have enough money for that. Please Select a different item or type LEAVE\n")
                elif purchase == "2":
                    if coins >= 30:
                        if hero == "battlemage":
                            coins = (coins - 30)
                            strength = (strength + 4)
                            print("Nice! You purchased the Lightning Staff, good choice.")
                            buyfail = 0
                        elif hero == "warrior":
                            coins = (coins - 20)
                            strength = (strength + 1)
                            print("Ummm... You purchased the Lightning Staff, not really sure why but whatever floats your boat...")
                            buyfail = 0
                    else:
                        buyfail = 1
                        purchase = input("You Don't Have enough money for that. Please Select a different item or type LEAVE\n")
                elif purchase == "3":
                    if coins >= 28:
                        coins = (coins - 28)
                        defence = (defence + 2)
                        print("Nice! You got the Polished Steel Chestplate! That should help when you're taking a beating.")
                        buyfail = 0
                    else:
                        buyfail = 1
                        purchase = input("You Don't Have enough money for that. Please Select a different item or type LEAVE\n")
                elif purchase == "4":
                    if coins >= 16:
                        coins = (coins - 16)
                        pot = (pot + 3)
                        print("you purchased 3 Health Potions. Great drink when you're feeling hurt.")
                        buyfail = 0
                    else:
                        buyfail = 1
                        purchase = input("You Don't Have enough money for that. Please Select a different item or type LEAVE\n")
                elif purchase == "leave":
                    break
                elif purchase == "5":
                    if coins >= 120:
                        coins = (coins - 120)
                        curse = (curse + 1)
                        print("You purchased the Cursing Powder. Do you know what you're getting yourself into?")
                        buyfail = 0
                    else:
                        buyfail = 1
                        purchase = input("You Don't Have enough money for that. Please Select a different item or type LEAVE\n")
                elif purchase == "Leave":
                    break
    if ckill >= 3:
        print("You have beaten the game! You killed:", kill, "monsters and you had", coins, "coins!")
        input()
    else:
        print("____    ____  ______    __    __      _______   __   _______  _______   __ ")
        print("\   \  /   / /  __  \  |  |  |  |    |       \ |  | |   ____||       \ |  |")
        print(" \   \/   / |  |  |  | |  |  |  |    |  .--.  ||  | |  |__   |  .--.  ||  |")
        print("  \_    _/  |  |  |  | |  |  |  |    |  |  |  ||  | |   __|  |  |  |  ||  |")
        print("    |  |    |  `--'  | |  `--'  |    |  '--'  ||  | |  |____ |  '--'  ||__|")
        print("    |__|     \______/   \______/     |_______/ |__| |_______||_______/ (__)")
        time.sleep(.999)
        print("You killed:", kill, "creatures and you had", coins, "coins.")
        input()
else:
    print("Thank you for playing Aether's RPG")
    input()
