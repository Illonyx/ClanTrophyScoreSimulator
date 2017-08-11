from clanIO import *
from clanmodel import *
from clanexport import *

#Path
SR_CLAN_MEMBERS_FILE_PATH="Data/SangRoyale/members-sr-default.json"
SR_CLAN_MEMBERS_EXP_FILE_PATH="Data/SangRoyale/members-sr-example.json"
PIMANIACS_MEMBERS_FILE_PATH="Data/LesPimaniacs/members-pims.json"

exportManager=ExportManager()

#Define potential players to enter
player_pierreJL=Player("PierreJL", 4307, 4428)
player_Chi=Player("Chi44chi", 4017, 4219)
player_Kebab=Player("KebabDeLaNight", 4014, 4151)
player_Boulad=Player("Boulad", 4000, 4000)
#player_Sky=Player("Skyice",4510, 4510)

#--4665

sangRoyaleClan=Clan.loadFromFile(SR_CLAN_MEMBERS_FILE_PATH)
#Add players
sangRoyaleClan.addMember(player_pierreJL)
sangRoyaleClan.addMember(player_Chi)
sangRoyaleClan.addMember(player_Kebab)
sangRoyaleClan.addMember(player_Boulad)
#sangRoyaleClan.addMember(player_Sky)

exportManager.exportClanSortedByMaxTr("Exports/SangRoyale/sangRoyaleMaxTr.txt", sangRoyaleClan)

Clan.saveToFile(SR_CLAN_MEMBERS_EXP_FILE_PATH, sangRoyaleClan)

sangRoyaleClan.printDefault()