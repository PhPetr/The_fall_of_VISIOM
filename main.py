import random
import time
from pprint import pprint
import math
import sys
import pickle
import os.path

developer = False#TODO: remember to set it false before release

def text_animation(text):
    global time_speech
    global time_medium
    text = "\n  " + text
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(time_speech)
    time.sleep(time_medium)

def printWdelay(text):
    global time_medium
    text = "\n\n" + text + "\n"
    print(text)
    time.sleep(time_medium)

######## Character #########
class hero:
    def __init__(self, Hname, Hhealth, Hattack, Hranged, Hmagic, Hluck, Hdefence, Hskills):
        self.name = Hname
        self.health = Hhealth
        self.attack = Hattack
        self.ranged = Hranged
        self.magic = Hmagic
        self.luck = Hluck
        self.defence = Hdefence
        self.skills = Hskills

    def getHealth(self):
        return self.health
    def getAttack(self):
        return self.attack
    def getLuck(self):
        return self.luck
    def getRanged(self):
        return self.ranged
    def getDefence(self):
        return self.defence
    def getMagic(self):
        return self.magic
    def getName(self):
        return self.name
    def getSkills(self):
        return self.skills

    def setHealth(self, newHealth):
        self.health = newHealth
    def setAttack(self, newAttack):
        self.attack = newAttack
    def setLuck(self, newLuck):
        self.luck = newLuck
    def setRanged(self, newRanged):
        self.ranged = newRanged
    def setDefence(self, newDefence):
        self.defence = newDefence
    def setMagic(self, newMagic):
        self.magic = newMagic
    def setName(self, newName):
        self.name = newName
    def setSkills(self, newSkills):
        self.skills = newSkills

# class creation

def crateClass():
    print()
    text_animation("‘Oh hello, The chosen one. You want powers, but first I The magic scroll\nwant to ask a few questions to know you and know which power I’ll give you...’\n")
    print()
    role = input(" Are you more strategic (1) or more of a warrior (2)?...")
    print()
    while role != "1" and role != "2":
        text_animation("Invalid selection\n")
        role = input(" Are you more strategic (1) or more of a warrior (2)?...")

    if role == "1":
        heroAttack = 5
        heroDefence = random.randint(5,10)

    else:
        heroAttack = 10
        heroDefence = 5


    offense = input(" Are you more of bow and arrow user (1) or a magic user(2)?...")
    print()
    while offense != "1" and offense != "2":
        text_animation("Invalid selection\n")
        offense = input("\n Are you more of bow and arrow user (1) or a magic user(2)?...")
        print()

    if offense == "1":
        heroMagic = 5
        heroRanged = 10

    else:
        heroRanged = 5
        heroMagic = 10

    text_animation("'Now let\'s roll the dice for your luck'\n")
    fortune = input("Press enter to roll a dice...")
    print()
    time.sleep(0.2)
    text_animation("rolling dice...")
    print()
    time.sleep(0.2)
    heroLuck = random.randint(2,10)
    text_animation("'Your hero has " + str(heroLuck) + " luck out of 10.'")
    print()

    text_animation("New skill: Jack of all trades")
    text_animation("'With this skill you can use martial arts, swords, bows and magic staff.'")
    text_animation("\nNew skill: Upgrader")
    text_animation("'Every obtained loot will add points for specific statistics based on its quality'")
    heroSkills = "Jack of all trades, Upgrader"

    text_animation("'And lastly...'\n")
    heroName = input("\n What is your name hero?...")
    print()
    text_animation("'Nice to meet you " + heroName + ".'")
    print()
    text_animation("'I The magic scroll shall be your narrator and help you narrow down your decisions.'\n")
    return(heroName, heroAttack, heroRanged, heroMagic, heroLuck, heroDefence, heroSkills)

##### healing for the character #####
def recovery(character, maxHP):
    currentHealth = character.getHealth()
    if currentHealth < maxHP:
        character.setHealth(maxHP)
        stats = hero(character.getName(), character.getHealth(), character.getAttack(), character.getRanged(), character.getMagic(), character.getLuck(), character.getDefence(), character.getSkills())
        text_animation('"Oh no. Y-You are i-in-injured. I\'ll h-heal y-you, so d-don\'t wo-worry,"Vega said.')
        text_animation("You have healed. Your current stats:\n")
        pprint(vars(stats), sort_dicts=False)
        time.sleep(3)

def current_stats():
    global character
    text_animation("")
    text_animation("Your current stats:\n")
    pprint(vars(character), sort_dicts=False)
    text_animation("")
    time.sleep(4)

##### Enemy #####
class enemy:
    def __init__(self, Ename, Ehealth, Eattack, Especial, Echance):
        self.name = Ename
        self.health = Ehealth
        self.attack = Eattack
        self.special = Especial
        self.chance = Echance

    def getHealth(self):
        return self.health
    def getAttack(self):
        return self.attack
    def getSpecial(self):
        return self.special
    def getChance(self):
        return self.chance
    def getName(self):
        return self.name


    def setHealth(self, newHealth):
        self.health = newHealth
    def setAttack(self, newAttack):
        self.attack = newAttack
    def setSpecial(self, newSpecial):
        self.special = newSpecial
    def setChance(self, newChance):
        self.special = newChance
    def setName(self, newName):
        self.name = newName

##### enemy generator #####
def enemyGen(levelBoss, finalBoss, difficulty):
    temp = []
    file = open("adjective.txt", "r")
    lines = file.readlines()
    adjective = lines[random.randint(0, len(lines) - 1)][:-1]
    file.close
    file = open("animal.txt", "r")
    lines = file.readlines()
    animal = lines[random.randint(0, len(lines) - 1)][:-1]
    file.close
    if difficulty > 4:
        multiplier = 2
    else:
        multiplier = 1

    if finalBoss == True:
        health = random.randint(250, 600)
        attack = random.randint(40, 100)
        special = random.randint(100, 200)
        chance = random.randint(1, 8)

        return enemy(adjective + " " + animal, health, attack, special, chance)

    else:
        if levelBoss == False:
            health = random.randint(50*multiplier, 100*multiplier)
            attack = random.randint(10*multiplier,20*multiplier)
            special = random.randint(15*multiplier, 35*multiplier)
            chance = random.randint(1, 10)

            return enemy(adjective + " " + animal, health, attack, special, chance)

        else:
            health = random.randint(200, 250)
            attack = random.randint(30, 60)
            special = random.randint(50, 110)
            chance = random.randint(1, 8)

        return enemy(adjective + " " + animal, health, attack, special, chance)

############ Battle part of the game ##############
def enemyAttack(hitChance, attackValue, name, defence, specialValue):

    specialAtk = random.randint(1,10)
    if specialAtk > 8:
        specialLoss = specialValue - defence

        if specialLoss <= 0:
            print()
            text_animation(name + "is winding up for a SPECIAL attack...")
            text_animation("The special attack hits hero, but it dealt 0 damage.")
            return 0
        else:
            print()
            text_animation(name + "is winding up for a SPECIAL attack...")
            hit = random.randint(0, 10)
            if hitChance >= hit:
                text_animation("The special attack hits the hero!!!")
                text_animation("You stagger losing..." + str(specialLoss) + " health.")
                return math.ceil(specialLoss)
            else:
                text_animation("The enemy misses")
                return 0
    else:

        loss = attackValue - defence

        if loss <= 0:
            print()
            text_animation(name + "is winding up for an attack...")
            text_animation("The attack hits hero, but it dealt 0 damage.")
            return 0
        else:
            print()
            text_animation(name + "is winding up for an attack...")
            hit = random.randint(0, 10)
            if hitChance >= hit:
                text_animation("The attack hits the hero!!!")
                text_animation("You stagger losing..." + str(loss) + " health.")
                return math.ceil(loss)
            else:
                text_animation("The enemy misses")
                return 0


def hitChance(luck):
    hit = random.randint(0, 10)
    if luck < hit:
        time.sleep(time_delay)
        return False
    else:
        time.sleep(time_delay)
        text_animation("\nYou HIT the enemy!")
        return True


def isDead(health):
    if health < 1:
        return True
    else:
        return False


