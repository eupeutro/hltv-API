from dataclasses import dataclass
from pprint import pprint
from lxml import etree
from app.services.players.profile import HLTVPlayerProfile
from app.services.players.search import HLTVPlayerSearch
from app.services.players.achievements import HLTVPlayerAchievements

if __name__ == "__main__":
    # Exemplo com s1mple (ID 7998)

    query = "insani"
    player_id = "2023"  # ID do jogador
    profile = HLTVPlayerSearch(query=query)
    #data = profile.search_players()
    
    achievements = HLTVPlayerAchievements(player_id= player_id)

    rows = achievements.page.xpath("//table[@class='table-container achievement-table']/tbody/tr[@class='team']")
    for i, row in enumerate(rows):
        print(f"\n=== Conquista {i + 1} (HTML) ===")
        print(etree.tostring(row, pretty_print=True, encoding="unicode"))

        print(f"\n=== Conquista {i + 1} (Texto) ===")
        text_content = row.xpath("string()")  # Isso retorna uma lista com o texto completo
        print(text_content[0].strip() if text_content else  "no text found")
    #pprint(data)

