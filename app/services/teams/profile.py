from dataclasses import dataclass

from app.services.base import HLTVBase
from app.utils.utils import extract_from_url, clear_number_str, trim

from app.utils.xpath import Teams

@dataclass
class HLTVTeamProfile (HLTVBase):
    team_id: str
    
    def __post_init__(self) -> None:

        HLTVBase.__init__(self)
        url = f"https://www.hltv.org/team/{self.team_id}/who"
        self.URL = url
        self.page = self.request_url_page()

    def __parse_team_profile(self) -> list:
        
        team_name = self.get_text_by_xpath(Teams.TeamProfile.NAME)
        valve_ranking = clear_number_str(self.get_text_by_xpath(Teams.TeamProfile.VALVE_RANKING))
        world_ranking = clear_number_str(self.get_text_by_xpath(Teams.TeamProfile.WORLD_RANKING))
        weeks_in_top30_for_core = self.get_text_by_xpath(Teams.TeamProfile.WEEKS_IN_TOP30_FOR_CORE)

        logo_url = self.get_text_by_xpath(Teams.TeamProfile.LOGO_URL)
        social_media = self.get_all_by_xpath(Teams.TeamProfile.SOCIAL_MEDIA)

        
        average_player_age = self.get_text_by_xpath(Teams.TeamProfile.AVERAGE_PLAYER_AGE)

        player_nickname = self.get_all_by_xpath(Teams.TeamProfile.PLAYER_NICKNAME)
        player_url = self.get_all_by_xpath(Teams.TeamProfile.PLAYER_URL)

        coach_nickname = trim(self.get_text_by_xpath(Teams.TeamProfile.COACH_NICKNAME))
        coach_url = f"https://www.hltv{self.get_text_by_xpath(Teams.TeamProfile.COACH_URL)}"
        coach_id = extract_from_url(coach_url, 'id')


        lineup = []
        for (nickname, url) in zip(player_nickname, player_url):
            player_id = extract_from_url(url, 'id')

            lineup.append({
                "id": player_id,
                "nickname": nickname,
            })
        
        coach_data = [{
            "id": coach_id,
            "nickname":coach_nickname,
        }]

        return {
            "name": team_name,
            "valve_ranking": valve_ranking,
            "world_ranking": world_ranking,
            "weeks_in_top30_for_core": weeks_in_top30_for_core,
            "average_player_age": average_player_age,
            "lineup": lineup,
            "coach": coach_data,
            "logo_url": logo_url,
            "social_media": social_media
        }
    def get_team_profile(self) -> dict:

        self.response["id"] = self.team_id
        self.response["team_profile"] = self.__parse_team_profile()
        
        return self.response

        
