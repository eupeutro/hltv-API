from dataclasses import dataclass

from app.services.base import HLTVBase
from app.utils.utils import trim
from app.utils.xpath import Players

@dataclass
class HLTVPlayerPersonalAchievements(HLTVBase):
    """
    A class for extract personal achievements from a player. 

    Attributes:
        player_id (str): The HLTV player id.
    """
    player_id: str

    def __post_init__(self) -> None:
        """        
        Initializes the base class, sets the URL to the player profile page, 
        sends the request and check if the page is valid.
        """
        HLTVBase.__init__(self)
        url = f"https://www.hltv.org/player/{self.player_id}/who#tab-trophiesBox"
        self.URL = url
        self.page = self.request_url_page()
        self.raise_exception_if_not_found(xpath = Players.Profile.URL)

    def __parse_player_personal_achievements(self) -> list:
        """
        Parses the player's achievements section from the retrieved HLTV data.

        Returns:
        list: A list of dictionaries, where each dictionary contains information about a specific
              achievement. Each dictionary includes the following keys:
                - 'title': The name or title of the achievement.
                - 'count': The number of times the player received this achievement.
        """
        placements = self.get_all_by_xpath(Players.personalAchievements.TOP_20_PLACEMENT)
        years = self.get_all_by_xpath(Players.personalAchievements.TOP_20_YEAR)
        article_urls = self.get_all_by_xpath(Players.personalAchievements.TOP_20_ARTICLE_URL)

        top_20_list = []
        for i, (placement, year) in enumerate(zip(placements,years)):
        
            clean_placement = trim(placement)
            clean_year = "20" + year.strip("()'")
            article = f"https://www.hltv.org{article_urls[i]}"

            top_20_list.append({
                "placement": clean_placement,
                "year": clean_year,
                "article": article
            })

        major_winner_count = self.get_text_by_xpath(Players.personalAchievements.MAJOR_WINNER_COUNT)
        major_mvp_count = self.get_text_by_xpath(Players.personalAchievements.MAJOR_MVP_COUNT)

        raw_mvp_winner = self.get_text_by_xpath(Players.personalAchievements.MVP_WINNER)

        evp_at = self.get_all_by_xpath(Players.personalAchievements.EVP)

        if raw_mvp_winner:
            mvp_winner = raw_mvp_winner.split('\n')[1:]
        
        else:
            mvp_winner = []

        mvp_winner_count = self.get_text_by_xpath(Players.personalAchievements.MVP_WINNER_COUNT)
        
        return {

            "major_winner_count": major_winner_count if major_winner_count else None,
            "major_mvp_count": major_mvp_count if major_mvp_count else None, 
            "mvp_winner_count": mvp_winner_count if mvp_winner_count else None,
            "evp_count": len(evp_at) if evp_at else None,
            "top_20_count": len(top_20_list) if top_20_list else None,
            "mvp_winner": mvp_winner if mvp_winner else None,
            "evp_at": evp_at if evp_at else None,
            "top_20": top_20_list if top_20_list else None,
        }
    
    def get_player_personal_achievements(self) -> dict:
        """
    Retrieves and parses the personal achievements of the player.

    Returns:
        dict: A dictionary containing the player's unique identifier (`id`) and their 
              personal achievements under the key `personal_achievements`.
        """


        self.response["id"] = self.player_id
        self.response["personal_achievements"] = self.__parse_player_personal_achievements()
    
        return self.response