from dataclasses import dataclass

from app.services.base import HLTVBase
from app.utils.utils import extract_from_url
from app.utils.xpath import Events

@dataclass
class HLTVEventProfile (HLTVBase):
    """
    Class for retrieving and parsing a event profile from HLTV.

    Args:
        player_id (str): Unique identifier for the HLTV event.

    Attributes:
        URL (str): Formatted HLTV profile URL based on event ID.
    """
    event_id: str

    def __post_init__(self) -> None:
        """ Initialize the HLTVEventProfile class."""

        HLTVBase.__init__(self)
        url = f"https://www.hltv.org/events/{self.event_id}/who"
        self.URL = url
        self.page = self.request_url_page 
    
    def __parse_event_profile(self) -> list:
        """
        Parses the event profile data from the retrieved HLTV event profile tab.


        """
        event_name = self.get_text_by_xpath(Events.EventProfile.EVENT_NAME)
        team_count= self.get_text_by_xpath(Events.EventProfile.TEAM_COUNT)
        event_start_date = self.get_text_by_xpath(Events.EventProfile.EVENT_START_DATE)
        event_end_date = self.get_text_by_xpath(Events.EventProfile.EVENT_END_DATE)
        prize_pool = self.get_text_by_xpath(Events.EventProfile.PRIZE_POOL)
        event_location = self.get_text_by_xpath(Events.EventProfile.EVENT_LOCATION)
        location_flag_url = self.get_text_by_xpath(Events.EventProfile.LOCATION_FLAG_URL)
        event_mvp_nickname = self.get_text_by_xpath(Events.EventProfile.EVENT_MVP_NICKNAME)
        event_mvp_url = self.get_text_by_xpath(Events.EventProfile.EVENT_MVP_URL)
        event_mvp_id = extract_from_url(event_mvp_url, "id")
        event_evps_nickname = self.get_all_by_xpath(Events.EventProfile.EVENT_EVPS_NICKNAME)
        event_evps_url = self.get_all_by_xpath(Events.EventProfile.EVENT_EVPS_URL)
        team_name = self.get_all_by_xpath(Events.EventProfile.TEAM_NAME)
        team_url = self.get_all_by_xpath(Events.EventProfile.TEAM_URL)
        team_logo_url = self.get_all_by_xpath(Events.EventProfile.TEAM_LOGO_URL)
        qualify_method = self.get_all_by_xpath(Events.EventProfile.QUALIFY_METHOD) 

#dentro do for:
        #evps_id 
        #team_id