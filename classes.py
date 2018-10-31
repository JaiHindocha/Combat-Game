import random

class PlayerClass:
	def __init__(self, attack, speed, health, heal):
		self._AttackIncrease = attack
		self._SpeedIncrease = speed
		self._HealthIncrease = health
		self._HealIncrease = heal
		#self._Special = special
		#self._backup = 'punch'
	def returnAttackIncrease(self):
		return self._AttackIncrease
	def returnSpeedIncrease(self):
		return self._SpeedIncrease
	def returnHealthIncrease(self):
		return self._HealthIncrease
	def returnHealIncrease(self):
		return self._HealIncrease



class Wizard(PlayerClass):
	def __init__(self):
		super().__init__(8,0,100,30) #"Deflect Attack"

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
			return WizardStaff()
		else:
			return Shield()



class Warrior(PlayerClass):
	def __init__(self):
		super().__init__(12,2,25,20) #"Double Sword Attack"

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
			return Sword()
		if choice == '2':
			return Dagger()
		else:
			return Shield()



class Archer(PlayerClass):
	def __init__(self):
		super().__init__(4,3,25,15) #"Triple Arrow Shot"

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
			return Dagger()
		else:
			return Bow()


#####################################################



class PlayerRace:
	def __init__(self,attack,speed,health,heal):
		self._Attack = attack
		self._Speed = speed
		self._Health = health
		self._Heal = heal
	def returnAttack(self):
		return self._Attack
	def returnHealth(self):
		return self._Health
	def returnSpeed(self):
		return self._Speed
	def returnHeal(self):
		return self._Heal


class Human(PlayerRace):
	def __init__(self):
		super().__init__(6,2,100,5)

class Elf(PlayerRace):
	def __init__(self):
		super().__init__(4,3,100,10)

class Giant(PlayerRace):
	def __init__(self):
		super().__init__(8,0,150,0)


class Weapon:
	def __init__(self, damage, speed,block):
		self._DamageBoost = damage
		self._SpeedBoost = speed
		self._Block = block
	def returnDamageBoost(self):
		return self._DamageBoost
	def returnSpeedBoost(self):
		return self._SpeedBoost
	def returnBlock(self):
		return self._Block


class WizardStaff(Weapon):
	def __init__(self):
		super().__init__(4,1,0)

class Shield(Weapon):
	def __init__(self):
		super().__init__(2,2,1)

class Sword(Weapon):
	def __init__(self):
		super().__init__(5,2,0)

class Dagger(Weapon):
	def __init__(self):
		super().__init__(3,4,0)

class Bow(Weapon):
	def __init__(self):
		super().__init__(2,4,0)

class BattleAxe(Weapon):
	def __init__(self):
		super().__init__(4,1,0)

class Fire(Weapon):
	def __init__(self):
		super().__init__(random.randint(6,10),1,0)


