from dataclasses import dataclass

from app.services.base import HLTVBase
from app.utils.utils import trim
from app.utils.xpath import Players

@dataclass
class HLTVPlayerPersonalAchievements(HLTVBase):
    player_id: str

    def __post_init__(self) -> None:
        
        HLTVBase.__init__(self)
        url = f"https://www.hltv.org/player/{self.player_id}/who"
        self.URL = url
        self.page = self.request_url_page()
        self.raise_exception_if_not_found(xpath = Players.Profile.URL)

    def __parse_player_personal_achievements(self) -> list:
        
        placements = self.get_all_by_xpath(Players.personalAchievements.TOP_20_PLACEMENT)
        years = self.get_all_by_xpath(Players.personalAchievements.TOP_20_YEAR)
        article_urls = self.get_all_by_xpath(Players.personalAchievements.TOP_20_ARTICLE_URL)

        top_20_list = []
        for i, (placement, year) in enumerate(zip(placements,years)):
            
            clean_placement = trim(placement)
            clean_year = f"20{year.strip('()\'')}"
            article = f"https://www.hltv.org{article_urls[i]}"

            top_20_list.append({
                "placement": clean_placement,
                "year": clean_year,
                "article": article
            })

        major_winner_count = self.get_text_by_xpath(Players.personalAchievements.MAJOR_WINNER_COUNT)
        major_mvp_count = self.get_text_by_xpath(Players.personalAchievements.MAJOR_MVP_COUNT)

        raw_mvp_winner = self.get_text_by_xpath(Players.personalAchievements.MVP_WINNER)
        
        if raw_mvp_winner:
            mvp_winner = raw_mvp_winner.split('\n')[1:]
        
        else:
            mvp_winner = []

        mvp_winner_count = self.get_text_by_xpath(Players.personalAchievements.MVP_WINNER_COUNT)
        
        return {

            "major_winner_count": major_winner_count if major_winner_count else None,
            "major_mvp_count": major_mvp_count if major_mvp_count else None, 
            "mvp_winner_count": mvp_winner_count if mvp_winner_count else None,
            "mvp_winner": mvp_winner if mvp_winner else None,
            "top_20": top_20_list if top_20_list else None,
        }
    
    def get_player_personal_achievements(self) -> dict:
        self.response["id"] = self.player_id
        self.response["personal_achievements"] = self.__parse_player_personal_achievements()
    
        return self.response