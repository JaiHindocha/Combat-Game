import random
from getpass import getpass

class PlayerClass:
	def __init__(self, attack, health, heal):
		self._AttackIncrease = attack
		self._HealthIncrease = health
		self._HealIncrease = heal
		#self._Special = special
	def returnAttackIncrease(self):
		return self._AttackIncrease
	def returnHealthIncrease(self):
		return self._HealthIncrease
	def returnHealIncrease(self):
		return self._HealIncrease



class Wizard(PlayerClass):
	def __init__(self):
		super().__init__(10,100,30) #"Deflect Attack"

	def chooseWeapon(self):
		print("""
Weapons Available:

	1. Wizard Staff
	2. Shield
""")
		choice=input("Enter weapon 1 or 2: ")
		while choice not in ['1','2']:
			print("Please choose 1 or 2")
			choice=input("Enter weapon 1 or 2: ")
		if choice == '1':
			return WizardStaff(),"Wizard"
		else:
			return Shield(),"Shield"



class Warrior(PlayerClass):
	def __init__(self):
		super().__init__(14,25,20) #"Double Sword Attack"

	def chooseWeapon(self):
		print("""
Weapons Available:

	1. Sword
	2. Dagger
	3. Shield
""")
		choice=input("Enter weapon 1 or 2 or 3: ")
		while choice not in ['1','2','3']:
			print("Please choose 1 or 2 or 3")
			choice=input("Enter weapon 1 or 2 or 3: ")
		if choice == '1':
			return Sword(),"Sword"
		if choice == '2':
			return Dagger(),"Dagger"
		else:
			return Shield(),"Shield"



class Archer(PlayerClass):
	def __init__(self):
		super().__init__(6,25,15) #"Triple Arrow Shot"

	def chooseWeapon(self):
		print("""
Weapons Available:

	1. Dagger
	2. Bow and Arrow
""")
		choice=input("Enter weapon 1 or 2: ")
		while choice not in ['1','2','3']:
			print("Please choose 1 or 2")
			choice=input("Enter weapon 1 or 2: ")
		if choice == '1':
			return Dagger(),"Dagger"

		else:
			return Bow(),"Bow"



class PlayerRace:
	def __init__(self,attack,health,heal):
		self._Attack = attack
		self._Health = health
		self._Heal = heal
	def returnAttack(self):
		return self._Attack
	def returnHealth(self):
		return self._Health
	def returnHeal(self):
		return self._Heal


class Human(PlayerRace):
	def __init__(self):
		super().__init__(8,100,15)

class Elf(PlayerRace):
	def __init__(self):
		super().__init__(6,110,20)

class Giant(PlayerRace):
	def __init__(self):
		super().__init__(10,150,0)


class Weapon:
	def __init__(self, damage,block):
		self._DamageBoost = damage
		self._Block = block
	def returnDamageBoost(self):
		return self._DamageBoost
	def returnBlock(self):
		return self._Block


class WizardStaff(Weapon):
	def __init__(self):
		super().__init__(5,0)

class Shield(Weapon):
	def __init__(self):
		super().__init__(3,1)

class Sword(Weapon):
	def __init__(self):
		super().__init__(6,0)

class Dagger(Weapon):
	def __init__(self):
		super().__init__(4,0)

class Bow(Weapon):
	def __init__(self):
		super().__init__(3,0)


class Player:

	def __init__(self, _class, weapon):
		self._damage = 0
		self._health = 0
		self._heal = 0
		self._class = _class
		self._weapon = weapon
		self._race = ''
		self._block=0


	def chooseRace(self):
		print("""
Races:
	1. Human - [Damage: 8, Health: 100, Heal: 15]
	2. Elf - [Damage: 6, Health: 100, Heal: 20]
	3. Giant - [Damage: 10, Health: 150, Heal: 0]
""")
		choice = input("Choose a race: ")
		while choice not in ['1','2','3']:
			print("Invalid choice")
			choice = input("Choose an option: ")
		if choice == '1':
			self._race = Human()
		elif choice == '2':
			self._race = Elf()
		else:
			self._race = Giant()

		self._damage += self._race.returnAttack()
		self._health += self._race.returnHealth()
		self._heal += self._race.returnHeal()

	def classStats(self):
		self._damage += (self._class.returnAttackIncrease() + self._weapon.returnDamageBoost())
		self._health += self._class.returnHealthIncrease()
		self._heal += self._class.returnHealIncrease()
		self._block = self._weapon.returnBlock()

	def displayStats(self):
		print("Damage:",self._damage)
		print("Health:",self._health)
		print("Heal:",self._heal)

	def Turn(self):
		choice=getpass("Enter 'a' for attack, 'b' for block or 'h' for heal: ")
		while choice not in ['a','b','h']:
			choice=getpass("Enter 'a' for attack, 'b' for block or 'h' for heal: ")
		return choice

	def getHealth(self):
		return self._health
	def setHealth(self, health):
		self._health = health
	def getHeal(self):
		return self._heal
	def getAttack(self):
		return self._damage


