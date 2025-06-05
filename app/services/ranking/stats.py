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

    def __parse_ranking_stats_(self) -> list:


        team_name = self.get_all_by_xpath(Ranking.Stats.TEAM_NAME)
        team_url = self.get_all_by_xpath(Ranking.Stats.TEAM_URL)
        team_logo_url = self.get_all_by_xpath(Ranking.Stats.TEAM_LOGO_URL)
        
        player_nickname = self.get_all_by_xpath(Ranking.Stats.PLAYER_NICKNAME)
        player_url = self.get_all_by_xpath(Ranking.Stats.PLAYER_URL)
        player_nationality = self.get_all_by_xpath(Ranking.Stats.PLAYER_NATIONALITY)
        player_picture_url = self.get_all_by_xpath(Ranking.Stats.PLAYER_PICTURE_URL)
    
        #hltv_points = self.get_all_by_xpath(Ranking.Stats.HLTV_POINTS)
        placements = self.get_all_by_xpath(Ranking.Stats.PLACEMENT)

        

        #nickname, picture_url, p_url, nationality, 
        #player_nickname, player_picture_url, player_url, player_nationality
        #player_id = extract_from_url(p_url, 'id')

        lineup = []
        for (nickname, p_url, nationality, picture_url) in zip(player_nickname, player_url, player_nationality, player_picture_url):
            player_id = extract_from_url( p_url , 'id')
            
            lineup.append({
                "player_id": player_id,
                "nickname": nickname,
                "nationality": nationality,
                "picture_url": picture_url
            })

        ranking = []
        for (name, t_url, logo_url, placement) in zip(team_name, team_url, team_logo_url, placements):
            team_id = extract_from_url(t_url, 'id')
            

            ranking.append({
                "team_id": team_id,
                "team_name": name,
                "placement": placement,
                #"hltv_points": points,
                "lineup": lineup,
                "logo_url": logo_url,
            })
            

        return ranking

    def get_ranking_stats(self) -> dict:
        ranking_date = self.get_text_by_xpath(Ranking.Stats.RANKING_DATE)


        self.response["ranking_date"] = parse_date(ranking_date)
        self.response["ranking_stats"] = self.__parse_ranking_stats_()

        return self.response
