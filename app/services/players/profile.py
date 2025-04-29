from dataclasses import dataclass
from lxml import etree

from app.services.base import HLTVBase
from app.utils.utils import trim 
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
    #URL: str = f"https://www.hltv.org/player/{player_id}/-"
    
    def __post_init__(self) -> None:
        url = f"https://www.hltv.org/player/{self.player_id}/-"
        HLTVBase.__init__(self)
        self.URL = url
        self.page = self.request_url_page()
        
    def get_player_profile(self) -> dict:
     """
        Parses and returns the player's profile information.

        Returns:
            dict: Player profile data.
    """
     self.response["id"] = self.player_id
     self.response["nickName"] = self.get_text_by_xpath(Players.Profile.NICKNAME)
     self.response["rating"] = self.get_text_by_xpath(Players.Profile.RATING)
     self.response["name"] = self.get_text_by_xpath(Players.Profile.NAME)
     self.response["age"] = self.get_text_by_xpath(Players.Profile.AGE)
     self.response["nationality"] = self.get_text_by_xpath(Players.Profile.NATIONALITY)
     self.response["currentTeam"] = self.get_text_by_xpath(Players.Profile.CURRENT_TEAM)
     self.response["currentTeamurl"] = f"https://www.hltv.org/{self.get_text_by_xpath(Players.Profile.CURRENT_TEAM_URL)}"
     
     html_string = etree.tostring(self.page, pretty_print=True).decode("utf-8")
     #print(html_string)
     return self.response