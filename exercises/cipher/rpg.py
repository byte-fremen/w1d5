

class Game:

    def __init__(self):
        self.player = Player()
        self.mission = Mission()

        self.actions_set = [eats_dinner, travel, attack, harm]
    


    def travel(self):
        player_choice = self.mission.first_task()
        if player_choice == 1:
        	health_change(1)
            
        elif player_choice == 2:
        	health_change(2)

        elif player_choice == 3:
        	health_change(4)



    def attack(self):
        player_choice = self.mission.first_task()
        if player_choice == 1:
        	health_change(-2)
            
        elif player_choice == 2:
            health_change(-4)
            
        elif player_choice == 3:
        	health_change(-1)

    def harm(self, self.health_change):
        self.health += health_change
        return "You've been harmed. Deduction of %d" % (health_change)


    # def inventory(self):
    #     self.player.view_inventory()


class Player:

    def __init__(self):
        self.name = self.get_name()

    def get_name(self):
        name = input("Hello Adventurer what is your name? (John, Paul, Ringo, George)")
        return name

    def get_race(self):
    	race = input("What is your character's race? (hobbit, unicorn, leprechaun)")
    	return race

class Character:
	def __init__(self,name, race, health, stats, weapon):
		self.name = name
		self.health = health
		self.stats = stats


class Hobbit(Character):
	def __init__(self,name, race, health, stats, weapon):
		self.name = name
		self.health = health
		self.stats = stats
		self.weapon = 'slingshot'


class Unicorn(Character):
	def __init__(self,name, race, health, stats, weapon):
		self.name = name
		self.health = health
		self.stats = stats
		self.weapon = 'bow and arrow'

class Leprechaun(Character):
	def __init__(self,name, race, health, stats, weapon):
		self.name = name
		self.health = health
		self.stats = stats
		self.stats = 'butter knife'


class Activity:


    def travel(self):
        option = input("""
            [1] sees a foreign film
            [2] a disco
            [3] the bingo hall
            """)
        if option != integer:
            self.travel
        else:
            return option

    def attack(self):
        option = input("""
            [1] stabbed by a priest
            [2] shot by a mobster
            [3] slimed by a ghost
            """)
        if option != integer:
            self.attack
        else:
            return option


    def harm(self):
        option = input("""
            [1] crushed
            [2] mauled
            [3] spat upon
            """)
        if option != integer:
            self.harm
        else:
            return option


game = Game()
game.start()