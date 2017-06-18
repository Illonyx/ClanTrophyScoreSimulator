import operator

class Player(object):
	def __init__(self, name, trophies, best):
		self.name=name
		self.trophies=trophies
		self.best=best

	def toString(self):
		return "Name :" + str(self.name) + " Trophies : " + str(self.trophies)

	def toStringBest(self):
		return "Name :" + str(self.name) + " Record : " + str(self.best)

class Clan:

	

	def __init__(self, defaultClan, overriddenClan, maxClanSize=50):
		self.defaultClan=defaultClan
		self.overriddenClan=overriddenClan
		self.maxClanSize=maxClanSize


	def resetChanges(self):
		self.overriddenClan=list(self.defaultClan)
		
	def returnResetValue(self, trophyValue):
		if trophyValue < 4000:
			return trophyValue
		elif trophyValue >= 4000 and trophyValue < 4900:
			return 4000
		elif trophyValue >= 4900:
			return 4300
		else:
			return 4600
	
	def resetTrophies(self):
		#Allows trophies to be reseted for all players
		for player in self.overriddenClan:
			player.trophies=self.returnResetValue(player.trophies)
			
	
		

	def printDefault(self):
		copy=list(self.overriddenClan)
		copy.sort(key=operator.attrgetter('trophies'), reverse=True)
		rank=0
		for player in copy:
			rank += 1
			print(str(rank) + ". " + player.toString())

	def printBest(self):
		copy=list(self.overriddenClan)
		copy.sort(key=operator.attrgetter('best'), reverse=True)
		rank=0
		for player in copy:
			rank += 1
			print(str(rank) + ". " + player.toStringBest())

	def addMember(self, player):
		if len(self.overriddenClan) == self.maxClanSize:
			self.overriddenClan.remove(self.overriddenClan[-1])
		self.overriddenClan.append(player)
		self.overriddenClan.sort(key = operator.attrgetter('trophies'), reverse=True)

	def findPlayer(self, playerName):
		for player in self.overriddenClan:
			if player.name == playerName:
				return player
		print("Player with following name has not been found ! :" + playerName)
		return None

	def updatePlayer(self,playerName, trophyValue):
		if self.findPlayer(playerName) != None:
			self.findPlayer(playerName).trophies=trophyValue
			self.overriddenClan.sort(key = operator.attrgetter('trophies'), reverse=True)


	def calculateClanScore(self, playersList, considerateOnlyBest=False):
		index=0
		score=0

		if considerateOnlyBest: 
			playersList=list(playersList)
			playersList.sort(key=operator.attrgetter('best'), reverse=True)


		for player in playersList:
			index += 1
			trophiesToConsider=player.trophies
			if considerateOnlyBest:
				trophiesToConsider=player.best

			if index >=1 and index <=10:
				score += 50/100*trophiesToConsider
			elif index >=11 and index <= 20:
				score += 25/100*trophiesToConsider
			elif index >=21 and index <= 30:
				score += 12/100*trophiesToConsider
			elif index >=31 and index <= 40:
				score += 10/100*trophiesToConsider
			elif index >=41 and index <= 50:
				score += 3/100*trophiesToConsider
			else:
				print("Should not be called")
		return score

	def calculateOverriddenClanScore(self, considerateOnlyBest=False):
		return self.calculateClanScore(self.overriddenClan, considerateOnlyBest)

	def calculateDefaultClanScore(self, considerateOnlyBest=False):
		return self.calculateClanScore(self.defaultClan, considerateOnlyBest)

	def calculateOffsetDefaultOverridden(self, considerateOnlyBest=False):
		return self.calculateOverriddenClanScore(considerateOnlyBest) - self.calculateDefaultClanScore(considerateOnlyBest)