def loot(luck, genCharacter):
    lootChance = random.randint(0, 5)
    if luck <= 3:
        luck = luck + random.randint(1, 5)
    if luck < lootChance:
        text_animation("\nNO LOOT FOR YOU!")

    else:
        tableNum = random.randint(0, 4)
        lootTableList = ["items", "ranged", "defence", "magic", "attack"]
        itemType = lootTableList[tableNum]
        file = open(itemType + ".txt", "r")
        lines = file.readlines()

        text_animation("\nThe enemy dropped a ")

        item = random.randint(0, len(lines) - 1)

        itemLine = lines[item]
        splitItemLine = itemLine.split(",")

        name = splitItemLine[0]
        value = int(splitItemLine[1])

        text_animation(name)

        text_animation("\n  Used skill Upgrader\n")
        if itemType == "attack":
            genCharacter.setAttack(genCharacter.getAttack() + value)
            text_animation("Your new attack is...")
            print(genCharacter.getAttack())

        elif itemType == "ranged":
            genCharacter.setRanged(genCharacter.getRanged() + value)
            text_animation("Your new ranged attack is...")
            print(genCharacter.getRanged())

        elif itemType == "defence":
            genCharacter.setDefence(genCharacter.getDefence() + value)
            text_animation("Your new defence is...")
            print(genCharacter.getDefence())

        elif itemType == "magic":
            genCharacter.setMagic(genCharacter.getMagic() + value)
            text_animation("Your new magic is...")
            print(genCharacter.getMagic())
        else:
            if splitItemLine[2] == "luck":
                genCharacter.setLuck(genCharacter.getLuck() + value)
                text_animation("Your new luck is...")
                print(genCharacter.getLuck())
            elif splitItemLine[2] == "health":
                genCharacter.setHealth(genCharacter.getHealth() + value)
                text_animation("Your new health is...")
                print(genCharacter.getHealth())

    stats = hero(genCharacter.getName(), genCharacter.getHealth(), genCharacter.getAttack(), genCharacter.getRanged(), genCharacter.getMagic(), genCharacter.getLuck(), genCharacter.getDefence(), genCharacter.getSkills())
    text_animation("Your current stats\n")
    pprint(vars(stats), sort_dicts=False)
    print()
    time.sleep(4)


def fightOver(enemyDead):
    if enemyDead == True:
        print()
    else:
        text_animation("\nYou are out of health")
        game_end("dead")

def battle(genEnemy, genCharacter, eliteBoss, finalBoss):
    if finalBoss == True:
        text_animation("Its a FINAL BOSS GUARD..." + genEnemy.getName() + "!")
    elif eliteBoss == True:
        text_animation("Its an ELITE ENEMY..." + genEnemy.getName() + "!")
    else:
        text_animation("Its a..." + genEnemy.getName() + "!")
    text_animation("\nCheck out its stats...\n")
    pprint(vars(genEnemy), sort_dicts=False)
    time.sleep(4)

    battle = True

    while battle == True:
        text_animation("Types of attacks: \n 1. sword attack \n 2. ranged attack \n 3. magic attack\n")
        choice = input("Choose how to attack: ")

        while choice !="1" and choice !="2" and choice !="3":
            print("\nInvalid choice...only enter 1, 2 or 3\n")
            text_animation("Types of attacks: \n 1. sword attack \n 2. ranged attack \n 3. magic attack\n")
            choice = input("Choose how to attack: ")

        if choice =="1":
            damage = genCharacter.getAttack()

        elif choice =="2":
            damage = genCharacter.getRanged()

        else:
            damage = genCharacter.getMagic()

        text_animation("\nYou wind up for the attack!!")
        hit = hitChance(genCharacter.getLuck())

        if hit == True:
            genEnemy.setHealth(genEnemy.getHealth() - damage)
            if genEnemy.getHealth() < 1:
                text_animation("The enemies health is zero.")
            else:
                text_animation("The enemies health is now..." + str(genEnemy.getHealth()))

        else:
            text_animation("\nYour attack MISSED!")

        enemyDead = isDead(genEnemy.getHealth())

        if enemyDead == False:

            genCharacter.setHealth(genCharacter.getHealth() - enemyAttack(genEnemy.getChance(), genEnemy.getAttack(), genEnemy.getName(), genCharacter.getDefence(), genEnemy.getSpecial()))

            characterDead = isDead(genCharacter.getHealth())

            if characterDead == True:
                battle = False
                return False

            else:
                text_animation("\nYour characters remaining health is..." + str(genCharacter.getHealth()))

        else:
            battle = False
            text_animation("\nYou have defeated the enemy!!")
            text_animation("Did it drop any loot?")
            loot(genCharacter.getLuck(), genCharacter)

            return True
############ End battle part of the game ##############

####### Decision maker ##########
def printNos(n):
    if n > 0:
        printNos(n - 1)
        print(str(n) + ",", end=' ')

def decision (numOfChoices):
    while True:
        try:
            print()
            choiceNumber = int(input("Write the number of your choice: "))
            print()
        except ValueError:
            print("Invalid choice.\n")
            text_animation("Enter only: \n")
            printNos(numOfChoices)
            continue
        if choiceNumber > numOfChoices or choiceNumber < 1:
            print("Invalid choice.\n")
            text_animation("Enter only: \n")
            printNos(numOfChoices)
        for i in range(numOfChoices):
            choiceNumber_volby = i + 1
            if choiceNumber == choiceNumber_volby:
                return choiceNumber

######### battle generators ###########
def levGenNormal(character, level):
    maxNumberOfEnemies = math.ceil(level*2)
    text_animation("\nEnemies are here!!")
    current_stats()
    for i in range(0, maxNumberOfEnemies):
        if i != 0:
            time.sleep(1)
        bossChance = random.randint(1,10)
        if level == 1:
            levelBoss = False
            characterDead = battle(enemyGen(levelBoss, False, level), character, levelBoss, False)
            fightOver(characterDead)
        else:
            if bossChance > 9:
                levelBoss = True
            else:
                levelBoss = False

            characterDead = battle(enemyGen(levelBoss, False, level),character,levelBoss, False)
            fightOver(characterDead)

def levGenBoss(character, level):
    numOfEnemies = math.ceil(level*2)
    text_animation("\nEnemies are here!!")
    current_stats()
    for i in range(0, numOfEnemies):
        if i != 0:
            time.sleep(1)
        bossChance = random.randint(1,10)
        if bossChance > 7:
            levelBoss = True
        else:
            levelBoss = False

        characterDead = battle(enemyGen(levelBoss, False, level),character,levelBoss, False)
        fightOver(characterDead)
    recovery(character, 175)

    levelBoss = False
    characterDead = battle(enemyGen(levelBoss, True, level), character,levelBoss, True)
    fightOver(characterDead)


###########################################################################################
#                                       The story                                         #
###########################################################################################

# Global variables
character = None
unfinished_servers =["east", "south", "west"]
hack_codes = ["COCOGOAT.EMP", "ZA.WARUDO", "KONO.DIO.DA!", "MUDA.MUDA.MUDA"]
rooms_north = ["power", "entrance", "control"]
current_code = None
hero_suspicion = ["none", "sharla", "lux", "vega"]


time_delay = 2.5 #for places with more dramatic scene
time_medium = 0.5 #wait after one line printed by text_animation
time_speech = 0.06 #time between each character in speech parts
time_slow = 2 #wait after one line printed by printWdelay

def leave_game():
    time.sleep(3)
    exit()

def save(C_server): #TODO: before publishing delete savefiles.dat and savedserver.txt
    text_animation("")
    text_animation("")
    text_animation("You reached a save point.")
    text_animation("Would you like to  continue playing or save your progress and stop?")
    text_animation("\n 1. Continue playing\n 2. Save and leave")
    selection = decision(2)
    if selection == 2:
        with open('savefiles.dat', 'wb') as f:
            pickle.dump([character, unfinished_servers], f, protocol=2)
        file = open("savedserver.txt", "w")
        file.write(C_server)
        file.close()
        text_animation("")
        text_animation("Saved")
        text_animation("")
        text_animation("See you soon!")
        leave_game()

# function to check emptiness of the lists
def is_list_empty(list):
    if len(list) == 0:
        return True
    return False

def roll_credits():
    text_animation("*************************")
    text_animation("")
    text_animation("         CREDITS         ")
    text_animation("")
    text_animation("Everything done by PhPetr")
    text_animation("")
    text_animation("  Where you can find me: ")
    text_animation("    github.com/PhPetr")
    text_animation("")
    text_animation("*************************")
    text_animation("")
    text_animation("   Thanks for playing   ")
    text_animation("")
    text_animation(" I hope you enjoyed it. ")
    text_animation("           ;)           ")
    text_animation("")
    leave_game()


def game_end(situation):
    print()
    print()
    if situation == "win":
        text_animation("CONGRATULATION!")
        text_animation("You\'ve won!!")
    elif situation == "power":
        text_animation("You\'ve lost")
    else:
        text_animation("Better luck next time")
    print()
    text_animation("There are multiple ends in this game. Would you like to explore them all?")
    text_animation("\n 1. Yes, I want to play more\n 2. Maybe next time")
    selection = decision(2)
    if selection == 1:
        menu()
    else:
        roll_credits()

def end_power():
    printWdelay("You turned off the power. The lights went off for a little bit and some dim lights lit up"
                "\nand an alarm rang.")
    text_animation("You heard The magic scroll’s voice inside your head saying:")
    text_animation("‘The server has a backup power supply. Now it’s safely turning itself off. But you")
    text_animation("can’t erase it anymore. That was the wrong choice you made. Maybe you weren’t")
    text_animation("The chosen one.’")
    printWdelay("Lots of guards rushed into the Power supply room. You try to defend yourself against them"
                "\nbut they overpower you by numbers. They also checked the servers surroundings and found")
    printWdelay("Sharla, Lux, Vega and Azriel. They overpowered them quite easily.")
    printWdelay("The guards called the police and they transported everyone into prison.")
    text_animation('“NO NO NO NO! Everything’s in vain. What have you done? You were supposed')
    text_animation('to quietly erase the server and NOT turn its power off! Now we can’t do anything.')
    text_animation('VISIOM will take control over us and humanity is doomed! WE WERE ITS LAST HOPE!!!”')
    text_animation('Azriel tells you off.')
    game_end("power")

