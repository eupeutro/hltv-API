from dataclasses import dataclass

from app.services.base import HLTVBase
from app.utils.utils import extract_from_url
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

    def __parse_team_event_stats(self) -> list:

            team_lineup = self.get_text_by_xpath(Events.EventTeamStats.TEAM_LINEUP)
            team_coach = self.get_text_by_xpath(Events.EventTeamStats.TEAM_COACH)
            vrs_date = self.get_text_by_xpath(Events.EventTeamStats.VRS_DATE)
            vrs_points_before_event = self.get_text_by_xpath(Events.EventTeamStats.VRS_POINTS_BEFORE_EVENT)
            vrs_points_after_event = self.get_text_by_xpath(Events.EventTeamStats.VRS_POINTS_AFTER_EVENT)
            vrs_points_acquired = self.get_text_by_xpath(Events.EventTeamStats.VRS_POINTS_ACQUIRED)
            vrs_placement_before_event  = self.get_text_by_xpath(Events.EventTeamStats.VRS_PLACEMENT_BEFORE_EVENT)
            vrs_placement_after_event = self.get_text_by_xpath(Events.EventTeamStats.VRS_PLACEMENT_AFTER_EVENT)
            prize = self.get_text_by_xpath(Events.EventTeamStats.PRIZE)
            prize_club_share = self.get_text_by_xpath(Events.EventTeamStats.PRIZE_CLUB_SHARE)
            team_placement = self.get_text_by_xpath(Events.EventTeamStats.TEAM_PLACEMENT)
            team_logo_url = self.get_text_by_xpath(Events.EventTeamStats.TEAM_LOGO_URL)
            qualify_method = self.get_text_by_xpath(Events.EventTeamStats.QUALIFY_METHOD)
            