from dataclasses import dataclass

from app.services.base import HLTVBase
from app.utils.utils import extract_from_url, trim
from app.utils.xpath import Teams

@dataclass
class HLTVTeamAchievements(HLTVBase):
    team_id: str

    def __post_init__(self) -> None:
        HLTVBase.__init__(self)
        url = f"https://www.hltv.org/team/{self.team_id}/who#tab-achievementsBox"
        self.URL = url
        self.page = self.request_url_page()
    
    def __parse_team_achievements(self) -> list:
        
        placements = self.get_all_by_xpath(Teams.Achievements.PLACEMENT)
        tournament_name = self.get_all_by_xpath(Teams.Achievements.TOURNAMENT_NAME)
        tournament_url = self.get_all_by_xpath(Teams.Achievements.TOURNAMENT_URL)

        team_achievements = []

        for (placement, name, url ) in zip(placements, tournament_name, tournament_url):
            tournament_id = extract_from_url(url, 'id')

            team_achievements.append({
                "id": tournament_id,
                "tournament_name": name,
                "placement": placement,
                "team_event_stats": f"https://www.hltv.org/stats/teams/{self.team_id}/who?event={tournament_id}"
            })

        return team_achievements
    
    def get_team_achievements(self) -> dict:

        self.response["id"] = self.team_id
        self.response["team_achievements"] = self.__parse_team_achievements()

        return self.response
        