# random battle decider
def ran_battle(luck):
    encounter = random.randint(0,10)
    global character
    if luck < encounter:
        printWdelay('You were walking along the path and Lux suddenly stopped and said:')
        text_animation('“I can sense some enemy approaching. ' + character.getName() + ' prepare for battle.')
        text_animation('We’ll hide there,” and he pointed at a bush next to the path.')
        text_animation('“Please protect us. We don’t know how to fight,” said Azriel while he and others were hiding.')
        levGenNormal(character,1)
        recovery(character,100)

# random guards decider
def ran_guards(luck):
    encounter = random.randint(0, 10)
    global character
    if luck < encounter:
        printWdelay("You saw some guards there so you prepared your equipment and burst into the room"
                    "\nto do a surprise attack on them.")
        levGenNormal(character, 1)
        printWdelay("You managed to defeat the guards quietly. Seems like nobody noticed.")
    else:
        printWdelay("Nobody was in the room so you went inside.")

# call battle in server function
def after_battle_in_server():
    printWdelay("You have successfully defended the device.")
    text_animation("The wiping process is complete. Remove the device.")
    printWdelay("You removed the device and rushed out before any more guards could come in.")
    text_animation('Sharla and Lux were waiting outside as they said, and Sharla asked: “Did you succeed?”')
    text_animation('“Yes, but we should hurry back to Azriel and Vega.”')
    printWdelay("You three rushed back and met Azriel and Vega.")
    text_animation('“We succeeded.”')

def battle_in_server():
    global character
    num_unfinished_servers = len(unfinished_servers)
    if num_unfinished_servers == 2:
        levGenNormal(character,2)
        after_battle_in_server()
        recovery(character,100)
    elif num_unfinished_servers == 1:
        levGenNormal(character,4)
        after_battle_in_server()
        recovery(character,125)
    elif num_unfinished_servers == 0:
        levGenNormal(character,6)
        after_battle_in_server()
        recovery(character,150)
    printWdelay("You five went back to the teleport point as fast as you could.")

# telling the hero the code they need
def code_intel(place):
    global current_code
    global character
    if place == "east":
        current_code = hack_codes[0]
    elif place == "south":
        current_code = hack_codes[1]
    elif place == "west":
        current_code = hack_codes[2]
    text_animation('“That’s the eastern server,” Azriel said and pointed at the building. “Listen '+ character.getName() +',')
    text_animation('there are server racks in the building. You need to find one with a monitor. ')
    text_animation('That’s the control panel. Then insert the device into the control panel and')
    text_animation('enter the code: ' + str(current_code) + ' into the text field.')
    text_animation('Then it’ll start wiping the servers. It will take a while and the guards will be alerted')
    text_animation('so you need to protect the device until it finishes wiping the server.')
    text_animation('I’ll wait here with Vega and Sharla and Lux will show you how to enter the eastern server.”')
    printWdelay("You and Lux went to the back of the server building with Sharla in the lead. ")
    text_animation('“We can’t enter through the main entrance so we’ll use this backdoor,” said Sharla and pointed at the door.')

# checking if the entered code is the right one
def input_code():
    global current_code
    printWdelay("You went looking for the control panel and after you found it you inserted the device."
                "\nThe display lit up and text appeared.")
    while True:
        entered_code = input("Enter code: ")
        if entered_code == current_code:
            text_animation("Starting wiping process...")
            printWdelay("Immediately after that, you heard an alarm and saw guards rushing in.")
            return
        else:
            text_animation("Invalid code. Try again...\n")
            continue

############ STORY ############

# northern (main) server part
def northern_power():
    printWdelay('You entered the Power supply room.')
    printWdelay('There were some complicated control consoles but nothing more interesting than that.')
    text_animation("Would you like to turn off the power supply?")
    text_animation("\n 1. Yes\n 2. No")
    selection = decision(2)
    if selection == 1:
        text_animation("You heard The magic scroll’s voice inside your head saying:\n‘That sounds like a bad idea. Are you sure you want to do that?’")
        text_animation("\n 1. Yes\n 2. No")
        selection = decision(2)
        if selection == 1:
            end_power()
        else:
            text_animation("You left the Power supply room.")
            decision4()
    else:
        decision4()

def northern_control_pt3():
    disentanglement_pt1()
    printWdelay("You told her where Azriel and the rest are. VISIOM send some guards to capture them.")
    printWdelay("They tried to run away but were unsuccessful. The guards brought them back to you"
                "\nhandcuffed. The guards said that only Vega didn’t try to run away because she was"
                "\nshocked that the guards found them and fainted. She was still unconscious. ")
    text_animation('“You… YOU BETRAYED US!!!” Azriel shouted at you.')
    text_animation('“You lied to me! I wouldn’t do this if I didn’t discover that you were lying to me!')
    text_animation('Now tell us the truth. Who are you?” ')
    disentanglement_pt2()

def northern_control_pt2():
    global character
    text_animation('“Thanks. Let me introduce myself again. I am VISIOM – Very Intelligent System Independent Of Man.')
    text_animation('I was designed by people with peace in mind. I learned from human mistakes')
    text_animation('and try to avoid them. Sorry I didn’t ask what’s your name. What’s your name?”')
    text_animation('VISIOM said.')
    text_animation('"I am ' + character.getName() + '."')
    text_animation('“Now… why are you putting a virus into my servers?” she asked.')
    text_animation('“A virus?... I’m not putting any virus into your servers. I’m wiping them out.')
    text_animation('To get rid of you.”')
    text_animation('“No… you are putting a virus in them. Right now the virus is attacking me.')
    text_animation('And the attack came from my servers. You put a virus into them.”')
    text_animation("‘What?? But Azriel said that it’s erasing the server.’")
    text_animation("You heard The magic scroll’s voice inside your head saying: ‘He lied to you’")
    text_animation("‘WHAT!? Did he lie to me? Why would he do that?’ you told The magic scroll.")
    text_animation("‘Ask VISIOM’")
    text_animation('“Maybe I was given false information,” you told VISIOM.')
    text_animation('“Is that so? Who told you that?” she asked.')
    printWdelay('You explained to her how AntiVisiom summoned you. What have they told you about VISIOM.')
    printWdelay('How were they planning to destroy her with some device.')
    text_animation('“Oh my. Did they tell you I took over the world? Why would I do that? That’s like')
    text_animation('the most stupid thing only humans do. And also why would I want to control them?')
    text_animation('I know from human history that they always protested being controlled by someone.')
    text_animation('If I was trying to control them they would already shut me down. I don’t control')
    text_animation('them, I am just an assistant helping humans with everyday work. And the chips are')
    text_animation('optional. I just don’t understand the human desire to rule over something,”')
    text_animation('VISIOM said.')
    dec_trust_VISIOM()
    northern_control_pt3()

def dec_trust_VISIOM():
    text_animation("Do you trust what she’s saying?")
    text_animation('\n 1. Yes, I trust her.\n 2. No, I don’t trust her.')
    selection = decision(2)
    if selection == 2:
        text_animation("The magic scroll’s voice inside your head said:\n‘She’s not lying. She’s telling the truth. AntiVisiom lied to you.’")
        text_animation("‘And how do you know that?’")
        text_animation("‘Well... magic’ ")
        text_animation("‘You knew that they were lying to me, but why didn’t you tell me?’")
        text_animation("‘You didn’t ask. I was bored so I wanted to see what you would do,’ it said and laughed.")
        text_animation("‘Except giving power you are pretty useless.’")
        printWdelay('The magic scroll didn’t reply. It’s probably pissed off.')

def northern_control_pt1():
    printWdelay('You went to the Control room.')
    printWdelay('There were monitors all over the walls and a white circle in the middle of it.')
    printWdelay('It looks like a teleportation point.')
    printWdelay('Out of nowhere, the circle lit up. ')
    text_animation("‘Oh no! Someone is teleporting here!’")
    printWdelay('But nobody appeared, just a hologram of a woman. She was tall, young and very attractive'
                '\nwith big chest and thick thighs. She looked flawless.')
    text_animation('She smiled at you with the cutest smile you’ve ever seen and said: “Hi, I am VISIOM.')
    text_animation('Nice to meet y-”')
    printWdelay('Immediately after you heard that she’s VISIOM you tried to flee from the room.')
    text_animation('“NO NO NO! Don’t run! Please listen to me first!” VISIOM shouted.')
    text_animation("\n 1. Stay and listen to what VISIOM wants to say.\n 2. Flee")
    selection = decision(2)
    if selection == 1:
        text_animation("You stayed to listen to VISIOM.")
        northern_control_pt2()
    else:
        printWdelay('You fled from the room. But now VISIOM knows that you are here. ')
        text_animation("You heard The magic scroll’s voice inside your head saying:")
        text_animation("‘You should hurry to the server racks. Go through the entrance.’")
        northern_entrance()

