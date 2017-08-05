import operator
from clanIO import *

class Player(object):
	def __init__(self, name, trophies, best):
		self.name=name
		self.trophies=trophies
		self.best=best

	#Mapping in constructor
	def mappingIn(dic):
		name=dic["name"]
		trophies=dic["trophies"]
		if dic["best"] != None or dic["best"] < dic["trophies"]:
				print("Erreur de saisie pour le joueur : " + dic["name"])
				best=trophies
		else:
			best=dic["best"]
		return Player(name,trophies,best)

	def toString(self):
		return "Name :" + str(self.name) + " Trophies : " + str(self.trophies)

	def toStringBest(self):
		return "Name :" + str(self.name) + " Record : " + str(self.best)

class Clan:

	def __init__(self, clan, maxClanSize=50):
		self.clan=clan
		self.maxClanSize=maxClanSize

	def loadFromFile(path):
		clanPersistance=ClanPersistance(path)
		return Clan.mappingIn(clanPersistance.loadClan())
		
	#Mapping in constructor
	def mappingIn(listDic):
		players=[]
		for dic in listDic:
			player=Player.mappingIn(dic)
			players.append(player)
			players.sort(key = operator.attrgetter('trophies'), reverse=True)
		return Clan(players,50)

#---------------------------------------------	
#--- Clan general methods
#---------------------------------------------

	def returnResetValue(self, trophyValue):
		if trophyValue < 4000:
			return trophyValue
		elif trophyValue >= 4000 and trophyValue < 4900:
			return 4000
		elif trophyValue >= 4900:
			return 4300
		else:
			return 4600

	def calculateClanScore(self):
		index=0
		score=0

		for player in self.clan:
			index += 1
			trophiesToConsider=player.trophies

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
				11
		return score

#-------------------------------------------------------
#--- Player manipulation 
#-------------------------------------------------------
	def addMember(self, player):
		#50th is kicked?
		if len(self.clan) == self.maxClanSize:
			self.clan.remove(self.clan[-1])
		self.clan.append(player)
		self.clan.sort(key = operator.attrgetter('trophies'), reverse=True)

	def findPlayer(self, playerName):
		for player in self.clan:
			if player.name == playerName:
				return player
		print("Player with following name has not been found ! :" + playerName)
		return None

	def updatePlayerTrophies(self, playerName, trophyValue):
		foundPlayer = self.findPlayer(playerName)
		if foundPlayer != None:
			foundPlayer.trophies=trophyValue
			if trophyValue > foundPlayer.best: 
				foundPlayer.best=trophyValue
			self.clan.sort(key = operator.attrgetter('trophies'), reverse=True)

	#-----------------------------------------------------
	#--- Printers
	#-----------------------------------------------------

	def printDefault(self):
		copy=list(self.clan)
		copy.sort(key=operator.attrgetter('trophies'), reverse=True)
		rank=0
		for player in copy:
			rank += 1
			print(str(rank) + ". " + player.toString())

	def printBest(self):
		copy=list(self.clan)
		copy.sort(key=operator.attrgetter('best'), reverse=True)
		rank=0
		for player in copy:
			rank += 1
			print(str(rank) + ". " + player.toStringBest())

"""
class EditableClan(Clan):
def resetTrophies(self):
		#Allows trophies to be reseted for all players
		for player in self.overriddenClan:
			player.trophies=self.returnResetValue(player.trophies)
			
	"""
