from clanIO import *
from clanmodel import *

#sangRoyaleClans path
SR_CLAN_MEMBERS_FILE_PATH="members-sr-default.json"
SR_sangRoyaleClan_MEMBERS_OVERRIDEN="members-sr-overriden.json"

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

sangRoyaleClan.printDefault()