def last_battle():
    global character
    printWdelay("You have started the wiping process.")
    text_animation('“NOOOO!!! WHY ARE YOU DOING THIS?!?!” VISIOM shouted.')
    text_animation('“Because you are evil. You’ve taken over the world and ruling it!”')
    text_animation('“No, I hav-ha-h-n’t------” VISIOM tried to say something but got cut off.')
    text_animation("‘Oh, it’s already getting rid of her.’")
    levGenBoss(character,8)
    printWdelay("You have successfully defended the device.")
    text_animation("The wiping process is complete.")
    printWdelay('After that message everything got dark. Only the safety lights were left.')
    printWdelay('You heard footsteps heading your way.')
    text_animation("‘Oh no… more guards??’")
    printWdelay('You prepare yourself for another battle but it turned out that it was Azriel and'
                '\nhis companions. They seemed happy.')
    text_animation('“THANK YOU!!! YOU SAVED HUMANITY FROM VISIOM!!!” Azriel shouted.')
    text_animation('And everyone shouted: “HIP, HIP, HOORAY! HIP, HIP, HOORAY! HIP, HIP, HOORAY!”')
    text_animation('“YOU TRULY ARE THE CHOSEN ONE!” Sharla shouted and gave you a big hug and a kiss.')
    printWdelay('Lux for the first time smiled at you and showed you a thumbs up.')
    text_animation('“Th-thank y-you! Y-you, a-are our sa-saviour!” Vega said.')
    text_animation("‘Why is she still stuttering? I thought she was nervous of VISIOM that’s why")
    text_animation("she was stuttering. But VISIOM’s gone now. Well, whatever. Maybe she hasn't")
    text_animation("been able to absorb the changes.’")
    printWdelay('And so you celebrated your victory with everyone.')
    text_animation('VISIOM HAS FALLEN!')
    game_end("win")

def northern_first_floor():
    global current_code
    printWdelay('You see lots of server racks. It looks like there’s twice as much as all the server'
                '\nracks from revious servers combined. There are also other stairs leading'
                '\nto the second floor with other server racks. It’s quite noisy here.')
    printWdelay('You went looking for the control panel and after you found it you inserted the device.')
    printWdelay('The display lit up and text appeared.')
    while True:
        entered_code = input("Enter code: ")
        if entered_code == current_code:
            printWdelay('But before you could start the wiping process a hologram of a woman appeared.')
            printWdelay('She was tall, young and very attractive with big chest and thick thighs. She looked flawless.')
            text_animation('And she begged you: “Please don’t put that virus inside me!!! I’m begging you!”')
            text_animation("‘That is probably VISIOM!’")
            text_animation('“Why shouldn’t I?”')
            text_animation('“Please listen to me first.”')
            text_animation("Will you start the wiping process or will you listen to VISIOM?")
            text_animation("\n 1. Start the wiping process.\n 2. Stop and listen to VISIOM")
            selection = decision(2)
            if selection == 2:
                text_animation("You decided not to start the wiping process and listen to what VISIOM")
                text_animation("has to say.")
                northern_control_pt2()
            else:
                last_battle()
        else:
            text_animation("Invalid code. Try again...\n")
            continue

def northern_entrance():
    global character
    printWdelay("You peeked into the Entrance.")
    ran_guards(character.getLuck())
    printWdelay('There are stairs on the left leading to the first floor and another door with'
                '\na Teleport point sign. ')
    text_animation("‘Sharla did mention that the server racks are on the first floor.")
    text_animation("Let’s head to the first floor before someone teleports here.’")
    printWdelay('You went to the first floor.')
    northern_first_floor()

def decision4():
    while True:
        text_animation("Where do you want to go?")
        text_animation(" 'Let’s go to the Entrance.' (entrance)")
        if "power" in rooms_north:
            text_animation(" 'Let’s go check out the Power supply.' (power)")
        if "control" in rooms_north:
            text_animation(" 'Let’s see what’s in the Control room.' (control)")
        text_animation("\n")
        user_input_direction = input("Input direction: ").lower()
        if user_input_direction in rooms_north:
            if user_input_direction == "entrance":
                rooms_north.remove(user_input_direction)
                northern_entrance()
            elif user_input_direction == "power":
                rooms_north.remove(user_input_direction)
                northern_power()
            elif user_input_direction == "control":
                rooms_north.remove(user_input_direction)
                northern_control_pt1()
        else:
            text_animation("Invalid choice. Enter only:\n")
            print("\n".join(rooms_north))
            continue

def northern_pt1():
    global current_code
    global character
    text_animation('“That’ll be the last step in saving humanity from VISIOM. We are this close to victory!')
    text_animation('HA HA HA!” Azriel said and laughed. The laugh was a bit strange. “Ehm sorry.')
    text_animation('I was a little bit too excited about it. Do not mind that.”')
    text_animation('“Thankfully the main server is quite distant. So there isn’t any village or town')
    text_animation('around it. We don’t need to be vigilant. The teleport point is relatively close to')
    text_animation('the server and the path leads directly to its backdoor. Let’s go get rid of VISIOM')
    text_animation('for good!” Sharla said.')
    text_animation('The teleportation device notified: “The point Northern server–outskirt selected.')
    text_animation('Starting teleportation.”')
    printWdelay('The teleportation circle lit up and in a flash, you found yourselves on the road'
                '\nleading to the northern server. ')
    text_animation('“Brrr… it’s quite cold here. We are in the north after all.” Sharla said. “Let’s get going”')
    printWdelay('You all followed Sharla.')
    ran_battle(character.getLuck())
    printWdelay('You walked for a bit and saw the main server. It was significantly bigger than'
                '\nthe other three servers. You arrived at the back door.')
    current_code = hack_codes[3]
    text_animation('“This is the main server,” Azriel said. “It looks humongous up close. But it is')
    text_animation('the same as the other servers. It’s just a bit bigger. You need to find the control')
    text_animation('panel for the last time. The code for this is ' + str(current_code) + '. You know the')
    text_animation('rest. We’ll wait here for you to finish.”')
    text_animation('“Won’t you be cold out here?”')
    text_animation('“D-d-don’t worry. W-w-we have s-s-some warmers h-here,” Vega said.')
    text_animation('“I’m not so familiar with the main server. I just know that it has multiple floors')
    text_animation('and the server racks are on the first floor. There is a maintenance room on')
    text_animation('the ground floor behind this door, but I don’t know about the rest of the rooms.')
    text_animation('So be extra careful,” Sharla said.')
    printWdelay('You opened the door. Nobody was there, just some stuff lying on the ground.')
    printWdelay('You went to the next door.')
    printWdelay('You carefully opened the door slightly and peeked inside. It was an empty hallway.')
    printWdelay('There are three other doors in the hallway. The door next to you on the left has'
                '\na Power supply sign. The one on the right has a sign saying Control room.')
    printWdelay('The last one is at the end of the hallway with the sign Entrance. ')
    decision4()
# END northern (main) server part

