from dataclasses import dataclass

from app.services.base import HLTVBase
from app.utils.utils import extract_from_url, clear_number_str
from app.utils.xpath import Events

@dataclass
class HLTVEventTeamStats(HLTVBase):
    """
    A class for extract stats from a team in an specific event.

    Attributes:
        event_id (str): The HLTV event id.
        team_id (str): The HLTV team id.
    """
    event_id: str
    team_id: str

    def __post_init__(self) -> None:
        """
        Initializes the base class, sets the URL to the player stats tab, 
        sends the request and check if the page is valid.

        """
        HLTVBase.__init__(self)
        url = f"https://www.hltv.org/events/{self.event_id}/who"
        self.URL = url
        self.page = self.request_url_page()
        self.raise_exception_if_not_found(xpath=Events.EventProfile.EVENT_URL)
    def get_team_event_stats(self) -> dict:
            """
            Parses and returns the team stats in an specific event.

            Returns:
                dict: A dictionary containing the team unique identifier, stats at the event, and the timestamp of when
                the data was last updated.
            """

            #placement
            team_placement = self.get_text_by_xpath(Events.EventTeamStats.TEAM_PLACEMENT.format(team_id = self.team_id))
            qualify_method = self.get_text_by_xpath(Events.EventTeamStats.QUALIFY_METHOD.format(team_id = self.team_id))
            
            
            #lineup
            team_lineup = self.get_all_by_xpath(Events.EventTeamStats.TEAM_LINEUP.format(team_id = self.team_id))
            team_player_url= self.get_all_by_xpath(Events.EventTeamStats.TEAM_PLAYER_URL.format(team_id = self.team_id))
            team_coach = self.get_text_by_xpath(Events.EventTeamStats.TEAM_COACH.format(team_id = self.team_id))
            team_coach_url = f"http://www.hltv.org{self.get_text_by_xpath(Events.EventTeamStats.TEAM_COACH_URL.format(team_id = self.team_id))}"



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
            
            lineup = []

            for (nickname, url) in zip(team_lineup, team_player_url):
                 player_id = extract_from_url(url, 'id')
                 
                 lineup.append({
                      "id": player_id,
                      "nickname": nickname,
                      "event_stats":  f"https://www.hltv.org/stats/players/{player_id}/who?event={self.event_id}"
                 })
            if team_coach_url: 
                 team_coach_id = extract_from_url(team_coach_url, 'id')

            eventStats = {
                "team_placement": team_placement,
                "qualify_method": qualify_method,
                "lineup":lineup,
                "coach":[{
                    "id": team_coach_id,
                    "nickname":team_coach
                }],
                 "vrs":[{
                        "vrs_date":vrs_date,
                        "points_before_event": vrs_points_before_event,
                        "points_after_event": vrs_points_after_event,
                        "points_acquired": vrs_points_acquired,
                        "placement_before_event": vrs_placement_before_event,
                        "placement_after_event": vrs_placement_after_event
                 }],
                 "prize":[{
                      "prize": prize,
                      "club_share":prize_club_share if prize_club_share else None
                 }]
            }

            self.response ["team_id"] = self.team_id
            self.response ["event_id"] = self.event_id
            self.response ["stats"] = eventStats
            return self.response