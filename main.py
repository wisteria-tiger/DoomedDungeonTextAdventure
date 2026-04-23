#-----------------DOOMED DUNGEON-----------------
#Set in a relatively generic fantasy world, with knights, wizards, dwarves, skeletons, slimes, dragons - and dungeons, of course.
#You play as a knight who ventures off to fight through a legendary dungeon with promise of great treasures. 
#However, you find that the dungeon is, for lack of a better term, incredibly lame. 
#After fighting a couple of skeletons, you stumble upon a goblin that barely puts up a fight, instead asking for your critique
#on how to return the dungeon back to its former glory. Apparently, the dungeon's conditions have been declining over time
#due to newer more trendy dungeons popping up in foreign lands, stealing would-be adventurers from this one. Dungeons feed on the 
#fighting spirit of the adventurers that brave them, so the lack of adventurers means that the dungeon's inhabitants have been 
#weakening until eventually, they'll wither away to nothing. As a virtuous knight (or not, depends on you), you can't help but assist
#a creature in desperate need. So how will you go about saving this doomed dungeon?
#------------------------------------------------

#-----------------------
#PLAYER SETUP AND WORLD INTRODUCTION
#-----------------------

import random
dungeon_is_doomed = False
health = 3
potions = 3
fighting_spirt = 0
def fight_goblin():
    enemy_health = 3
    global health
    global potions
    print("A battle with the goblin commences!")
    while enemy_health > 1:
        action = input("W TO ATTACK  S TO HEAL\nENTER: ")
        if action.upper() == "W":
            print("You attack the goblin your %s!" %weapon)
            enemy_health -= 1
            print("It loses 1 health!")
        elif action.upper() == "S" and potions > 0:
            print("You decide to heal with a potion.\n HEALTH = %d, POTIONS = %d" %(health, potions))
            health += 1
            potions -= 1
        elif action.upper() == "S"  and potions == 0:
            print("You don't have any more potions!")
        else:
            print("You do nothing, for some reason...")

        if random.random() < 0.50:
            print("The goblin swings its club!")
            
            health -= 1
            print("You lost 1 health! HEALTH = %d" %health)
            if  health == 0:
                print("You took one hit too many! Game over...")
                raise SystemExit
        else:
            print("The goblin grunts, as if annoyed that it has to deal with you. Quite rude.")

def fight_skeleton():
    enemy_health = 4
    global health
    global potions
    print("A battle with the skeleton commences!")
    while enemy_health > 0:
        action = input("W TO ATTACK  S TO HEAL\nENTER: ")
        if action.upper() == "W":
            print("You attack the skeleton your %s!" %weapon)
            enemy_health -= 1
            print("It loses 1 health!")
        elif action.upper() == "S" and potions > 0:
            print("You decide to heal with a potion.\n HEALTH = %d, POTIONS = %d" %(health, potions))
            health += 1
            potions -= 1
        elif action.upper() == "S"  and potions == 0:
            print("You don't have any more potions!")
        else:
            print("You do nothing, for some reason...")

        if random.random() < 0.50:
            print("The skeleton slashes with a broken blade!")
            
            print("You lost 1 health! HEALTH = %d" %health)
            health -= 1
            if  health == 0:
                print("You took one hit too many! Game over...")
                raise SystemExit
        else:
            print("The skeleton's bones rattle, as if raring to strike again! Quite boisterous of a bag of bones!")

    print("You defeated the skeleton! You watch as it fades into a mysterious flame that imbues itself into the dungeon. The dungeon rumbles, as if reawakening from slumber. A few potions appear in you hand, as if the dungeon is thanking you for your trouble.")
    potions += 2
    print("YOU NOW HAVE %d POTIONS!" %potions)