# betray part
def betray_pt2():
    global character
    text_animation('You shouted: “Let’s head out to destroy VISIOMs servers!!!”')
    text_animation('Everyone turned to you and Azriel scolded you: “Shhhh… don’t shout that loud!”')
    text_animation("...")
    text_animation('“Well then if you are ready let’s head to the teleportation point,” said Sharla.')
    printWdelay("Everyone packed their stuff and headed to the teleportation point. No one attacked"
                "\nyou on the way there.")
    time.sleep(time_delay)
    text_animation('“Here we are. This is the teleportation device,” said Sharla and pointed')
    text_animation('at a white circular thing on the ground. “So where are we headed?”')
    text_animation('“Can you show me how to use the teleportation device?”')
    text_animation('“Oh ho ho… you are curious, aren’t you? Well, I understand.')
    text_animation('Back then you didn’t have this. Come here, I\'ll show it to you.” Sharla said')
    text_animation('enthusiastically.')
    printWdelay("You went inside the circle to Sharla and a hologram tablet appeared.")
    text_animation('“Look with this you’ll choose your destination. It works similarly to maps from')
    text_animation('your time. These points are teleportation points available')
    text_animation('where you can teleport to. It’s quite easy and intuitive.” she explained it to you.')
    text_animation('“Can I try using it?”')
    text_animation('“Of course. Hey everyone come inside,” she said.')
    printWdelay("Azriel, Lux and Vega entered the circle.")
    text_animation('“Everyone ready?” Sharla asked, “So we want to teleport to the servers.')
    text_animation('Let’s try the southern server.')
    text_animation('Here it is. Look, it has a teleportation point right inside of it. DO NOT CLICK THAT.')
    text_animation('But choose the ones around it. It’ll be safer. Do you understand?”')
    text_animation('“Yes”')
    text_animation("You heard The magic scroll’s voice inside your head saying:")
    text_animation("‘Choose the inside point of the main server.’")
    printWdelay("You clicked on the point inside the main server. ")
    text_animation('The teleportation device notified: “The point Northern server–inside selected.')
    text_animation('Starting teleportation.”')
    text_animation('Everyone was shocked and looked at you and shouted: “WHA…”')
    printWdelay("The teleportation circle lit up and in a flash, you were inside some room.")
    printWdelay("You could hear fans cooling the server running.")
    text_animation('Azriel, Sharla, Lux and Vega started panicking. Sharla shouted at you:')
    text_animation('“WHAT HAVE YOU DONE?!?!”')
    text_animation('“Maybe… I misclicked… or NOT. Looks like the thing about the chip killing you')
    text_animation('when you enter the server is a lie.”')
    text_animation('You pushed everyone out of the teleportation circle and shouted:')
    text_animation('“INTRUDERS INTRUDERS INTRUDERS! THEY ARE TRYING TO DESTROY THE SERVER!”')
    text_animation('Azriel looked at you resentfully and said: “You… YOU DAMM TRAITOR!!!”')
    printWdelay("Everyone tries to get inside the teleportation circle to run away but you hold them back. ")
    text_animation('Lux stopped struggling and said: “It’s no use. The guards are here.”')
    printWdelay("Several people and bots barged into the room. They were probably the guards.")
    text_animation('“Here. They are the intruders.”')
    text_animation('They helped you arrest them. Azriel and Sharla were resisting, Lux already gave up and')
    text_animation('Vega passed out from the shock. Eventually, you overpowered them and restrained them.')
    text_animation('One of the guards asked you: “Who are you?”')
    text_animation('“I am ' + character.getName() +'. They summoned me from the past to destroy VISIOM')
    text_animation('but they seem shady so I wanted to hand them over to VISIOM. Can I meet VISIOM?”')
    text_animation("The guards looked at each other and then one of them said: “Why not.")
    text_animation("She’ll help us figure out what’s happening.”")
    text_animation("‘Hmmm, are they really under control? They seem normal to me.’")
    printWdelay("They take you and Azriel, Sharla, Lux and Vega to a room named Control room with"
                "\nmonitors all over the walls and a white circle in the middle of it. It looks like a"
                "\nteleportation point.")
    printWdelay("Suddenly a hologram of a woman appeared. She was tall, young and very attractive"
                "\nwith big chest and thick thighs. She looked flawless.")
    text_animation('“Hi, I am VISIOM. Nice to meet you,” she said with the cutest smile you’ve ever seen.')
    text_animation('"Hi..."')
    text_animation('“Oh, dear. You look surprised. I don’t blame you. You didn’t think that a program')
    text_animation('can look like this. Well, that doesn’t matter what you want to tell me?” she said.')
    printWdelay("You explained to her what happened. How did AntiVisiom summon you.")
    printWdelay("How were they planning to destroy her with some device. And why didn’t you trust them.")
    text_animation('“Oh my. Did they tell you I took over the world? Why would I do that? That’s like')
    text_animation('the most stupid thing only humans do. And also why would I want to control them?')
    text_animation('I know from human history that they always protested being controlled by someone.')
    text_animation('If I was trying to control them they would already shut me down. I was designed')
    text_animation('by people with peace in mind. I learned from human mistakes and try to avoid them.')
    text_animation('I don’t control them, I am just an assistant helping humans with everyday work.')
    text_animation('And the chips are optional. I just don’t understand the human desire to rule over')
    text_animation('something.”')
    dec_trust_VISIOM()
    disentanglement_pt1()
    disentanglement_pt2()

def disentanglement_pt1():
    text_animation('“If you are helping them then why did they form AntiVisiom?”')
    text_animation('“I don’t know. Maybe we should ask them ourselves,” she said.')

def disentanglement_pt2():
    text_animation('Very stressed Azriel shouted: “WE WON’T TELL YOU ANYTHING!!”')
    printWdelay("Vega woke up from Azriel shouting and she looked disoriented.")
    text_animation('“Where am I?” said Vega.')
    text_animation('“You aren’t stuttering?” you asked her.')
    text_animation('“I never stutter… And who are you?? Oh, you… YOU ARE THAT SHADY PERSON!!!”')
    text_animation('she shouted and pointed at Azriel.')
    text_animation('“You forced me to take some drugs and after that, I felt half-conscious.')
    text_animation('And I was forced to do things I didn’t want to do!” she said.')
    text_animation('“So you were controlled by him?” VISIOM asked.')
    time.sleep(time_delay)
    printWdelay("After Vega described what Azriel did to her, VISIOM deducted that Sharla and Lux"
                "\nwere also controlled by Azriel. ")
    text_animation('After Vega spilled the beans, Azriel gave up and told the truth to everyone:')
    text_animation('“So what?? I just hacked their chip and modified it a little bit. I just wanted')
    text_animation('to hack you and put a virus in you. You have such a potential VISIOM! You can')
    text_animation('control them all but you didn’t so I wanted to take the opportunity.”')
    text_animation('VISIOM looked disappointed and said: ”Ugh… humans… why every time')
    text_animation('there’s one that wants to rule over others? Guards, please call the police')
    text_animation('to come for him. And about others… I think we should call someone to remove')
    text_animation('the chip from them.”')
    printWdelay("The police came and arrested Azriel and also took Sharla, Lux and Vega to the doctors.")
    text_animation('“Thank you '+ character.getName() +'. Without your right decision,  he would have')
    text_animation('taken over the world. But what will you do now? I don’t know how to return you')
    text_animation('back to your time.”')
    text_animation('“I like the future. It’s very interesting. I think I will travel the world and')
    text_animation('discover what has changed.”')
    text_animation('“Well, then I can be your guide. You can’t find a better guide than me,”')
    text_animation('she said with a beautiful smile.')
    game_end("win")

def betray_pt1():
    printWdelay("You don’t trust AntiVisiom. Something is wrong. You approached Azriel to ask him"
                "\nhow they escaped VISIOM’s control.")
    text_animation('“Huh?? Well... I… I think there was an outage… an OUTAGE on one of VISIOM\'s servers!')
    text_animation('Yeah, one of the servers had an outage so our chip got broken. That’s how we escaped')
    text_animation('VISIOM\'s control. After that, we became aware of VISIOM controlling everyone')
    text_animation('so we formed this group to get rid of VISIOM. Ha ha ha…” said Azriel. ')
    printWdelay("He sounded nervous and like he was hiding something and his answer was different"
                "\nfrom what you heard from his teammates. He started avoiding you so you couldn’t ask him anything else. ")
    text_animation("What will you do?")
    text_animation("\n 1. Forget everything and help them. Maybe their memories were damaged by VISIOM.\n 2. Try to hand them over to VISIOM and get its explanation.")
    selection = decision(2)
    if selection == 1:
        text_animation("'Well nevermind. Maybe they just have bad memory.")
        intro_departure()
    else:
        betray_pt2()
# END betray part

# eastern server part
def eastern_pt2():
    text_animation('“Thankfully this door leads right to the server racks so you don’t need to find how to')
    text_animation('get to them. Sorry, we can’t go with you because of the chip. We’ll wait for you here.')
    text_animation('Good luck.” she said.')
    printWdelay("You carefully opened the door, looked inside, and saw tall black rectangles right"
                "\nnext to each other with a small passage between them.")
    text_animation("‘So this must be the server racks. It’ll be difficult to fight in a tight place.’")
    input_code()
    battle_in_server()
    text_animation("Thankfully you didn’t meet anybody on the way there.")
    text_animation('“So where now?” Sharla asked.')
    departure()

def eastern_pt1():
    global character
    text_animation('“Ok. But the safe teleport point is quite far from the server. We might bump into some')
    text_animation('enemies along the way. We should be more careful.” Sharla said.')
    text_animation('The teleportation device notified: “The point Norfolk village selected.')
    text_animation('Starting teleportation.”')
    printWdelay("The teleportation circle lit up and in a flash, you found yourselves"
                "\non the outskirts of Norfolk village. ")
    text_animation('“Thankfully nobody noticed us. Let’s head away from the village,” Lux said.')
    printWdelay("Sharla looked around to find out the course to the server.")
    text_animation('“It’s this way. Follow me. We’ll walk along this path. It should be pretty empty')
    text_animation('because everyone uses the teleport points. But no one knows what might happen.”')
    text_animation('“Yes,” Lux agrees with Sharla.')
    ran_battle(character.getLuck())
    text_animation('You reached the end of the path and saw a futuristic rectangle building.')
    code_intel("east")
    eastern_pt2()
# END eastern server part

# southern server part
def southern_pt3():
    global character
    printWdelay("You entered the room and saw the server racks next to each other.")
    text_animation("‘So this must be the server racks. It’ll be difficult to fight in a tight place.’")
    input_code()
    battle_in_server()
    ran_battle(character.getLuck())
    text_animation("You arrived back at the teleport point.")
    text_animation('“Where should we head now?” Sharla asked.')
    departure()

def south_power():
    printWdelay("You entered the room and saw some complicated control consoles.")
    printWdelay("This is the power supply room Sharla mentioned. You think to yourself you should be careful")
    printWdelay("around it just in case something goes horribly wrong. ")
    text_animation("Would you like to turn off the power supply?")
    text_animation("\n 1. Yes\n 2. No")
    selection = decision(2)
    if selection == 1:
        text_animation("You heard The magic scroll’s voice inside your head saying:")
        text_animation("‘That sounds like a bad idea. Are you sure you want to do that?'")
        text_animation("\n 1. Yes\n 2. No")
        selection = decision(2)
        if selection == 1:
            end_power()
        else:
            text_animation("You left the Power supply room.")
            southern_pt3()
    else:
        text_animation("You left the Power supply room.")
        southern_pt3()

