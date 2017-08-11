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
		if dic["best"] == None or dic["best"] < dic["trophies"]:
				print("Erreur de saisie pour le joueur : " + dic["name"])
				best=trophies
		else:
			best=dic["best"]
		return Player(name,trophies,best)

	def mappingOut(player):
		dicToReturn={}
		dicToReturn["name"]=player.name
		dicToReturn["trophies"]=player.trophies
		dicToReturn["best"]=player.best
		return dicToReturn

	def toString(self):
		return "Name :" + str(self.name) + " Trophies : " + str(self.trophies)

	def toStringBest(self):
		return "Name :" + str(self.name) + " Record : " + str(self.best)

class Clan(object):

	def __init__(self, name, idC, editionDate, additionalInfo, members, maxClanSize=50):
		self.name=name
		self.id=idC
		self.editionDate=editionDate
		self.additionalInfo=additionalInfo
		self.members=members
		self.maxClanSize=maxClanSize


	def loadFromFile(path):
		clanPersistance=ClanPersistance(path)
		return Clan.mappingIn(clanPersistance.loadClan())

	def saveToFile(path, clan):
		clanPersistance=ClanPersistance(path)
		clanPersistance.saveClan(Clan.mappingOut(clan))

		
		
	#Mapping in constructor
	def mappingIn(jsonString):
		clanName=jsonString["name"]
		clanEditionDate=jsonString["editionDate"]
		clanId=jsonString["id"]
		clanAdditionalInfo=jsonString["additionalInfo"]

		players=[]
		for dic in jsonString["members"]:
			player=Player.mappingIn(dic)
			players.append(player)
			players.sort(key = operator.attrgetter('trophies'), reverse=True)
		return Clan(clanName, clanId, clanEditionDate, clanAdditionalInfo, players)

	#Mapping out constructor
	def mappingOut(clan):
		dicToReturn = {}
		dicToReturn["name"]=clan.name
		dicToReturn["id"]=clan.id
		dicToReturn["editionDate"]=clan.editionDate
		dicToReturn["additionalInfo"]=clan.additionalInfo

		#manage members
		members=[]
		for member in clan.members:
			memberDic=Player.mappingOut(member)
			members.append(memberDic)

		dicToReturn["members"]=members

		return dicToReturn



		return dicsToReturn


#---------------------------------------------	
#--- Clan general methods
#---------------------------------------------

	def returnResetValue(trophyValue):
		if trophyValue >= 0 and trophyValue < 4000:
			return trophyValue
		elif trophyValue >= 4000 and trophyValue < 4900:
			return 4000
		elif trophyValue >= 4900 and trophyValue < 5800:
			return 4300
		elif trophyValue >= 5800 and trophyValue < 6700:
			return 4600
		elif trophyValue >= 6700:
			return 4900
		else:
			print("Negative Trophy Value or superior at 6700! Should not happen!")
			return None

	def resetTrophies(self):
		#Allows trophies to be reseted for all players
		for player in self.members:
			player.trophies=self.returnResetValue(player.trophies)

	def calculateClanScore(self, considerateBestTr=False):
		index=0
		score=0

		for player in self.members:
			trophiesToConsider=player.trophies
			index += 1
			if considerateBestTr:
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

#-------------------------------------------------------
#--- Player manipulation 
#-------------------------------------------------------
	def addMember(self, player):
		#50th is kicked
		if len(self.members) == self.maxClanSize:
			self.members.remove(self.members[-1])
		self.members.append(player)
		self.members.sort(key = operator.attrgetter('trophies'), reverse=True)

	def findPlayer(self, playerName):
		for player in self.members:
			if player.name == playerName:
				return player
		print("Player with following name has not been found ! :" + playerName)
		return None


	#TODO : Maybe a update player method should be better..
	def updatePlayerTrophies(self, playerName, trophyValue):
		foundPlayer = self.findPlayer(playerName)
		if foundPlayer != None:
			foundPlayer.trophies=trophyValue
			if trophyValue > foundPlayer.best: 
				foundPlayer.best=trophyValue
			self.members.sort(key = operator.attrgetter('trophies'), reverse=True)


	#-----------------------------------------------------
	# --- Clan manipulation
	#-----------------------------------------------------

	def mergeWith(otherClan):
		self.additionalInfo = "Is the result of merge of " + self.name + " and "+ otherClan.name
		for member in otherClan.members:
			self.addMember(member)

	#-----------------------------------------------------
	#--- Printers
	#-----------------------------------------------------

	def printDefault(self):
		copy=list(self.members)
		copy.sort(key=operator.attrgetter('trophies'), reverse=True)
		rank=0
		for player in copy:
			rank += 1
			print(str(rank) + ". " + player.toString())

	def printBest(self):
		copy=list(self.members)
		copy.sort(key=operator.attrgetter('best'), reverse=True)
		rank=0
		for player in copy:
			rank += 1
			print(str(rank) + ". " + player.toStringBest())


