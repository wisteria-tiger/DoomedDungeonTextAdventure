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

#Prompt for name


sword_flag = False
axe_flag = False
spear_flag = False
health = 3
potions = 3
#Prompt for weapon of choice (sword, axe, or spear)

#Give the lowdown on what the setting is like
#Have the player arrive at the dungeon's entrance after gathering supplies, accentuating how excited the knight is to explore the famed dungeon
#CHOICE 1 - Give them the choice to enter the dungeon, or decide just to straight up leave because the entrance looks really depressing compared to the poster advertising the dungeon
#Leaving the dungeon entrance ends the game anticlimactically.
print("After a long, arduous journey and a quick stop for potions, you have arrived at the entrance of the terrible Doom Dungeon. ")
name = input("You, a brave knight, seek to brave this legendary dungeon so that the name... uh... whats your name again?\n")
print("Right, right... So the name Knight %s will be known throughout the lands! However, upon closer inspection, it seems that time has not been kind to the once grand archway into the dungeon. In fact, it's rather depressing." %name)
dungeon_entrance_choice = input("While it was a very long, arduous journey, you could always find another, more exciting looking dungeon to spend your valuable time in. What say you, Knight %s?\nW TO ADVANCE   S TO ABANDON\n" %name)
print()
if dungeon_entrance_choice.upper() == "W":
    weapon_choice = int(input("Alrighy then, onward! In preparation for your adventure, you a draw a fierce weapon; shall you wield a sword(1), an axe(2), or a spear?(3): "))
    if weapon_choice == 1:
        print("You have drawn a valiant sword!")
        sword_flag = True
        health = 3
        potions = 2
    elif weapon_choice == 2:
        print("You have drawn a powerful axe!")
        axe_flag = True
        health = 4
        potions = 1
    elif weapon_choice == 3:
        print("You have drawn a keen spear!")
        spear_flag  = True
        health = 2
        potions = 4
else:
    print("Well, if that's what you want. Off to look for a different adventure you go...")
    raise SystemExit
player = {name, health, potions}

#------------------------
#PLAYER ENTERS THE DUNGEON
#------------------------
#The player chooses to enter the dungeon, further encouraging a sense of disappointment as they look upon the gray and sullen halls and rooms. They expected grand setpieces and ancient stages of battle, nothing like what they've seen before.

#The player finally stumbles upon an enemy, a shambling skeleton that, somehow, looks more withered than you thought bones could be. It stumbles towards the player.

#CHOICE 2 - Attack the skeleton OR walk past it (it's moving really slow)
#ATTACK: THe skeleton tumbles back on its butt... pelvic bone? It was a solid strike, but the skeleton struggles to right itself, a faint spark now in it's eye sockets. It attacks with more force this time, requiring a stronger strike to dispatch.
#AVOID: THe skeleton's jaw drops in shock at the player's audacity to walk past an "obvious" threat. However, it seems to crumble into a pile of bones in it's weak attempt to protest. 

#The player continues on, taking note of the encounter.

#----------------------
#PLAYER LEARNS OF THE DUNGEON'S PLIGHT
#----------------------

# Player finds goblin who looks like hes dying of starvation. He makes a weak swing that pings off the player's armor harmlessly. The goblin thenn breaks down and starts crying. Out of pity, the player can: 
# 1. Put it out of its misery with a quick strike.
# 2. Ask why it is in its current state. 

# If the player kills the goblin, they are none the wiser to the dungeon's plight and they decide to leave out of a newfound sadness. the game ends on a pretty depressing note.
# If the player asks the goblin why its crying, the goblin decides to vent its frustrations by explaining that the dungeon has basically gone bankutpt with a severe lack of fighting spirit to go around,
# so the player can then decide to somehow help the dungeon's inhabitants or let the dungeon die. 

#----------------------
#PLAYER SAVES/DOOMS THE DUNGEON
#----------------------

# if the player decides to help, they must fight every enemy on the way to the dungeon's treasure, saving the dungeon and gaining a prize for their work. They will then show off the prize to other adventurers, steering them towards the dungeon and revitalzing it for years to come
# They can also choose to avoid the enemies to try and get the treasure with little effort, the dungeon will still die in the process. 
# if the player decides to let the dungeon die, they must make their way out of the dungeon in one piece. In a last ditch effort, the dungeon rearranges itself and sets traps throughout its halls to try and force the player to provide fighting spirit.
# if the player dies while attempting to escape the dungeon, their soul is consumed, and the dungeon is revitalized for a few years before eventually falling into disarray, withering away for good.

# if the player makes it out of the dungeon, the dungeon will wither away as it was going to.