def chooseClass():
		print("""
Races:
	1. Wizard - [Damage: 10, Health Boost: 100, Heal: 30]
	2. Warrior - [Damage: 14, Health Boost: 25, Heal: 20]
	3. Archer - [Damage: 6, Health Boost: 25, Heal: 10]
""")
		choice = input("Choose a class: ")
		while choice not in ['1','2','3']:
			print("Invalid choice")
			choice = input("Choose an option: ")
		if choice == '1':
			_class = Wizard()
			weapon,weaponType = _class.chooseWeapon()
		elif choice == '2':
			_class = Warrior()
			weapon,weaponType = _class.chooseWeapon()
		else:
			_class = Archer()
			weapon,weaponType = _class.chooseWeapon()

		return _class,weapon,weaponType


_class1,weapon1,weaponType1 = chooseClass()

user1 = Player(_class1,weapon1)
user1.chooseRace()
username1 = input("Enter a username: ")
while len(username1) < 3:
	username1 = input("Enter a longer username: ")
user1.classStats()
userAttack1 = user1.getAttack()
userHeal1 = user1.getHeal()


_class2,weapon2,weaponType2 = chooseClass()

user2 = Player(_class2,weapon2)
user2.chooseRace()
username2 = input("Enter a username: ")
while len(username2) < 3:
	username2 = input("Enter a longer username: ")
user2.classStats()
userAttack2 = user2.getAttack()
userHeal2 = user2.getHeal()

print("\n",username1,"STATS: ")
user1.displayStats()
print("\n",username2,"STATS: ")
user2.displayStats()


while user1.getHealth() > 0 and user2.getHealth() > 0:
	userTurn1 = user1.Turn()
	user1Health = user1.getHealth()
	userTurn2 = user2.Turn()
	user2Health = user2.getHealth()

	if userTurn1 == 'a':
		if userTurn2 == 'a':
			user2Health -= userAttack1
			user2.setHealth(user2Health)
			user1Health -= userAttack2
			user1.setHealth(user1Health)
			print("BOTH PLAYERS ATTACKED!")
			print(username2,'took',userAttack1,'damage')
			print(username1,"took",userAttack2,'damage')

		elif userTurn2 == 'b':
			user2Health -= 10
			user2.setHealth(user2Health)
			print(username1,'attacked but',username2,'blocked.')
			print(username2,"took 10 damage.")

		elif userTurn2 == 'h':
			user2Health -= userAttack1
			user2.setHealth(user2Health)
			print(username1, "ATTACKED!")
			print(username2,"took",userAttack1,"damage.")

	elif userTurn1 == 'b':
		if userTurn2 == 'a':
			user1Health -= 10
			user1.setHealth(user1Health)
			print(username2,'attacked but',username1,'blocked.')
			print(username1,"took 10 damage.")

		elif userTurn2 == 'h':
			user2Health += userHeal2
			user2.setHealth(user2Health)
			print(username2,'healed and',username1,'blocked.')

		elif userTurn2 == 'b':
			print("BOTH PLAYERS BLOCKED!")

	elif userTurn1 == 'h':
		if userTurn2 == 'a':
			user1Health -= userAttack2
			user1.setHealth(user1Health)
			print(username2,'attacked and',username1,'blocked.')
			print(username1,"took",userAttack2,'damage')

		elif userTurn2 == 'b':
			user1Health += userHeal1
			user1.setHealth(user1Health)
			print(username1,'healed and',username2,'blocked.')

		else:
			print("BOTH PLAYERS HEALED!")

	print("\n")
	if user1.getHealth() > 0 and user2.getHealth() > 0:
		print(username1,"health:",user1Health)
		print(username2,"health:",user2Health)
		print("\n")
	elif user1.getHealth() < 0 and user2.getHealth() < 0:
		print("YOU BOTH TIE!!!")
	elif user1.getHealth() > 0 and user2.getHealth() < 0:
		print(username1,"WINS!!!")
	else:
		print(username2,"WINS!!!")
