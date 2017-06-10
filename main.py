from clanIO import *

#Clans path
SR_CLAN_MEMBERS_DEFAULT="members-sr-default.json"
SR_CLAN_MEMBERS_OVERRIDEN="members-sr-overriden.json"

#Define potential players to enter
player_pierreJL=Player("PierreJL", 4307, 4428)
player_Chi=Player("Chi44chi", 4017, 4219)
player_Kebab=Player("KebabDeLaNight", 4014, 4151)
player_Boulad=Player("Boulad", 4000, 4000)
#player_Sky=Player("Skyice",4510, 4510)

#--4665

#Import mechanism
defaultClanImporter = ClanImporter(SR_CLAN_MEMBERS_DEFAULT, SR_CLAN_MEMBERS_OVERRIDEN)
defaultClanExporter = ClanExporter()
clansImported=defaultClanImporter.returnValues()
clan = Clan(clansImported[0], clansImported[1])

#defaultClanExporter.exportDefaultClanMaxTrInfo(clan)

#Add players
clan.addMember(player_pierreJL)
clan.addMember(player_Chi)
clan.addMember(player_Kebab)
clan.addMember(player_Boulad)
#clan.addMember(player_Sky)


clan.resetTrophies()
print("Norm " + str(clan.calculateOverriddenClanScore()))
clan.printDefault()