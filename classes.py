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


#####################################################


class Weapon:
	def __init__(self, damage, speed):
		self._DamageBoost = damage
		self._SpeedBoost = speed
	def returnDamageBoost(self):
		return self._DamageBoost
	def returnSpeedBoost(self):
		return self._SpeedBoost


class WizardStaff(Weapon):
	def __init__(self):
		super().__init__(4,1)

class Shield(Weapon):
	def __init__(self):
		super().__init__(2,2)

class Sword(Weapon):
	def __init__(self):
		super().__init__(5,2)

class Dagger(Weapon):
	def __init__(self):
		super().__init__(3,4)

class Bow(Weapon):
	def __init__(self):
		super().__init__(2,4)

class BattleAxe(Weapon):
	def __init__(self):
		super().__init__(4,1)

class Fire(Weapon):
	def __init__(self):
		super().__init__(random.randint(8,12),2)




#####################################################


class Player:

	def __init__(self, _class, weapon):
		self._damage = 0
		self._health = 0
		self._speed = 0
		self._heal = 0
		self._class = _class
		self._weapon = weapon
		self._race = ''

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


	def displayStats(self):
		print("\nCHOSEN STATS: ")
		print("Damage:",self._damage)
		print("Health:",self._health)
		print("Attacks per second:",self._speed)
		print("Heal:",self._heal)


#####################################################


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
		super().__init__(20,400,2)

class Orc(EnemyRace):
	def __init__(self):
		super().__init__(15,300,4)
	

#####################################################


class Enemy:

	def __init__(self):
		self._Attack = 0
		self._Health = 0
		self._Speed = 0
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

	def displayStats(self):
		print("\n")
		print("ENEMY STATS:")
		print("Race:",self._raceType)
		print("Weapon:",self._weaponType)

		print("Enemy Damage:",self._Attack)
		print("Enemy Health:",self._Health)
		print("Enemy Attack Speed:",self._Speed)


#####################################################

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

enemy = Enemy()
enemy.randomRace()
enemy.displayStats()
