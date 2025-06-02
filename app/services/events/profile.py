from dataclasses import dataclass

from app.services.base import HLTVBase
from app.utils.utils import extract_from_url,clear_number_str
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
        self.page = self.request_url_page()
    
    def __parse_event_profile(self) -> list:
        """
        Parses the event profile data from the retrieved HLTV event profile tab.


        """
      
        event_name = self.get_text_by_xpath(Events.EventProfile.EVENT_NAME)
        team_count= self.get_text_by_xpath(Events.EventProfile.TEAM_COUNT)
        event_start_date = self.get_text_by_xpath(Events.EventProfile.EVENT_START_DATE)
        event_end_date = self.get_text_by_xpath(Events.EventProfile.EVENT_END_DATE)
        prize_pool = clear_number_str(self.get_text_by_xpath(Events.EventProfile.PRIZE_POOL))
        event_location = self.get_text_by_xpath(Events.EventProfile.EVENT_LOCATION)
        location_flag_url = f"https://www.hltv.org{self.get_text_by_xpath(Events.EventProfile.LOCATION_FLAG_URL)}"
      
        event_mvp_nickname = self.get_text_by_xpath(Events.EventProfile.EVENT_MVP_NICKNAME)
        event_mvp_url_suffix = self.get_text_by_xpath(Events.EventProfile.EVENT_MVP_URL)
        
        
     
        event_evps_nickname = self.get_all_by_xpath(Events.EventProfile.EVENT_EVPS_NICKNAME)
        event_evps_url = self.get_all_by_xpath(Events.EventProfile.EVENT_EVPS_URL)
        
      
        team_name = self.get_all_by_xpath(Events.EventProfile.TEAM_NAME)
        team_url = self.get_all_by_xpath(Events.EventProfile.TEAM_URL)
        team_placement = self.get_all_by_xpath(Events.EventProfile.TEAM_PLACEMENT)


        mvp_list = None

        if event_mvp_nickname and event_mvp_url_suffix:
            event_mvp_url = f"https://www.hltv.org{event_mvp_url_suffix}"
            event_mvp_id = extract_from_url(event_mvp_url, 'id')
            
            mvp_list =[{
                "id": event_mvp_id,
                "nickname": event_mvp_nickname,
                "event_stats": f"https://www.hltv.org/stats/players/{event_mvp_id}/who?event={self.event_id}"
            }]

        team_list = []

        for (name, url,placement) in zip(team_name, team_url,team_placement):
            id = extract_from_url(url, 'id')

            team_list.append({
                "id": id,
                "name": name,
                "team_placement": placement
            })


        evps_list = []
        for (nickname, url) in zip(event_evps_nickname, event_evps_url):
            
            event_evp_id = extract_from_url(url, 'id')

            evps_list.append({
                "id": event_evp_id,
                "nickname": nickname,
                "event_stats": f"https://www.hltv.org/stats/players/{event_evp_id}/who?event={self.event_id}"
            })

        return {
            "name": event_name,
            "start_date": event_start_date,
            "end_date": event_end_date,
            "teams": team_list,
            "team_count": team_count,
            "prize_pool": prize_pool,
            "location": event_location,
            "location_flag_url": location_flag_url,
            "mvp": mvp_list if mvp_list else None,
            "evps": evps_list if  evps_list else None
             }
    
    def get_event_profile(self) -> dict:

        self.response ["id"] = self.event_id
        self.response["event_profile"] = self.__parse_event_profile()

        return self.response