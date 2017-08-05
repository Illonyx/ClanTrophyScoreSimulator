import json

class ClanPersistance:

	def __init__(self, path):
		self.path = path

	def importFile(self, fileName):
		fo = open(fileName)
		print("Name of the file: ", fo.name)

		line = fo.read()
		fo.close()
		return line

	def loadClan(self):
		playersInClan=[]
		try:
			strFile=self.importFile(self.path)
			listDic=json.loads(strFile)
			
		except FileNotFoundError:
			print("File with " + str(fileName) + " not found")

		return listDic

"""

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
"""
