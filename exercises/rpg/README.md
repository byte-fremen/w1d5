# Command Line RPG

* This weekend you will be building your first ever command line application. 
* A text based rpg adventure
* You will be taking user input and using it throughout the game. 
* Utilize Classes and Methods to instantiate objects necessary for the game. 
* Some example classes may be:
	* `User` or `Player`
	* `Monsters`
		* child classes of `Goblin`, `Ogre`, `Dragon`
	* `Places of Travel`
* Checkout the `example_rpg.py` file in the root of this repository for an example, if you want.
* Below is an example of what the terminal interface can look like. 


```
Hello Beautiful Person. What is your name?

>>> Jason

Welcome Jason. Would you like begin your adventure? (yes or no)

>>> yes

What is your character name?

>>> Drizzt 

What is your characters gender?

>>> Male

What is your characters race?

>>> Dark Elf

Drizzt, you are currently in the City of New York. A townsman approaches you and tells you to please save his son who was kidnapped by a group of goblins nearby. He will give you 50 gold. Do you accept this quest? (yes or no)

>>> yes

You approach a small camp 5 miles east of the village, during your scouting a goblin attacks you from behind
You take 3 damange. 
What do you do? (attack or run)

>>> attack

You miss the goblin
Goblin attacks you 
Goblin misses
What do you do? (attack or run)

>>> run
```

#### Starting This App

* The above is just an example. You can take this game as far as you want. 
* Make sure you PSEUDO CODE
* Write down user stories before writing any actual code
* User stories will look something like

```
User will be able to declare a character
User character will have a name, race, health, stats, weapon
User will be able to travel to an area
User will be able to attack a monster
User will be able to take damage from a monster
```


#### Example from class

```
class Game:

    def __init__(self):
        self.player = Player()
        self.mission = Mission()
    
    def start(self):
        player_choice = self.mission.first_task()
        if player_choice == 1:
            # Run this function
        elif player_choice == 2:
            # Do this function

    def blah(self):
        self.player.view_inventory()


class Player:

    def __init__(self):
        self.name = self.get_name()

    def get_name(self):
        name = input("Hello Adventurer what is your name")
        return name

    def view_inventory(self):
        print("this is what you have in your inventory")

class Mission:

    def first_task(self):
        option = input("""
            [1] Go to the forest
            [2] Go to the village
            [3] Go to the castle
            """)
        if option != integer:
            self.first_task
        else:
            return option

game = Game()
game.start()
```



