from dataclasses import dataclass
from pprint import pprint
from app.services.players.profile import HLTVPlayerProfile

if __name__ == "__main__":
    # Exemplo com s1mple (ID 7998)
    player_id = "7998"  # ID do jogador
    profile = HLTVPlayerProfile(player_id=player_id)
    data = profile.get_player_profile()
    pprint(data)
