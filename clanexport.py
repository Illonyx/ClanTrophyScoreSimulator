from clanmodel import *
from clanIO import *

import copy as copyLib
class ExportManager: 

	def exportClanSortedByMaxTr(self, path, clan):
		copy=copyLib.deepcopy(clan)
		copy.members.sort(key=operator.attrgetter('best'), reverse=True)
		considerateBestTrForTrophyClan=True

		fileContent="Record Score clan : " + str(copy.calculateClanScore(considerateBestTrForTrophyClan)) + "\n"
		rank=0
		for player in copy.members:
			rank += 1
			currentRank=clan.members.index(clan.findPlayer(player.name)) + 1
			fileContent += str(rank) + ". " + player.toStringBest() + " (Rang actuel : " +  str(currentRank) + " / Tr : " + str(player.trophies) + " )\n"

			persistance=ClanPersistance(path)
			persistance.saveExport(fileContent)