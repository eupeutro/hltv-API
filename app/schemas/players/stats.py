from typing import Optional, List

from app.schemas.base import HLTVBaseModel ,AuditMixin



class PlayerStatsFirepower(HLTVBaseModel):
    kills_per_round: Optional[float]
    kills_per_round_win: Optional[float]
    damage_per_round: Optional[float] = None
    damage_per_round_win: Optional[float]
    rounds_with_a_kill_percentage: Optional[float]
    rating_1_0: Optional[float]
    rounds_with_multi_kill_percentage: Optional[float]
    pistol_round_rating: Optional[float]


class PlayerStatsEntrying(HLTVBaseModel):
    saved_by_teammate_per_round: Optional[float]
    traded_deaths_per_round: Optional[float]
    traded_deaths_percentage: Optional[float]
    opening_deaths_traded_percentage: Optional[float]
    assists_per_round: Optional[float]
    support_rounds_percentage: Optional[float]


class PlayerStatsTrading(HLTVBaseModel):
    saved_teammate_per_round: Optional[float]
    trade_kills_per_round: Optional[float]
    trade_kills_percentage: Optional[float]
    assisted_kills_percentage: Optional[float]
    damage_per_kill: Optional[float]


class PlayerStatsOpening(HLTVBaseModel):
    opening_kills_per_round: Optional[float]
    opening_deaths_per_round: Optional[float]
    opening_attempts_percentage: Optional[float]
    opening_success_percentage: Optional[float]
    win_after_opening_kill_percentage: Optional[float]
    attacks_per_round: Optional[float]


class PlayerStatsClutching(HLTVBaseModel):
    clutch_points_per_round: Optional[float]
    last_alive_percentage: Optional[float]
    _1v1_win_percentage: Optional[float]
    time_alive_per_round: Optional[float]
    saves_per_round_loss_percentage: Optional[float]


class PlayerStatsSniping(HLTVBaseModel):
    sniper_kills_per_round: Optional[float]
    sniper_kills_percentage: Optional[float]
    rounds_with_sniper_kills_percentage: Optional[float]
    sniper_multi_kill_rounds: Optional[float]
    sniper_opening_kills_per_round: Optional[float]


class PlayerStatsUtility(HLTVBaseModel):
    utility_damage_per_round: Optional[float]
    utility_kills_per_100_rounds: Optional[float]
    flashes_thrown_per_round: Optional[float]
    flash_assists_per_round: Optional[float]
    time_opponent_flashed_per_round: Optional[float]

class PlayerStatsRoles(HLTVBaseModel):
    firepower: Optional[PlayerStatsFirepower]
    entrying: Optional[PlayerStatsEntrying]
    trading: Optional[PlayerStatsTrading]
    opening: Optional[PlayerStatsOpening]
    clutching: Optional[PlayerStatsClutching]
    sniping: Optional[PlayerStatsSniping]
    utility: Optional[PlayerStatsUtility]

class PlayerStats(HLTVBaseModel, AuditMixin):
    id: str
    stats: Optional[List[PlayerStatsRoles]] = None


