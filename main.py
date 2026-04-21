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

name = input("Salutations brave adventurer! What do you call yourself in this fantastical world of ours? ")
weapon = ""
#Prompt for weapon of choice (sword, axe, or spear)
weapon_choice = input("So your name is Knight %s, huh? Shall you wield the valiant sword(1), the imposing axe(2), or the tactical spear?(3)" %name)
def choose_weapon(weapon_choice):
    match weapon_choice:
        case 1:
            print("You have chosen the valiant sword!")
            weapon = "sword"
        case 2:
            weapon = "axe"
            return "You have chosen the imposing axe!", weapon
        case 3:
            print()
            weapon = "spear"
            return "You have chosen the tactical spear!", weapon
        case _:
            weapon = "fists"
            return "You have chosen to use your bare fists! Since you have such an attitude!", weapon
#Give the lowdown on what the setting is like
player = {name, weapon}


#Have the player arrive at the dungeon's entrance after gathering supplies, accentuating how excited the knight is to explore the famed dungeon
#CHOICE 1 - Give them the choice to enter the dungeon, or decide just to straight up leave because the entrance looks really depressing compared to the poster advertising the dungeon
#Leaving the dungeon entrance ends the game anticlimactically.


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

#Player finds goblin who looks like hes dying of starvation. He makes a weak swing that pings off the player's armor harmlessly. The goblin thenn breaks down and starts crying. Out of pity, the player can: 
#1. PUt it out of its misery with a quick strike.
#2. Ask why it is in its current state. 

# If the player kills the goblin, they are none the wiser to the dungeon's plight and they decide to leave out of a newfound sadness. the game ends on a pretty depressing note.
# If the player asks the goblin why its cryinng, the goblin decides to vent its frustrations by explaining that the dungeon has basically gone bankutpt with a severe lack of fighting spirit to go around,
# so the player can then decide to somehow help the dungeon's inhabitants or let the dungeon die. 

# 