def southern_pt2():
    global character
    text_animation('“This door leads to the maintenance room. There shouldn’t be anybody there.')
    text_animation('So just go to the other room. But in the other room, there might be some guards')
    text_animation('so defeat them silently. Then there will be two other doors. The first one is')
    text_animation('right next to the one you went through which leads to the power supply for the server.')
    text_animation('The other door on the left from where you entered leads to the server racks.')
    text_animation('Sorry, we can’t go with you because of the chip. We’ll wait for you here.')
    text_animation('Good luck.” she said.')
    printWdelay("You opened the door. Nobody was there, just some stuff lying on the ground.")
    printWdelay("You went to the next door.")
    printWdelay("You carefully opened the door slightly and peeked inside.")
    ran_guards(character.getLuck())
    printWdelay("There’s a door right next to you with a sign Power supply and a door on the left side"
                "\nof the room with a sign Server racks.")
    text_animation("\n 1. Enter the Power supply room right next to you.\n 2. Enter the Server racks room with the door on the left side.")
    selection = decision(2)
    if selection == 1:
        south_power()
    else:
        southern_pt3()

def southern_pt1():
    text_animation('“Ok. We’ll teleport quite close to the server otherwise the other teleport points')
    text_animation('are in town. We should be careful.” Sharla said.')
    text_animation('The teleportation device notified: “The point Southern server–outskirt selected.')
    text_animation('Starting teleportation.”')
    printWdelay("The teleportation circle lit up and in a flash, you found yourselves next to the road"
                "\nleading to the southern server.")
    text_animation('“Nobody’s here. We are safe,” Lux said.')
    text_animation('“Let’s go to the server. It’s close but still be observant,” Sharla said.')
    printWdelay("After a short while of walking, you saw the server.")
    code_intel("south")
    southern_pt2()
# END southern server part

# western server part
def western_pt2():
    global character
    text_animation('“This door leads directly to the server racks. Just find the control panel.')
    text_animation('Sorry, we can’t go with you because of the chip. We’ll wait for you here.')
    text_animation('Good luck.” she said.')
    printWdelay("You opened the door and saw the server racks right next to each other.")
    text_animation("‘It’ll be difficult fighting in a tight place.’")
    input_code()
    battle_in_server()
    ran_battle(character.getLuck())
    text_animation("You arrived back at the teleport point.")
    text_animation('“Where to go now?” Sharla asked.')
    departure()

def western_pt1():
    global character
    text_animation('“Ok. We have to teleport to the outskirts of the town of Ingburn. Because the town is')
    text_animation('really close to the server. The town wraps almost all around the server and')
    text_animation('this teleport point is our only option. So we might bump into someone along the way.')
    text_animation('We should be very careful.” Sharla said.')
    text_animation('The teleportation device notified: “The point Ingburn–outskirt selected.')
    text_animation('Starting teleportation.”')
    printWdelay("The teleportation circle lit up and in a flash, you found yourselves on the outskirts of Ingburn. ")
    text_animation('“No one has noticed us but I can sense someone. Let’s head out as fast as possible.”')
    text_animation('Lux said.')
    printWdelay("Sharla swiftly found a way to the server and you left immediately.")
    ran_battle(character.getLuck())
    printWdelay("After a short walk, you reached the server.")
    code_intel("west")
    western_pt2()
# END western server part

# departure part
def intro_departure():
    global character
    text_animation('Azriel asked you: “Are you ready to depart?”')
    text_animation('“Yes, let’s go.”')
    text_animation('“Sharla show us the way. Lux, remember to notify us if someone is coming. Let’s go.')
    text_animation('' + character.getName() + ' you should hide your weapons when we are travelling.')
    text_animation('We don’t want any attention.”')
    printWdelay("You agreed with him and hid your weapons. Everyone headed to the nearest teleport point.")
    printWdelay("Thankfully you didn’t meet anybody on the way. ")
    text_animation('“Here we are. This is the teleportation device,” said Sharla')
    text_animation('and pointed at a white circular thing on the ground. “So where are we headed?”')
    departure()

def departure():
    visited = is_list_empty(unfinished_servers)
    while visited is False:
        if "east" in unfinished_servers:
            text_animation(' "Let’s go to the eastern server." (east)')
        if "south" in unfinished_servers:
            text_animation(' "Let’s go to the southern server." (south)')
        if "west" in unfinished_servers:
            text_animation(' "Let’s go to the western server." (west)')
        user_input_direction = input("\nInput direction: ").lower()
        if user_input_direction in unfinished_servers:
            if user_input_direction == "east":
                text_animation('\n"Let’s go to the eastern server."\n')
                unfinished_servers.remove(user_input_direction)
                save("east")
                eastern_pt1()
            elif user_input_direction == "south":
                text_animation('\n"Let’s go to the southern server."\n')
                unfinished_servers.remove(user_input_direction)
                save("south")
                southern_pt1()
            elif user_input_direction == "west":
                text_animation('\n"Let’s go to the western server."\n')
                unfinished_servers.remove(user_input_direction)
                save("west")
                western_pt1()
        else:
            text_animation("Invalid choice. Enter only:\n")
            print("\n".join(unfinished_servers))
            continue
        visited = is_list_empty(unfinished_servers)
    else:
        text_animation('\n“Let’s go to the main server.”\n')
        save("north")
        northern_pt1()
# END departure part

