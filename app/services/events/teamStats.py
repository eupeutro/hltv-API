from dataclasses import dataclass

from app.services.base import HLTVBase
from app.utils.utils import extract_from_url, clear_number_str
from app.utils.xpath import Events

@dataclass
class HLTVEventTeamStats(HLTVBase):
    event_id: str
    team_id: str

    def __post_init__(self) -> None:

        HLTVBase.__init__(self)
        url = f"https://www.hltv.org/events/{self.event_id}/who"
        self.URL = url
        self.page = self.request_url_page()

    def get_team_event_stats(self) -> dict:
            

            #placement
            team_placement = self.get_text_by_xpath(Events.EventTeamStats.TEAM_PLACEMENT.format(team_id = self.team_id))
            qualify_method = self.get_text_by_xpath(Events.EventTeamStats.QUALIFY_METHOD.format(team_id = self.team_id))
            
            
            #lineup
            team_lineup = self.get_all_by_xpath(Events.EventTeamStats.TEAM_LINEUP.format(team_id = self.team_id))
            team_coach = self.get_text_by_xpath(Events.EventTeamStats.TEAM_COACH.format(team_id = self.team_id))
           
            #vrs
            vrs_date = self.get_text_by_xpath(Events.EventTeamStats.VRS_DATE)
            vrs_points_before_event = self.get_text_by_xpath(Events.EventTeamStats.VRS_POINTS_BEFORE_EVENT.format(team_id = self.team_id))      
            vrs_points_after_event = self.get_text_by_xpath(Events.EventTeamStats.VRS_POINTS_AFTER_EVENT.format(team_id = self.team_id))
            vrs_points_acquired = self.get_text_by_xpath(Events.EventTeamStats.VRS_POINTS_ACQUIRED.format(team_id = self.team_id))
            vrs_placement_before_event  = clear_number_str(self.get_text_by_xpath(Events.EventTeamStats.VRS_PLACEMENT_BEFORE_EVENT.format(team_id = self.team_id)))
            vrs_placement_after_event = clear_number_str(self.get_text_by_xpath(Events.EventTeamStats.VRS_PLACEMENT_AFTER_EVENT.format(team_id = self.team_id)))
            
            #prize
            prize = clear_number_str(self.get_text_by_xpath(Events.EventTeamStats.PRIZE.format(team_id = self.team_id)))
            prize_club_share = clear_number_str(self.get_text_by_xpath(Events.EventTeamStats.PRIZE_CLUB_SHARE.format(team_id = self.team_id)))
            
            eventStats = {
                 "team_placement": team_placement,
                 "qualify_method": qualify_method,
                 "lineup":{
                        "lineup":team_lineup,
                        "coach":team_coach
                 },
                 "vrs":{
                        "vrs_date":vrs_date,
                        "points_before_event": vrs_points_before_event,
                        "points_after_event": vrs_points_after_event,
                        "points_acquired": vrs_points_acquired,
                        "placement_before_event": vrs_placement_before_event,
                        "placement_after_event": vrs_placement_after_event
                 },
                 "prize":{
                      "prize": prize,
                      "club_share":prize_club_share
                 }
            }

            self.response ["team_id"] = self.team_id
            self.response ["event_id"] = self.event_id
            self.response ["stats"] = eventStats

            return self.response