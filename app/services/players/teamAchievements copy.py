from dataclasses import dataclass

from app.services.base import HLTVBase
from app.utils.utils import trim, extract_from_url
from app.utils.xpath import Players

@dataclass
class HLTVPlayerTeamAchievements(HLTVBase):
    
    """
    A class for extracting team achievements from a player.

    Attributes:
        playerd_id (str): The HLTV player ID
    """
    
    
    player_id: str

    def __post_init__(self) -> None:
        """
        Initializes the base class, sets the URL to the player achivements tab, 
        sends the request and check if the page is valid.

        """

        HLTVBase.__init__(self)
        url = f"https://www.hltv.org/player/{self.player_id}/who#tab-achievementBox"
        self.URL = url
        self.page = self.request_url_page()
        self.raise_exception_if_not_found(xpath=Players.Profile.URL)

    def __parse_player_team_achievements(self) -> list:
        """
        Parses the player's team achievements section from the HLTV profile.

        Returns:
            list: A list of dictionaries, each containing information about 
                  each team achievement.
        """
        
        achievements = self.page.xpath(Players.teamAchievements.ROWS)
        
        player_achievements = []
        for achievement in achievements:
            placement = trim(achievement.xpath(Players.teamAchievements.PLACEMENT))
            
            team_name = trim(achievement.xpath(Players.teamAchievements.TEAM_NAME))
            team_url = trim(achievement.xpath(Players.teamAchievements.TEAM_URL))
            team_id = extract_from_url(team_url, "id")
           
            tournament_name = trim(achievement.xpath(Players.teamAchievements.TOURNAMENT_NAME))
            tournament_url = trim(achievement.xpath(Players.teamAchievements.TOURNAMENT_URL))
            tournament_id = extract_from_url(tournament_url, "id")

            player_stats_url =f"https://www.hltv.org/{trim(achievement.xpath(Players.teamAchievements.PLAYER_STATS_URL))}"
            
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
    

    def get_player_team_achievements(self) -> dict:
        """
        Retrieve the player's team achievement

        Returns:
            dict: A dictionary containing the player ID, number of achievements,
                  and a list of structured achievement data.

        """


        achievements = self.__parse_player_team_achievements()

        self.response["id"] = self.player_id
        self.response["achievement_count"] = len(achievements)
        self.response["achievements"] = achievements

        return self.response