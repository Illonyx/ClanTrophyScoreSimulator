import json
import collections
from clanmodel import *


class ClanImporter:

	def __init__(self, defaultPath, overridenPath):
		self.defaultClan=self.readPlayerDataFromFile(defaultPath)
		self.overriddenClan=self.manageOverridenClan(overridenPath, self.defaultClan)

	def importFile(self, fileName):
		fo = open(fileName)
		print("Name of the file: ", fo.name)

		line = fo.read()
		fo.close()
		return line

	def readPlayerDataFromFile(self, fileName):
		playersInClan=[]
		try:
			strFile=self.importFile(fileName)
			listDic=json.loads(strFile)
			for dic in listDic:
				#TODO: there should be a better way..
				if dic["best"] < dic["trophies"]:
					print("Erreur de saisie pour le joueur : " + dic["name"])

				player=Player(dic["name"], dic["trophies"], dic["best"])
				playersInClan.append(player)
			playersInClan.sort(key = operator.attrgetter('trophies'), reverse=True)
		except FileNotFoundError:
			print("File with " + str(fileName) + " not found")

		return playersInClan

	def manageOverridenClan(self, overridenFileName, defaultValue):
		overridenClan=self.readPlayerDataFromFile(overridenFileName)
		if len(overridenClan) == 0:
			overridenClan = defaultValue
		return overridenClan

	def returnValues(self):
		return (self.defaultClan, self.overriddenClan)


class ClanExporter:

	def __init__(self, defaultExportMaxTrPath="exports/defaultMaxTr.txt", 
			overriddenExportPath="exports/overridden.txt", overriddenExportMaxTrPath="exports/overriddenMaxTr.txt"):
		self.defaultExportMaxTrPath=defaultExportMaxTrPath
		self.overriddenExportPath=overriddenExportPath
		self.overriddenExportMaxTrPath=overriddenExportMaxTrPath

	def exportFile(self, fileName, content):
		fo = open(fileName)
		print("Name of the file: ", fo.name)

		line = fo.read()
		fo.close()


	def exportDefaultClanMaxTrInfo(self, clan):

		score = clan.calculateDefaultClanScore(True)
		copy=list(clan.defaultClan)
		fo=open(self.defaultExportMaxTrPath, "w")

		fo.write("Record Score clan : " + str(score) + "\n")

		copy.sort(key=operator.attrgetter('best'), reverse=True)
		rank=0
		for player in copy:
			rank += 1
			currentRank=clan.defaultClan.index(player) + 1
			fo.write(str(rank) + ". " + player.toStringBest() + " (Rang actuel : " +  str(currentRank) + " / Tr : " + str(player.trophies) + " )\n")
		

		
		

		#Export trophy score

		#Export all members

	#def exportOverridenClanInfo(self, overridenClan):
