from dataclasses import dataclass

from app.services.base import HLTVBase
from app.utils.utils import extract_float_from_percentage_number
from app.utils.xpath import Players

@dataclass
class HLTVPlayerCareerStats(HLTVBase):

    """
    A class for extractng career stats from a player.
    
    Attributes:
        player_id (str): The HLTV player ID
    """

    player_id: str

    def __post_init__(self) -> None:
        HLTVBase.__init__(self)
        url = f"https://www.hltv.org/stats/players/{self.player_id}/who"
        self.URL = url
        self.page = self.request_url_page()
        self.raise_exception_if_not_found(xpath=Players.Profile.URL)

    def get_player_career_stats(self) -> dict:

        total_kills = int(self.get_text_by_xpath(Players.careerStats.TOTAL_KILLS))
        headshot_percentage = extract_float_from_percentage_number(self.get_text_by_xpath(Players.careerStats.HEADSHOT_PERCENTAGE))
        total_deaths = int(self.get_text_by_xpath(Players.careerStats.TOTAL_DEATHS))
        kd_ratio = float(self.get_text_by_xpath(Players.careerStats.KD_RATIO))
        damage_per_round = float(self.get_text_by_xpath(Players.careerStats.DAMAGE_PER_ROUND))
        grenade_dmg_per_round = float(self.get_text_by_xpath(Players.careerStats.GRENADE_DMG_PER_ROUND))
        maps_played = int(self.get_text_by_xpath(Players.careerStats.MAPS_PLAYED))
        rounds_played = int(self.get_text_by_xpath(Players.careerStats.ROUNDS_PLAYED))
        kills_per_round = float(self.get_text_by_xpath(Players.careerStats.KILLS_PER_ROUND))
        assists_per_round = float(self.get_text_by_xpath(Players.careerStats.ASSISTS_PER_ROUND))
        deaths_per_round = float(self.get_text_by_xpath(Players.careerStats.DEATHS_PER_ROUND))
        saved_by_teammate_per_round = float(self.get_text_by_xpath(Players.careerStats.SAVED_BY_TEAMMATE_PER_ROUND))
        saved_teammates_per_round = float(self.get_text_by_xpath(Players.careerStats.SAVED_TEAMMATES_PER_ROUND))
        rating_1_0 = float(self.get_text_by_xpath(Players.careerStats.RATING1_0))

        career_stats = {
            "total_kills": total_kills,
            "headshot_percentage": headshot_percentage,
            "total_deaths": total_deaths,
            "kd_ratio": kd_ratio,
            "damage_per_round": damage_per_round,
            "grenade_dmg_per_round": grenade_dmg_per_round,
            "maps_played": maps_played,
            "rounds_played": rounds_played,
            "kills_per_round": kills_per_round,
            "assists_per_round": assists_per_round,
            "deaths_per_round": deaths_per_round,
            "saved_by_teammate_per_round": saved_by_teammate_per_round,
            "saved_teammates_per_round": saved_teammates_per_round,
            "rating_1_0": rating_1_0
        }

        self.response ["id"] = self.player_id
        self.response ["careerStats"] = career_stats

        return self.response