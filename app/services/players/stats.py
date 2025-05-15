from dataclasses import dataclass

from app.services.base import HLTVBase
from app.utils.utils import extract_float_from_percentage_number, convert_minutes_to_seconds, parse_float
from app.utils.xpath import Players

@dataclass
class HLTVPlayerStats(HLTVBase):
    
    """
    A class for extracting stats from a player.

    Attributes:
        playerd_id (str): The HLTV player ID
    """
    player_id: str

    def __post_init__(self) -> None:
        """
        Initializes the base class, sets the URL to the player stats tab, 
        sends the request and check if the page is valid.

        """

        HLTVBase.__init__(self)
        url = f"https://www.hltv.org/stats/players/{self.player_id}/who"
        self.URL = url
        self.page = self.request_url_page()
        self.raise_exception_if_not_found(xpath=Players.Profile.URL)
        
    def get_player_stats(self) -> dict:
        """
        Parses and returns the player's stats information.

        Returns:
            dict: A dictionary containing the player's unique identifier, stats, and the timestamp of when
                the data was last updated.
        """
        # firepower stats
        kills_per_round = parse_float(self.get_text_by_xpath(Players.Stats.KILLS_PER_ROUND))
        kills_per_round_win = parse_float(self.get_text_by_xpath(Players.Stats.KILLS_PER_ROUND_WIN))
        damage_per_round = parse_float(self.get_text_by_xpath(Players.Stats.DAMAGE_PER_ROUND))
        damage_per_round_win = parse_float(self.get_text_by_xpath(Players.Stats.DAMAGE_PER_ROUND_WIN))
        rounds_with_a_kill_percentage = extract_float_from_percentage_number(self.get_text_by_xpath(Players.Stats.ROUNDS_WITH_A_KILL_PERCENTAGE))
        rating_1_0 = parse_float(self.get_text_by_xpath(Players.Stats.RATING_1_0))
        rounds_with_multi_kill_percentage = extract_float_from_percentage_number(self.get_text_by_xpath(Players.Stats.ROUNDS_WITH_MULTI_KILL_PERCENTAGE))
        pistol_round_rating = parse_float(self.get_text_by_xpath(Players.Stats.PISTOL_ROUND_RATING))

        # entrying stats
        saved_by_teammate_per_round = parse_float(self.get_text_by_xpath(Players.Stats.SAVED_BY_TEAMMATE_PER_ROUND))
        traded_deaths_per_round = parse_float(self.get_text_by_xpath(Players.Stats.TRADED_DEATHS_PER_ROUND))
        traded_deaths_percentage = extract_float_from_percentage_number(self.get_text_by_xpath(Players.Stats.TRADED_DEATHS_PERCENTAGE))
        opening_deaths_traded_percentage = extract_float_from_percentage_number(self.get_text_by_xpath(Players.Stats.OPENING_DEATHS_TRADED_PERCENTAGE))
        assists_per_round = parse_float(self.get_text_by_xpath(Players.Stats.ASSISTS_PER_ROUND))
        support_rounds_percentage = extract_float_from_percentage_number(self.get_text_by_xpath(Players.Stats.SUPPORT_ROUNDS_PERCENTAGE))

        # trading stats
        saved_teammate_per_round = parse_float(self.get_text_by_xpath(Players.Stats.SAVED_TEAMMATE_PER_ROUND))
        trade_kills_per_round = parse_float(self.get_text_by_xpath(Players.Stats.TRADE_KILLS_PER_ROUND))
        trade_kills_percentage = extract_float_from_percentage_number(self.get_text_by_xpath(Players.Stats.TRADE_KILLS_PERCENTAGE))
        assisted_kills_percentage = extract_float_from_percentage_number(self.get_text_by_xpath(Players.Stats.ASSISTED_KILLS_PERCENTAGE))
        damage_per_kill = parse_float(self.get_text_by_xpath(Players.Stats.DAMAGE_PER_KILL))

        # opening stats
        opening_kills_per_round = parse_float(self.get_text_by_xpath(Players.Stats.OPENING_KILLS_PER_ROUND))
        opening_deaths_per_round = parse_float(self.get_text_by_xpath(Players.Stats.OPENING_DEATHS_PER_ROUND))
        opening_attempts_percentage = extract_float_from_percentage_number(self.get_text_by_xpath(Players.Stats.OPENING_ATTEMPTS_PERCENTAGE))
        opening_success = extract_float_from_percentage_number(self.get_text_by_xpath(Players.Stats.OPENING_SUCCESS_PERCENTAGE))
        win_after_opening_kill_percentage = extract_float_from_percentage_number(self.get_text_by_xpath(Players.Stats.WIN_AFTER_OPENING_KILL_PERCENTAGE))
        attacks_per_round = parse_float(self.get_text_by_xpath(Players.Stats.ATTACKS_PER_ROUND))

        # clutching stats
        clutch_points_per_round = parse_float(self.get_text_by_xpath(Players.Stats.CLUTCH_POINTS_PER_ROUND))
        last_alive_percentage = extract_float_from_percentage_number(self.get_text_by_xpath(Players.Stats.LAST_ALIVE_PERCENTAGE))
        _1v1_win_percentage = extract_float_from_percentage_number(self.get_text_by_xpath(Players.Stats._1v1_WIN_PERCENTAGE))
        time_alive_per_round = convert_minutes_to_seconds(self.get_text_by_xpath(Players.Stats.TIME_ALIVE_PER_ROUND))
        saves_per_round_loss_percentage = extract_float_from_percentage_number(self.get_text_by_xpath(Players.Stats.SAVES_PER_ROUND_LOSS_PERCENTAGE))

        # sniping stats
        sniper_kills_per_round = parse_float(self.get_text_by_xpath(Players.Stats.SNIPER_KILLS_PER_ROUND))
        sniper_kills_percentage = extract_float_from_percentage_number(self.get_text_by_xpath(Players.Stats.SNIPER_KILLS_PERCENTAGE))
        rounds_with_sniper_kills_percentage = extract_float_from_percentage_number(self.get_text_by_xpath(Players.Stats.ROUNDS_WITH_SNIPER_KILLS_PERCENTAGE))
        sniper_multi_kill_rounds = parse_float(self.get_text_by_xpath(Players.Stats.SNIPER_MULTI_KILL_ROUNDS))
        sniper_opening_kills_per_round = parse_float(self.get_text_by_xpath(Players.Stats.SNIPER_OPENING_KILLS_PER_ROUND))

        # utility stats
        utility_damage_per_round = parse_float(self.get_text_by_xpath(Players.Stats.UTILITY_DAMAGE_PER_ROUND))
        utility_kills_per_100_rounds = parse_float(self.get_text_by_xpath(Players.Stats.UTILITY_KILLS_PER_100_ROUNDS))
        flashes_thrown_per_round = parse_float(self.get_text_by_xpath(Players.Stats.FLASHES_THROWN_PER_ROUND))
        flash_assists_per_round = parse_float(self.get_text_by_xpath(Players.Stats.FLASH_ASSISTS_PER_ROUND))
        time_opponent_flashed_per_round = parse_float(self.get_text_by_xpath(Players.Stats.TIME_OPPONENT_FLASHED_PER_ROUND))
        player_stats = {

            "firepower": {
                "kills_per_round": kills_per_round,
                "kills_per_round_win": kills_per_round_win,
                "damage_per_round": damage_per_round,
                "damage_per_round_win": damage_per_round_win,
                "rounds_with_a_kill_percentage": rounds_with_a_kill_percentage,
                "rating_1_0": rating_1_0,
                "rounds_with_multi_kill_percentage": rounds_with_multi_kill_percentage,
                "pistol_round_rating": pistol_round_rating,
    },

        "entrying": {
            "saved_by_teammate_per_round": saved_by_teammate_per_round,
            "traded_deaths_per_round": traded_deaths_per_round,
            "traded_deaths_percentage": traded_deaths_percentage,
            "opening_deaths_traded_percentage": opening_deaths_traded_percentage,
            "assists_per_round": assists_per_round,
            "support_rounds_percentage": support_rounds_percentage,
    },

        "trading": {
            "saved_teammate_per_round": saved_teammate_per_round,
            "trade_kills_per_round": trade_kills_per_round,
            "trade_kills_percentage": trade_kills_percentage,
            "assisted_kills_percentage": assisted_kills_percentage,
            "damage_per_kill": damage_per_kill,
    },

        "opening": {
            "opening_kills_per_round": opening_kills_per_round,
            "opening_deaths_per_round": opening_deaths_per_round,
            "opening_attempts_percentage": opening_attempts_percentage,
            "opening_success_percentage": opening_success,
            "win_after_opening_kill_percentage": win_after_opening_kill_percentage,
            "attacks_per_round": attacks_per_round,
    },

        "clutching": {
            "clutch_points_per_round": clutch_points_per_round,
            "last_alive_percentage": last_alive_percentage,
            "1v1_win_percentage": _1v1_win_percentage,
            "time_alive_per_round": time_alive_per_round,
            "saves_per_round_loss_percentage": saves_per_round_loss_percentage,
    },

        "sniping": {
            "sniper_kills_per_round": sniper_kills_per_round,
            "sniper_kills_percentage": sniper_kills_percentage,
            "rounds_with_sniper_kills_percentage": rounds_with_sniper_kills_percentage,
            "sniper_multi_kill_rounds": sniper_multi_kill_rounds,
            "sniper_opening_kills_per_round": sniper_opening_kills_per_round,
    },

        "utility": {
            "utility_damage_per_round": utility_damage_per_round,
            "utility_kills_per_100_rounds": utility_kills_per_100_rounds,
            "flashes_thrown_per_round": flashes_thrown_per_round,
            "flash_assists_per_round": flash_assists_per_round,
            "time_opponent_flashed_per_round": time_opponent_flashed_per_round,
    },
}
        self.response["id"] = self.player_id
        self.response["stats"] = player_stats

        return self.response