def fight_slime():
    enemy_health = 4
    global health
    global potions
    print("A battle with the slime commences!")
    while enemy_health > 0:
        action = input("W TO ATTACK  S TO HEAL\nENTER: ")
        if action.upper() == "W":
            print("You attack the slime your %s!" %weapon)
            enemy_health -= 1
            print("It loses 1 health!")
        elif action.upper() == "S" and potions > 0:
            print("You decide to heal with a potion.\n HEALTH = %d, POTIONS = %d" %(health, potions))
            health += 1
            potions -= 1
        elif action.upper() == "S"  and potions == 0:
            print("You don't have any more potions!")
        else:
            print("You do nothing, for some reason...")

        if random.random() < 0.50:
            print("The skeleton slashes with a broken blade!")
            
            print("You lost 1 health! HEALTH = %d" %health)
            health -= 1
            if  health == 0:
                print("You took one hit too many! Game over...")
                raise SystemExit
        else:
            print("The skeleton's bones rattle, as if raring to strike again! Quite boisterous of a bag of bones!")

    print("You defeated the skeleton! You watch as it fades into a mysterious flame that imbues itself into the dungeon. The dungeon rumbles, as if reawakening from slumber. A few potions appear in you hand, as if the dungeon is thanking you for your trouble.")
    potions += 2
    print("YOU NOW HAVE %d POTIONS!" %potions)
#Prompt for weapon of choice (sword, axe, or spear)

#Give the lowdown on what the setting is like
#Have the player arrive at the dungeon's entrance after gathering supplies, accentuating how excited the knight is to explore the famed dungeon
#CHOICE 1 - Give them the choice to enter the dungeon, or decide just to straight up leave because the entrance looks really depressing compared to the poster advertising the dungeon
#Leaving the dungeon entrance ends the game anticlimactically.
print("After a long, arduous journey and a quick stop for potions, you have arrived at the entrance of the terrible Doom Dungeon. ")
name = input("You, a brave knight, seek to brave this legendary dungeon so that the name... uh... whats your name again?\nENTER: ")
print("Right, right... So the name Knight %s will be known throughout the lands! However, upon closer inspection, it seems that time has not been kind to the once grand archway into the dungeon. In fact, it's rather depressing." %name)
dungeon_entrance_choice = input("While it was a very long, arduous journey, you could always find another, more exciting looking dungeon to spend your valuable time in. What say you, Knight %s?\nW TO ADVANCE   S TO ABANDON\nENTER: " %name)
print()
if dungeon_entrance_choice.upper() == "W":
    weapon_choice = int(input("Alrighy then, onward! In preparation for your adventure, you a draw a fierce weapon; shall you wield a sword(1), an axe(2), or a spear?(3)\nENTER: "))
    if weapon_choice == 1:
        print("You have drawn a valiant sword!")
        weapon = "sword"
        health = 3
        potions = 2
    elif weapon_choice == 2:
        print("You have drawn a powerful axe!")
        weapon = "axe"
        health = 4
        potions = 1
    elif weapon_choice == 3:
        print("You have drawn a keen spear!")
        weapon = "spear"
        health = 2
        potions = 4
else:
    print("Well, if that's what you want. Off to look for a different adventure you go...")
    raise SystemExit
player = {name, weapon, health, potions}

#------------------------
#PLAYER ENTERS THE DUNGEON
#------------------------
#The player chooses to enter the dungeon, further encouraging a sense of disappointment as they look upon the gray and sullen halls and rooms. They expected grand setpieces and ancient stages of battle, nothing like what they've seen before.
print("With your weapon at the ready, you press forward into the dungeon. Legends tell of the grand gold pillars and ceilings of emerald that watched great battles rage within the dungeon. Despite the initial look of the entrance, you can't help but retain some hope for whats ahead.")
print("As you get enter, however, the halls and ceilings reveal themselves to be... blank, gray stone. The only variation is the occasional mazelike intersection. There's nothing imposing about the dungeon from what you've seen, not even a dank odor. It's awfully boring. \nYou continue on, searching for any sign of an enemy to fight.")

#----------------------
#PLAYER LEARNS OF THE DUNGEON'S PLIGHT
#----------------------

