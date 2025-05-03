from dataclasses import dataclass
from lxml import etree


from app.services.base import HLTVBase
from app.utils.utils import trim,extract_from_url, extract_age
from app.utils.xpath import Players

@dataclass
class HLTVPlayerProfile (HLTVBase):
    """
    Service for retrieving and parsing a CS:GO player's profile from HLTV.

    Args:
        player_id (str): Unique identifier for the HLTV player.

    Attributes:
        URL (str): Formatted HLTV profile URL based on player ID.
    """
    player_id: str

    
    def __post_init__(self) -> None:
        """ Initialize the HLTVPlayerProfile class."""

        HLTVBase.__init__(self)
        url = f"https://www.hltv.org/player/{self.player_id}/who"
        self.URL = url
        self.page = self.request_url_page()
        
    def get_player_profile(self) -> dict:
     """
        Parses and returns the player's profile information.

        Returns:
            dict: A dictionary containing the player's unique identifier, profile information, and the timestamp of when
                the data was last updated.
    """
    
     self.response["id"] = extract_from_url(self.get_text_by_xpath(Players.Profile.URL), "id")
     self.response["nickname"] = self.get_text_by_xpath(Players.Profile.NICKNAME)
     self.response["name"] = self.get_text_by_xpath(Players.Profile.NAME)
     self.response["age"] = extract_age(self.get_text_by_xpath(Players.Profile.AGE))
     self.response["nationality"] = self.get_text_by_xpath(Players.Profile.NATIONALITY)
     self.response["rating"] = self.get_text_by_xpath(Players.Profile.RATING)
     self.response["current_team"] = self.get_text_by_xpath(Players.Profile.CURRENT_TEAM)
     self.response["current_team_url"] = f"https://www.hltv.org/{self.get_text_by_xpath(Players.Profile.CURRENT_TEAM_URL)}"
     self.response["image_url"] = self.get_text_by_xpath(Players.Profile.IMAGE_URL)
     self.response["url"] = self.get_text_by_xpath(Players.Profile.URL)
     self.response["social_media"] = self.get_all_by_xpath(Players.Profile.SOCIAL_MEDIA)
    

    
     
     return self.response