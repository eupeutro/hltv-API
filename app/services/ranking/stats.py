from dataclasses import dataclass

from app.services.base import HLTVBase
from app.utils.utils import extract_from_url, parse_date,clear_number_str
from app.utils.xpath import Ranking

@dataclass
class HLTVRankingStats(HLTVBase):

    def __post_init__(self) -> None:
        HLTVBase.__init__(self)
        url = "https://www.hltv.org/ranking/teams"
        self.URL = url
        self.page = self.request_url_page()

    def __parse_ranking_stats_(self) -> list:
        team_row = self.get_elements_by_xpath(Ranking.Stats.TEAM_ROW)

        ranking = []
        for team in team_row:
        
            team_name = self.get_text_by_xpath(Ranking.Stats.TEAM_NAME, element = team)
            team_url = self.get_text_by_xpath(Ranking.Stats.TEAM_URL, element = team)
            team_logo_url = self.get_text_by_xpath(Ranking.Stats.TEAM_LOGO_URL, element = team)
            placement = self.get_text_by_xpath(Ranking.Stats.PLACEMENT, element = team)
            team_id = extract_from_url(team_url, 'id')
            hltv_points = clear_number_str(self.get_text_by_xpath(Ranking.Stats.HLTV_POINTS))


            
            player_row = self.get_elements_by_xpath(Ranking.Stats.PLAYER_ROW, element = team)
            lineup = []
            
            for player in player_row:

                player_nickname = self.get_text_by_xpath(Ranking.Stats.PLAYER_NICKNAME, element = player)
                player_url = self.get_text_by_xpath(Ranking.Stats.PLAYER_URL, element = player)
                player_nationality = self.get_text_by_xpath(Ranking.Stats.PLAYER_NATIONALITY, element = player)
                player_picture_url = self.get_text_by_xpath(Ranking.Stats.PLAYER_PICTURE_URL, element = player)
                
                player_id = extract_from_url( player_url , 'id')
            
                lineup.append({
                    "player_id": player_id,
                    "nickname": player_nickname,
                    "nationality": player_nationality,
                    "picture_url": player_picture_url
            })
                
            ranking.append({
                "team_id": team_id,
                "team_name": team_name,
                "placement": placement,
                "hltv_points": hltv_points,
                "logo_url": team_logo_url,
                "lineup": lineup

            })


        return ranking

    def get_ranking_stats(self) -> dict:
        ranking_date = self.get_text_by_xpath(Ranking.Stats.RANKING_DATE)


        self.response["ranking_date"] = parse_date(ranking_date)
        self.response["ranking_stats"] = self.__parse_ranking_stats_()

        return self.response
