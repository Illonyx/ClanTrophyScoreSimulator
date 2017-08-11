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

	def saveFile(self, fileName, fileContent):
		fo = open(fileName, "w")
		fo.write(fileContent)
		fo.close()

	def loadClan(self):
		try:
			strFile=self.importFile(self.path)
			jsonObject=json.loads(strFile)
			
		except FileNotFoundError:
			print("File with " + str(fileName) + " not found")

		return jsonObject

	def saveClan(self,clan):
		try:
			clanStr = json.dumps(clan)
			self.saveFile(self.path, clanStr)

		except FileNotFoundError:
				print("File with " + str(fileName) + " not found")

	def saveExport(self, export):
		try:
			self.saveFile(self.path, export)

		except FileNotFoundError:
				print("File with " + str(fileName) + " not found")