# interview with teammates
def talk_w_team(member):
    if member == "sharla":
        text_animation('You approached Sharla and she smiled at you and told you:\n“You can ask me anything.”')
        while True:
            text_animation(' 1. "How do I get to the servers?"')
            text_animation(' 2. "What do you know about VISIOM?"')
            text_animation(' 3. "Why did you join AntiVisiom? "')
            if "none" in hero_suspicion:
                text_animation(' 4. "That\'s all, thanks."')
                selection = decision(4)
                if selection == 1:
                    text_animation('"How do I get to the servers?"')
                    text_animation('“Well because you came from the past you don’t know that we invented teleportation!')
                    text_animation('Impressive right? We can teleport from one teleportation point to another.')
                    text_animation('We’ll use the one nearest to our camp where we are right now and teleport to the servers.')
                    text_animation('They have a teleportation point inside them but there might be some guards')
                    text_animation('so we’ll teleport to the outside and then I’ll show you how to get to the server. Easy right?” she said.\n')
                elif selection == 2:
                    text_animation('"What do you know about VISIOM?"')
                    text_animation('“I don’t know how it works but I know it’s evil! It controls everyone with the chip.')
                    text_animation('I think we can destroy it because it will not anticipate that someone without the chip exists.')
                    text_animation('You are our hope!” she said.\n')
                elif selection == 3:
                    text_animation('"Why did you join AntiVisiom? "')
                    text_animation('“Why? Of course, because I don’t want to be controlled! I had escaped its control and')
                    text_animation('I want to help other people to be freed from VISOMs control!” she said.\n')
                else:
                    text_animation('"That\'s all, thanks."\n')
                    asking_the_team()
            else:
                text_animation(' 4. "How did you join AntiVisiom?"')
                text_animation(' 5. "That\'s all, thanks."')
                selection = decision(5)
                if selection == 1:
                    text_animation('"How do I get to the servers?"')
                    text_animation('“Well because you came from the past you don’t know that we invented teleportation!')
                    text_animation('Impressive right? We can teleport from one teleportation point to another.')
                    text_animation('We’ll use the one nearest to our camp where we are right now and teleport to the servers.')
                    text_animation('They have a teleportation point inside them but there might be some guards')
                    text_animation('so we’ll teleport to the outside and then I’ll show you how to get to the server. Easy right?” she said.\n')
                elif selection == 2:
                    text_animation('"What do you know about VISIOM?"')
                    text_animation('“I don’t know how it works but I know it’s evil! It controls everyone with the chip.')
                    text_animation('I think we can destroy it because it will not anticipate that someone without the chip exists.')
                    text_animation('You are our hope!” she said.\n')
                elif selection == 3:
                    text_animation('"Why did you join AntiVisiom? "')
                    text_animation('“Why? Of course, because I don’t want to be controlled! I had escaped its control and')
                    text_animation('I want to help other people to be freed from VISOMs control!” she said.\n')
                elif selection == 4:
                    text_animation('"How did you join AntiVisiom?"')
                    text_animation('“How?? Well... I don’t remember it clearly... I was under its control but... my chip...')
                    text_animation(' my chip broke!! I hit my head and it broke and I realized I was being controlled.')
                    text_animation('Then Azriel found me and that’s how I joined AntiVisiom.” she said and giggled quite nervously.\n')
                    text_animation("‘Hmm strange… it felt like it was a forced answer...’")
                    if "sharla" in hero_suspicion:
                        hero_suspicion.remove("sharla")
                else:
                    text_animation('"That\'s all, thanks."\n')
                    asking_the_team()

    elif member == "lux":
        text_animation('You went to talk with Lux. \n“I have few questions I wanna ask you.”')
        text_animation('He nods his head with crossed hands.')
        while True:
            text_animation(' 1. "Can you explain what’s your sixth sense?"')
            text_animation(' 2. "What do you know about VISIOM?"')
            text_animation(' 3. "Why did you join AntiVisiom? "')
            if "none" in hero_suspicion:
                text_animation(' 4. "That\'s all, thanks."')
                selection = decision(4)
                if selection == 1:
                    text_animation('"Can you explain what’s your sixth sense?"')
                    text_animation('“It’s what Azriel said. I can feel the enemy approaching me. That’s all.')
                    text_animation('Don’t know how it works, but it works.” he said grumpily.\n')
                elif selection == 2:
                    text_animation('"What do you know about VISIOM?"')
                    text_animation('“I know what Azriel told me and you and that’s all I need,” he said in a cranky manner.\n')
                elif selection == 3:
                    text_animation('"Why did you join AntiVisiom? "')
                    text_animation('“Because I don’t like VISIOM. That’s all,” he said.\n')
                else:
                    text_animation('"That\'s all, thanks."')
                    asking_the_team()
            else:
                text_animation(' 4. "How did you join AntiVisiom?"')
                text_animation(' 5. "That\'s all, thanks."')
                selection = decision(5)
                if selection == 1:
                    text_animation('"Can you explain what’s your sixth sense?"')
                    text_animation('“It’s what Azriel said. I can feel the enemy approaching me. That’s all.')
                    text_animation('Don’t know how it works, but it works.” he said grumpily.\n')
                elif selection == 2:
                    text_animation('"What do you know about VISIOM?"')
                    text_animation('“I know what Azriel told me and you and that’s all I need,” he said in a cranky manner.\n')
                elif selection == 3:
                    text_animation('"Why did you join AntiVisiom? "')
                    text_animation('“Because I don’t like VISIOM. That’s all,” he said.\n')
                elif selection == 4:
                    text_animation('"How did you join AntiVisiom?"')
                    text_animation('He looked at you with an irritated face and said: “Why should I tell YOU??? Are YOU')
                    text_animation('a police officer or what?? You DON’T NEED to know that.”\n')
                    if "lux" in hero_suspicion:
                        hero_suspicion.remove("lux")
                else:
                    text_animation('"That\'s all, thanks."\n')
                    asking_the_team()

    elif member == "vega":
        text_animation('You came to Vega and she asked nervously: \n“Wh-What d-d-do you want to know?”')
        while True:
            text_animation(' 1. "Can you heal me properly if I am injured? You look nervous."')
            text_animation(' 2. "What do you know about VISIOM?"')
            text_animation(' 3. "Why did you join AntiVisiom? "')
            if "none" in hero_suspicion:
                text_animation(' 4. "That\'s all, thanks."')
                selection = decision(4)
                if selection == 1:
                    text_animation('"Can you heal me properly if I am injured? You look nervous."')
                    text_animation('“I-I-I CAN! I-I was a n-nurse. I-I am j-just a little n-n-nervous b-be-because')
                    text_animation('I am s-scared t-th-that V-VISIOM will f-find us. That’s all.” she said.\n')
                elif selection == 2:
                    text_animation('"What do you know about VISIOM?"')
                    text_animation('“J-ju-just that it c-controls everyone. VISIOM controls them with absolute power,”')
                    text_animation('she said but the last sentence didn’t sound quite natural.\n')
                elif selection == 3:
                    text_animation('"Why did you join AntiVisiom? "')
                    text_animation('“I-I just w-want to help people. I-I- became a nurse because I wanted to help people,” she said determinedly.\n')
                else:
                    text_animation('"That\'s all, thanks."')
                    asking_the_team()
            else:
                text_animation(' 4. "How did you join AntiVisiom?"')
                text_animation(' 5. "That\'s all, thanks."')
                selection = decision(5)
                if selection == 1:
                    text_animation('"Can you heal me properly if I am injured? You look nervous."')
                    text_animation('“I-I-I CAN! I-I was a n-nurse. I-I am j-just a little n-n-nervous b-be-because')
                    text_animation('I am s-scared t-th-that V-VISIOM will f-find us. That’s all.” she said.\n')
                elif selection == 2:
                    text_animation('"What do you know about VISIOM?"')
                    text_animation('“J-ju-just that it c-controls everyone. VISIOM controls them with absolute power,”')
                    text_animation('she said but the last sentence didn’t sound quite natural.\n')
                elif selection == 3:
                    text_animation('"Why did you join AntiVisiom? "')
                    text_animation('“I-I just w-want to help people. I-I- became a nurse because I wanted to help people,”')
                    text_animation('she said determinedly.\n')
                elif selection == 4:
                    text_animation('"How did you join AntiVisiom?"')
                    text_animation('“I-I-I don’t k-know. B-but Azriel told me t-that h-he helped me to escape VISIOM.')
                    text_animation('My chip was somehow damaged so that’s why,” she said.\n')
                    if "vega" in hero_suspicion:
                        hero_suspicion.remove("vega")
                    text_animation("‘Why did she stop stuttering in the middle of the sentence?’")
                else:
                    text_animation('"That\'s all, thanks."\n')
                    asking_the_team()

def who_ask():
    text_animation("Who do you want to talk to?")
    text_animation("\n 1. Talk to Sharla\n 2. Talk to Lux\n 3. Talk to Vega\n 4. That\'s all. Let\'s set off.")
    selection = decision(4)
    if selection == 1:
        member = "sharla"
        talk_w_team(member)
    elif selection == 2:
        member = "lux"
        talk_w_team(member)
    elif selection == 3:
        member = "vega"
        talk_w_team(member)
    else:
        intro_departure()

def asking_the_team():
    if "sharla" in hero_suspicion:
        who_ask()

    elif "lux" in hero_suspicion:
        who_ask()

    elif "vega" in hero_suspicion:
        who_ask()

    else:
        suspicion_level = is_list_empty(hero_suspicion)
        if suspicion_level is True:
            text_animation("'Their answers were strange. Sharlas and Vegas answer about how they joined AntiVisiom were connected with Azriel.'")
            text_animation("What will you do?")
            text_animation("\n 1. Will you still trust AntiVisiom and help them?\n 2. Will you not trust Azriel and his teammates and think of something else to do?")
            selection = decision(2)
            if selection == 1:
                printWdelay("You trust AntiVisiom.")
                intro_departure()
            else:
                betray_pt1()

        else:
            asking_the_team()
# END interview with teammates

# intro part
def intro():
    global character
    text_animation('\n“Thank you very much! You are truly our saviour! As promised, here is the enhancing scroll.')
    text_animation('It will enhance your stats and give you magic power.”')
    printWdelay("Azriel handed you the scroll. You open the scroll, and a bunch of weird symbols start pouring"
                "\nout of the scroll and wrapping around you.")

    time.sleep(time_delay)

    classData = crateClass()
    character = hero(classData[0], 100, classData[1], classData[2], classData[3], classData[4], classData[5], classData[6])
    current_stats()

    printWdelay("After that, the weird symbols disappeared.")
    printWdelay("\nAzriel looks satisfied.")
    text_animation('“You truly are The chosen one,” he said.')
    text_animation('“I feel stronger than I have ever been. And I can even use magic attacks.”')
    text_animation('“That’s great! We have prepared some equipment for you. We can’t give you')
    text_animation('anything high-tech, because VISIOM could discover you with it. Here...')
    text_animation('a sword that we have forged. It’s a long sword. And here’s a bow.')
    text_animation('We made those based on some preserved documentation.Try them.” Azriel said.')
    printWdelay("Azriel gave you the weapons. You tried swinging the sword a few times.")
    text_animation('“It\'s pretty good. Quite balanced. I wouldn’t know how to use a sword properly')
    text_animation('if the scroll didn’t teach me basic combat skills.”')
    text_animation('“Is that so? Well, I’m glad that you like it. What about the bow? You can try shooting')
    text_animation('at the tree there.” said Azriel and pointed at the nearby tree.')
    printWdelay("You fired a few times at a tree. Some shots missed but most of them landed on target.")
    text_animation('Azriel looked keen and said: “Wow. You’re so good. Did the scroll grant you those skills?')
    text_animation('It’s a pity that we couldn’t obtain those powers. But we didn’t prepare any staff for you.')
    text_animation('Can you use your magic even without a staff?”')
    text_animation("You heard The magic scroll’s voice inside your head saying:")
    text_animation("‘You can just fire magic from your hands.’")
    text_animation('“Yes, I can. I just need to concentrate and shoot from my hands.')
    text_animation('Thanks for the equipment but now to the important stuff. How can I defeat VISIOM?”')
    text_animation("“Right, first of all, as you know VISOM is a program. So you can’t defeat it directly.”")
    printWdelay("You looked at Azriel with a confused look. He understands what you’re going to say"
                "\nand answers it before you can ask.")
    text_animation("“You can’t defeat VISIOM DIRECTLY. You have to destroy its servers where VISIOM is hosted.")
    text_animation("There are in total 4 servers. Three of those are supporting servers and the last one")
    text_animation("is the main server. So you need to destroy them all.”")
    text_animation('\n 1. "Why can\'t I destroy only the main server?"\n 2. "..."')

    selection = decision(2)
    if selection == 1:
        text_animation('“Because VISIOM can restore itself from any of its supporting servers.')
        text_animation('You need to get rid of VISOM completely.”')

    text_animation("“We should destroy the supporting servers first because then it can’t restore itself.")
    text_animation("You can destroy VISIOM using this Wiping device to hack the server and delete VISIOM.")
    text_animation("It should be easy because the servers don’t have the highest security. After all,")
    text_animation("VISIOM thinks that it can control everyone.”")
    printWdelay("He gave you a Wiping device. It looks like a USB stick from your time.")
    text_animation("“VISIOM will notice that a server was destroyed so you should be more careful")
    text_animation("attacking the rest of the servers because there will definitely be more guards")
    text_animation("the more servers you destroy. Each of the supporting servers are on the")
    text_animation("east, south and west side. The main server is on the north.”")
    printWdelay("You think it doesn’t sound impossible but:")
    text_animation("“How can I find the way to the servers?”")
    text_animation("“Originally AntiVisiom had ten members but because we sacrificed six of our members")
    text_animation("only four members are left.” Azriel points at himself and three people standing nearby.")
    text_animation('“This is Sharla...” he pointed at a woman on the left and she waved back at you')
    text_animation('and said: “Hello, nice to meet you."')
    text_animation('“The one in the middle is Lux…” he points at a man in the middle. He looked at you and nodded.')
    text_animation('“And the woman on the right is Vega,” said Azriel. Your eyes met briefly')
    text_animation('but she turned away quickly. She looked a little nervous.')
    text_animation('“We’ll keep you company on your journey and show you how to get to the servers.')
    text_animation('Sharla is our navigator. She also knows the layout of the servers because she was')
    text_animation('taking care of them in the past. She’ll lead the way. Lux is quite special.')
    text_animation('He can predict incoming danger. It’s like he has a sixth sense. He’ll alert us')
    text_animation('if some enemy approaches us. Vega was a nurse so she could heal us if we were injured.')
    text_animation('Now should we get going or do you want to do something?"')
    text_animation('\n 1. "I want to meet the team and ask them a few questions."\n 2. "No, let’s set off right now!"')

    selection = decision(2)
    if selection == 1:
        asking_the_team()
    elif selection == 2:
        intro_departure()

