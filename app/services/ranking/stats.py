from dataclasses import dataclass

from app.services.base import HLTVBase
from app.utils.utils import extract_from_url, parse_date
from app.utils.xpath import Ranking

@dataclass
class HLTVRankingStats(HLTVBase):

    def __post_init__(self) -> None:
        HLTVBase.__init__(self)
        url = "https://www.hltv.org/ranking/teams"
        self.URL = url
        self.page = self.request_url_page()

    def __parse_team_achievements_(self) -> list:


        team_name = self.get_all_by_xpath(Ranking.Stats.TEAM_NAME)
        team_url = self.get_all_by_xpath(Ranking.Stats.TEAM_URL)
        team_logo_url = self.get_all_by_xpath(Ranking.Stats.TEAM_LOGO_URL)
        
        player_nickname = self.get_all_by_xpath(Ranking.Stats.PLAYER_NICKNAME)
        player_picture_url = self.get_all_by_xpath(Ranking.Stats.PLAYER_PICTURE_URL)
        player_url = self.get_all_by_xpath(Ranking.Stats.PLAYER_URL)
        player_nationality = self.get_all_by_xpath(Ranking.Stats.PLAYER_NATIONALITY)

        hltv_points = self.get_all_by_xpath(Ranking.Stats.HLTV_POINTS)
        placements = self.get_all_by_xpath(Ranking.Stats.PLACEMENT)

        ranking = []

        for (name, t_url, logo_url,nickname,picture_url, p_url, nationality, points, placement) in zip(team_name, team_url, team_logo_url, player_nickname, player_picture_url, player_url, player_nationality, hltv_points, placements):
            team_id = extract_from_url(t_url, 'id')
            player_id = extract_from_url(p_url, 'id')

            ranking.append({
                "team_id": team_id,
                "team_name": name,
                "placement": placement,
                "hltv_points": points,
                "lineup":{ 
                    "player_id": player_id,
                    "nickname": nickname,
                    "nationality": nationality,
                    "picture_url": picture_url
                },
                "logo_url": logo_url,
            })
    def get_ranking_stats(self) -> dict:
        ranking_date = self.get_text_by_xpath(Ranking.Stats.RANKING_DATE)


        self.response["ranking_date"] = parse_date(ranking_date)
        self.response["ranking_stats"] = self.__parse_team_achievements_()
