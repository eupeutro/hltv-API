from dataclasses import dataclass
from pprint import pprint
from lxml import etree
from app.services.players.profile import HLTVPlayerProfile
from app.services.players.search import HLTVPlayerSearch
from app.services.players.personalAchievements import HLTVPlayerPersonalAchievements
from app.services.players.teamAchievements import HLTVPlayerTeamAchievements
from app.services.players.trophies import HLTVPlayersTrophies

if __name__ == "__main__":
    # Exemplo com s1mple (ID 7998)

    query = "insani"
    player_id = "2023"  # ID do jogador
    profile = HLTVPlayerSearch(query=query)
    #data = profile.search_players()
    
    #achievements = HLTVPlayerTeamAchievements(player_id=player_id)

    achievements = HLTVPlayersTrophies(player_id= player_id)

    data = achievements.get_player_trophies()

    #data = achievements.get_player_team_achievements()

    print(data)
    #for i, row in enumerate(rows):
       # print(f"\n=== Linha {i+1} ===")
       # print(etree.tostring(row, pretty_print=True, encoding="unicode"))
    #pprint(data)

