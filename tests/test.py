from dataclasses import dataclass
from pprint import pprint
from lxml import etree
from app.services.players.profile import HLTVPlayerProfile
from app.services.players.search import HLTVPlayerSearch
from app.services.events.search import HLTVEventsSearch
from app.services.players.personalAchievements import HLTVPlayerPersonalAchievements
from app.services.players.teamAchievements import HLTVPlayerTeamAchievements
from app.services.players.trophies import HLTVPlayersTrophies
from app.services.players.stats import HLTVPlayerStats
from app.services.players.careerStats import HLTVPlayerCareerStats
from app.services.events.profile import HLTVEventProfile
from app.services.events.teamStats import HLTVEventTeamStats

if __name__ == "__main__":
    # Exemplo com s1mple (ID 7998)

    query = "pro league"
    
    team_id = "9565"  # ID do jogador
    event_id = "8037"
    profile = HLTVEventTeamStats(event_id=event_id, team_id= team_id)
    data = profile.get_team_event_stats()
    
    #achievements = HLTVPlayerTeamAchievements(player_id=player_id)

    #achievements = HLTVPlayerCareerStats(player_id= player_id)

    #data = achievements.get_player_career_stats()

   

    print(data)
    #for i, row in enumerate(rows):
       # print(f"\n=== Linha {i+1} ===")
       # print(etree.tostring(row, pretty_print=True, encoding="unicode"))
    #pprint(data)

