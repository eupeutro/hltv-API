from dataclasses import dataclass

from app.services.base import HLTVBase
from app.utils.utils import trim, extract_from_url
from app.utils.xpath import Players

@dataclass
class HLTVPlayerAchievements(HLTVBase):
    player_id: str

    def __post_init__(self) -> None:
        
        HLTVBase.__init__(self)
        url = f"https://www.hltv.org/player/{self.player_id}/who#tab-achievementBox"
        self.URL = url
        self.page = self.request_url_page()
        self.raise_exception_if_not_found(xpath=Players.Profile.URL)

    def __parse_player_achievements(self) -> list:

        achievements = self.page.xpath(Players.Achievements.ROWS)
        
        player_achievements = []
        for achievement in achievements:
            placement = trim(achievement.xpath(Players.Achievements.PLACEMENT))
            
            team_name = trim(achievement.xpath(Players.Achievements.TEAM_NAME))
            team_url = trim(achievement.xpath(Players.Achievements.TEAM_URL))
            team_id = extract_from_url(team_url, "id")
           
            tournament_name = trim(achievement.xpath(Players.Achievements.TOURNAMENT_NAME))
            tournament_url = trim(achievement.xpath(Players.Achievements.TOURNAMENT_URL))
            tournament_id = extract_from_url(tournament_url, "id")

            player_stats_url =f"https://www.hltv.org/{trim(achievement.xpath(Players.Achievements.PLAYER_STATS_URL))}"
            
            achievement_detail ={
                "placement": placement,
                "team": {
                    "id": team_id,
                    "name": team_name
                },
                "tournament":{
                    "id": tournament_id,
                    "name": tournament_name,
                },
                "player_stats_url": player_stats_url
            }

            player_achievements.append(achievement_detail)

        return player_achievements
    

    def get_player_achievements(self) -> dict:

        self.response["id"] = self.player_id
        self.response["achievements"] = self.__parse_player_achievements()

        return self.response