from clanIO import *
from clanmodel import *
from clanexport import *

#Path
SR_CLAN_MEMBERS_FILE_PATH="Data/SangRoyale/members-sr-default.json"
SR_CLAN_MEMBERS_EXP_FILE_PATH="Data/SangRoyale/members-sr-example.json"
PIMANIACS_MEMBERS_FILE_PATH="Data/LesPimaniacs/members-pims.json"

exportManager=ExportManager()

#Sang Royale clans
sangRoyaleClan=Clan.loadFromStatsRoyale("CJQLP2")
#sangRoyale2Clan=Clan.loadFromStatsRoyale("2LUU0R0L")
#sangRoyale3Clan=Clan.loadFromStatsRoyale("8CPG2YU")

#Fusion clans
#preda4EverClan=Clan.loadFromStatsRoyale("22QGV2U2")
#lesPimaniacsClan=Clan.loadFromStatsRoyale("JQLPGJ")
zealandiaClan=Clan.loadFromStatsRoyale("2YG288QU")

sangRoyaleClan.mergeWith(zealandiaClan)

#Add players
#sangRoyaleClan.addMember(player_pierreJL)
#sangRoyaleClan.addMember(player_Chi)
#sangRoyaleClan.addMember(player_Kebab)
#sangRoyaleClan.addMember(player_Boulad)
#sangRoyaleClan.addMember(player_Sky)
sangRoyaleClan.printDefault()
exportManager.exportClanSortedByMaxTr("Exports/SangRoyale/sangRoyaleMaxTr.txt", sangRoyaleClan)
print("HEre?")
#Clan.saveToFile(SR_CLAN_MEMBERS_EXP_FILE_PATH, sangRoyaleClan)