# Player finds goblin who looks like hes dying of starvation. He makes a weak swing that pings off the player's armor harmlessly. The goblin thenn breaks down and starts crying. Out of pity, the player can: 
# 1. Put it out of its misery with a quick strike.
# 2. Ask why it is in its current state. 
goblin_choice = input("Finally, after hours of searching, you stumble upon a terrifying goblin - is what I'd like to tell you, but it looks rather worse for wear, with sunken cheeks and bloodshot eyes. \nWill you fight it, or... inquire about its sorry state, Knight %s?\nW TO FIGHT  S TO INQUIRE\nENTER: " %name) 
if goblin_choice.upper() == "W":
    fight_goblin()
    print("You have the goblin on the ropes! It drops its club, raising its hands as if to begging for mercy. Shall you spare it, or finish it off?")
    decision = input ("W TO KILL  S TO SPARE\nENTER: ")
    if decision.upper() == "W":
        print("The goblin perishes at your hand. You decide to leave, cutting your losses with this doomed dungeon after defeating such a sad creature.")
        raise SystemExit
    else:
        print("The goblin looks up, its face looking revitalized from the battle.")
        print("It thanks you for the combat, and explains that the dungeon has lost its former glory due to a lack of adventurers such as yourself providing the dungeon with their fighting spirit.")
        save_or_doom_choice = input("He explains that you must battle the rest of the monsters and claim the dungeon's treasure to help restore it to its former glory. Shall you take on this burden, or cut your losses and escape, dooming the dungeon?\nW TO SAVE  S TO DOOM\nENTER: ")
        if save_or_doom_choice.upper() == "W":
            print("You have chosen to save the dungeon! You forge a path onward in search for more enemies to battle!")
        else:
            dungeon_is_doomed = True
            print("You have chosen to flee this disappointing dungeon! However, a strange and ominous rumbling occurs, and you sense a shift in the dungeon's layout. It seems the dungeon itself won't let you leave without a fight.")
else:
    print("The goblin is surpised by your kindess, and decides to confide in you about the dungeon's plight.")
    print("He explains that you must battle the rest of the monsters and claim the dungeon's treasure to help restore it to its former glory. Shall you take on this burden, or cut your losses and escape the dungeon?")
    save_or_doom_choice = input("He explains that you must battle the rest of the monsters and claim the dungeon's treasure to help restore it to its former glory. Shall you take on this burden, or cut your losses and escape, dooming the dungeon?\nW TO SAVE  S TO DOOM\nENTER: ")
    if save_or_doom_choice.upper() == "W":
        print("You have chosen to save the dungeon! You forge a path onward in search for more enemies to battle!")
        print("The goblin grants you a couple potions for your help!")
        potions += 2
        print("YOU NOW HAVE %d POTIONS!" %potions)
    else:
        dungeon_is_doomed = True
        print("You have chosen to flee this disappointing dungeon! However, a strange and ominous rumbling occurs, and you sense a shift in the dungeon's layout. It seems the dungeon itself won't let you leave without a fight.")

if dungeon_is_doomed == False:
    print("After marching forward with new resolve, you come upon a skeleton, fire in its eye sockets. It seems that the dungeon has seen fit to give you a fierce opponent in response to your quest to save it. Finally, some excitement!")
    fight_skeleton()
# If the player kills the goblin, they are none the wiser to the dungeon's plight and they continue through the dungeon, but they do not know how to save the dungeon.
# If the player asks the goblin why its crying, the goblin decides to vent its frustrations by explaining that the dungeon has basically gone bankutpt with a severe lack of fighting spirit to go around,
# so the player can then decide to somehow help the dungeon's inhabitants or let the dungeon die. 
#The player finally stumbles upon an enemy, a shambling skeleton that, somehow, looks more withered than you thought bones could be. It stumbles towards the player.

#CHOICE 2 - Attack the skeleton OR walk past it (it's moving really slow)

#ATTACK: THe skeleton tumbles back on its butt... pelvic bone? It was a solid strike, but the skeleton struggles to right itself, a faint spark now in it's eye sockets. It attacks with more force this time, requiring a stronger strike to dispatch.
#AVOID: THe skeleton's jaw drops in shock at the player's audacity to walk past an "obvious" threat. However, it seems to crumble into a pile of bones in it's weak attempt to protest. 

#The player continues on, taking note of the encounter.



#----------------------
#PLAYER SAVES/DOOMS THE DUNGEON
#----------------------

# if the player decides to help, they must fight every enemy on the way to the dungeon's treasure, saving the dungeon and gaining a prize for their work. They will then show off the prize to other adventurers, steering them towards the dungeon and revitalzing it for years to come
# They can also choose to avoid the enemies to try and get the treasure with little effort, the dungeon will still die in the process. 
# if the player decides to let the dungeon die, they must make their way out of the dungeon in one piece. In a last ditch effort, the dungeon rearranges itself and sets traps throughout its halls to try and force the player to provide fighting spirit.
# if the player dies while attempting to escape the dungeon, their soul is consumed, and the dungeon is revitalized for a few years before eventually falling into disarray, withering away for good.

# if the player makes it out of the dungeon, the dungeon will wither away as it was going to.