class Player:

	def __init__(self, _class, weapon):
		self._damage = 0
		self._health = 0
		self._speed = 0
		self._heal = 0
		self._class = _class
		self._weapon = weapon
		self._race = ''
		self._block=0

	def chooseRace(self):
		print("""
Races:
	1. Human - [Damage: 6, Player Attack Speed: 2, Health: 100, Heal: 5]
	2. Elf - [Damage: 4, Player Attack Speed: 3, Health: 100, Heal: 10]
	3. Giant - [Damage: 8, Player Attack Speed: 0, Health: 150, Heal: 0]
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
		self._speed += self._race.returnSpeed()
		self._heal += self._race.returnHeal()

	def classStats(self):
		self._damage += (self._class.returnAttackIncrease() + self._weapon.returnDamageBoost())
		self._health += self._class.returnHealthIncrease()
		self._speed += (self._class.returnSpeedIncrease() + self._weapon.returnSpeedBoost())
		self._heal += self._class.returnHealIncrease()
		self._block = self._weapon.returnBlock()

	def displayStats(self):
		print("\nCHOSEN STATS: ")
		print("Damage:",self._damage)
		print("Health:",self._health)
		print("Attacks per second:",self._speed)
		print("Heal:",self._heal)

	def Turn(self):
		choice=input("Enter 'a' for attack, 'b' for block or 'h' for heal: ")
		while choice not in ['a','b','h']:
			choice=input("Enter 'a' for attack, 'b' for block or 'h' for heal: ")
		return choice

	def getHealth(self):
		return self._health
	def setHealth(self, health):
		self._health = health
	def getSpeed(self):
		return self._speed
	def getHeal(self):
		return self._heal
	def getAttack(self):
		return self._damage



class EnemyRace:
	def __init__(self,attack,health,speed):
		self._Attack = attack
		self._Health = health
		self._Speed = speed
	def returnAttack(self):
		return self._Attack
	def returnHealth(self):
		return self._Health
	def returnSpeed(self):
		return self._Speed

class Dragon(EnemyRace):
	def __init__(self):
		super().__init__(10,400,2)

class Orc(EnemyRace):
	def __init__(self):
		super().__init__(7,300,4)



class Enemy:

	def __init__(self):
		self._Attack = 0
		self._Health = 0
		self._Speed = 0
		self._Block = 0
		self._weaponType = ''
		self._raceType = ''
		self._weapon = ''

	def randomRace(self):
		choice = random.randint(1,3)
		if choice == 1:
			self._race = Dragon()
			self._raceType = "Dragon"
			self._weapon = Fire()
			self._weaponType = 'Fire'
		else:
			self._race = Orc()
			self._raceType="Orc"
			choice = random.randint(2,7)
			if choice == 2:
				self._weapon = Shield()
				self._weaponType = "Shield"

			elif choice == 3:
				self._weapon = Sword()
				self._weaponType = "Sword"

			elif choice == 4:
				self._weapon = Dagger()
				self._weaponType = "Dagger"

			elif choice == 5:
				self._weapon = Bow()
				self._weaponType = "Bow and Arrow"

			else:
				self._weapon = BattleAxe()
				self._weaponType = "Battle Axe"


		self._Attack += (self._race.returnAttack() + self._weapon.returnDamageBoost())
		self._Health += self._race.returnHealth()
		self._Speed += (self._race.returnSpeed() + self._weapon.returnSpeedBoost())
		self._Block += self._weapon.returnBlock()

	def displayStats(self):
		print("\n")
		print("ENEMY STATS:")
		print("Race:",self._raceType)
		print("Weapon:",self._weaponType)
		print("Enemy Damage:",self._Attack)
		print("Enemy Health:",self._Health)
		print("Enemy Attack Speed:",self._Speed)

	def Turn(self):
		turn = random.choice(['a','b'])
		return turn

	def getHealth(self):
		return self._Health

	def setHealth(self,newHealth):
		self._Health = newHealth

	def getAttack(self):
		return self._Attack

	def getSpeed(self):
		return self._Speed


def chooseClass():
		print("""
Races:
	1. Wizard - [Damage: 8, Speed Boost: 0, Health Boost: 100, Heal: 30]
	2. Warrior - [Damage: 12, Speed Boost: 2, Health Boost: 25, Heal: 20]
	3. Archer - [Damage: 3, Speed Boost: 3, Health Boost: 25, Heal: 10]
""")
		choice = input("Choose a class: ")
		while choice not in ['1','2','3']:
			print("Invalid choice")
			choice = input("Choose an option: ")
		if choice == '1':
			_class = Wizard()
			weapon = _class.chooseWeapon()
		elif choice == '2':
			_class = Warrior()
			weapon = _class.chooseWeapon()
		else:
			_class = Archer()
			weapon = _class.chooseWeapon()

		return _class,weapon


_class,weapon = chooseClass()

user = Player(_class,weapon)
user.chooseRace()
user.classStats()
user.displayStats()
userAttack = user.getAttack()
userSpeed = user.getSpeed()
userHeal = user.getHeal()

enemy = Enemy()
enemy.randomRace()
enemy.displayStats()
enemyAttack = enemy.getAttack()
enemySpeed = enemy.getSpeed()

def combat():
	while user.getHealth() > 0 and enemy.getHealth() > 0:
		enemyTurn = enemy.Turn()
		enemyHealth = enemy.getHealth()
		userTurn = user.Turn()
		userHealth = user.getHealth()

		if enemyTurn == 'a' and userTurn == 'a':
			enemyHealth -= userAttack * userSpeed
			enemy.setHealth(enemyHealth)
			userHealth -= enemyAttack * enemySpeed
			user.setHealth(userHealth)
			print("THE ENEMY ATTACKED!")
			print("You took",enemyAttack * enemySpeed,'damage')
			print("The enemy took",userAttack * userSpeed,'damage')

		elif enemyTurn == 'a' and userTurn == 'b':
			userHealth -= 10
			user.setHealth(userHealth)
			print("THE ENEMY ATTACKED!")
			print("You took 10 damage")

		elif enemyTurn == 'a' and userTurn == 'h':
			userHealth -= enemyAttack * enemySpeed
			user.setHealth(userHealth)
			print("THE ENEMY ATTACKED!")
			print("You took",enemyAttack * enemySpeed,'damage')
			print("The enemy took 0 damage")

		elif enemyTurn == 'b' and userTurn == 'a':
			enemyHealth -= 10
			enemy.setHealth(enemyHealth)
			print("THE ENEMY BLOCKED!")
			print("You took 0 damage")
			print("The enemy took 10 damage")

		elif enemyTurn == 'b' and userTurn == 'h':
			userHealth += userHeal
			user.setHealth(userHealth)
			print("THE ENEMY BLOCKED!")
			print("You gained",userHeal,"health")
		else:
			print("YOU AND THE ENEMY BOTH BLOCKED!")

		print("\n")
		if user.getHealth() > 0 and enemy.getHealth() > 0:
			print("Your health:",userHealth)
			print("Enemy health:",enemyHealth)
			print("\n")
		elif user.getHealth() < 0 and enemy.getHealth() < 0:
			print("YOU BOTH TIE!!!")
		elif user.getHealth() > 0 and enemy.getHealth() < 0:
			print("YOU WIN!!!")
		else:
			print("YOU LOSE!!!")