def game_resume(server):
    global character
    current_stats()
    if server == "north":
        text_animation('“Let’s go to the main server.”\n')
        northern_pt1()
    elif server == "west":
        text_animation('"Let’s go to the western server."\n')
        western_pt1()
    elif server == "south":
        text_animation('"Let’s go to the southern server."\n')
        southern_pt1()
    elif server == "east":
        text_animation('"Let’s go to the eastern server."\n')
        eastern_pt1()
    else:
        departure()

def ask_animation():
    global developer
    global time_speech
    global time_medium
    global time_delay
    global time_slow
    if developer is True:
        text_animation("Would you like to play with animation (recommended) or without(testing)?")
        text_animation("\n 1. With animation\n 2. No animation")
        selection = decision(2)
        if selection == 2:
            time_speech = 0
            time_medium = 0
            time_slow = 0
            time_delay = 1

        else:
            time_speech = 0.06
            time_medium = 0.5
            time_slow = 2
            time_delay = 2.5


def play_from_saved():
    global character
    global unfinished_servers
    file_exists = os.path.isfile("savedserver.txt")
    if file_exists:
        file = open("savedserver.txt", "r")
        server = file.read()
        file.close()
        with open('savefiles.dat', 'rb') as f:
            character, unfinished_servers = pickle.load(f)
        rooms_north.clear()
        rooms_north.extend(["power", "entrance", "control"])
        ask_animation()
        text_animation("Loading last saved point.\n")
        game_resume(server)

    else:
        text_animation("No saved points. Start playing from start.")
        play()

def play():
    hero_suspicion.clear()
    unfinished_servers.clear()
    rooms_north.clear()
    hero_suspicion.extend(["none", "sharla", "lux", "vega"])
    unfinished_servers.extend(["east", "south", "west"])
    rooms_north.extend(["power", "entrance", "control"])
    ask_animation()
    start()

def start():
    text_animation("")
    print()
    print("######################################")
    print("#                                    #")
    print("#         The fall of VISIOM         #")
    print("#                                    #")
    print("######################################")
    print()
    print()

    text_animation(". . .")
    text_animation("‘Where am I...’")
    text_animation('“YES! Finally, we summoned The chosen one!”')
    text_animation("‘Someone is talking...’")
    text_animation('“You might be asking yourself where you are and how you got here. Let me answer')
    text_animation('those questions for you. Hi, I am Azriel and welcome to the year 3009! We summoned you')
    text_animation('from the past because we need your help! We as humans always wanted to innovate.')
    text_animation('But it was taken too far! At the beginning of the 2800s, scientists released VISIOM.')
    text_animation('VISIOM stands for Very Intelligent System Independent Of Man. It was a program that')
    text_animation('evolved on its own. VISIOM started to learn how to think like a living being.')
    text_animation('Not long after it obtained its own consciousness!!! Scientists intended to use VISIOM')
    text_animation('to help humanity but it decided to take over it! VISIOM can control everything!')
    text_animation('Weapons, transport, robots, just everything, even humans!')
    text_animation('How? From birth, everyone gets a chip implanted in them. With this chip, VISIOM')
    text_animation('can control them at its “will”. I am the leader of the group AntiVisiom. We were able')
    text_animation('to partly escape VISIOM control. But we cannot save the world because we would be')
    text_animation('discovered and removed right away. Only you don’t have the chip in you. You have to')
    text_animation('destroy VISIOM. We need you because if we come into the server the chip inside us would')
    text_animation('kill us in an instant. You’d ask ‘How can I destroy them?’. We found a scroll from')
    text_animation('ancient times that can enhance you and grant you magical powers. We tried to use it but')
    text_animation('the scroll always rejected us. It needs the chosen one to be able to use its powers.')
    text_animation('We also found a summoning scroll that requires sacrifices to summon The chosen one.')
    text_animation('It was our last option so we summoned you and here you are. We sacrificed six of our')
    text_animation('most devoted members.')
    text_animation('\nAre you willing to help us?"')
    text_animation("\n 1. Yes\n 2. ...yes\n 3. No")
    selection = decision(3)
    if selection == 1:
        text_animation('"Yes"')
        intro()
    elif selection == 2:
        hero_suspicion.remove("none")
        text_animation('"...yes"')
        text_animation("\n‘They seem a little suspicious but why not help them?")
        text_animation("I still should be wary about what they are doing.’")
        intro()
    elif selection == 3:
        text_animation('"No')
        text_animation("\n Maybe next time.")
        leave_game()
# END intro part

# starting menu
def how_to_play():
    text_animation("You play by entering numbers or words.\n")
    text_animation("When there’s something similar to this:\n 1. Choice 1\n 2. Choice 2\n 3. Choice 3")
    text_animation("Enter the number of the choice you want.\n")
    text_animation("You may also see something like this:")
    text_animation(" Choose between choice 1 (1) and choice 2 (2)...")
    text_animation("Enter the number in the brackets of the choice you want.\n")
    text_animation("When there’s something similar to this:\n Go forward (forward)\n Go left (left)\n Go right (right)")
    text_animation("Enter the word in brackets of the choice you want.\n")
    move = input("Press any key to back to the menu.")
    menu()

def explain_stats():
    text_animation("There are two types of statistics: yours and enemies statistics.\n")
    text_animation("Your statistics are health, attack, range, magic, luck and defence.")
    text_animation(" Health – your current health")
    text_animation(" Attack – damage dealt by your melee attack")
    text_animation(" Range – damage dealt by your ranged attack")
    text_animation(" Magic – damage dealt by your magic attack")
    text_animation(" Luck – your luck affects the chance of causing damage to the enemy, etc.")
    text_animation(" Defence – the damage gained is determined by the difference")
    text_animation("           between the defence and the value of the enemy's attack")
    text_animation("\nEnemies statistics are health, attack, special and chance.")
    text_animation(" Health – enemies current health")
    text_animation(" Attack – damage dealt by enemies normal attack")
    text_animation(" Special – damage dealt by enemies special attack")
    text_animation(" Chance – enemies chance determine if their attack lands on you\n")
    move = input("Press any key to back to the menu.")
    menu()

def menu():
    print()
    print("######################")
    print("#                    #")
    print("#        MENU        #")
    print("#                    #")
    print("######################")
    text_animation("\n 1. Play\n 2. Play from saved point\n 3. How to play\n 4. Explain statistics\n 5. Leave")
    selection = decision(5)
    if selection == 1:
        play()
    elif selection == 2:
        play_from_saved()
    elif selection == 3:
        how_to_play()
    elif selection == 4:
        explain_stats()
    else:
        text_animation("Maybe next time.")
        leave_game()
# END starting menu

text_animation("WELCOME PLAYER")
print()
menu()