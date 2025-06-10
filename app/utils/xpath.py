
class Players:
    class Profile:
        URL = "//link[@rel='canonical']//@href"
        NICKNAME = "//h1[@class='playerNickname']/text()"
        NAME = "//div[@class='playerRealname']/text()"
        AGE = "//div[@class='playerInfoRow playerAge']//span[@itemprop='text']/text()"
        NATIONALITY = "//div[@class='playerRealname']//img/@alt"
        RATING = "//div[@class='player-stat']//span[@class='statsVal']//p/text()"
        CURRENT_TEAM = "//div[@class='playerInfoRow playerTeam']//span[@itemprop='text']//a/text()"
        CURRENT_TEAM_URL = "//div[@class= 'playerInfoRow playerTeam']//a/@href"
        IMAGE_URL = "//img[@class = 'bodyshot-img']/@src"
        SOCIAL_MEDIA = "//div[@class = 'socialMediaButtons']//a/@href"

    class Search:
        FOUND = "//text()"
        BASE = "//table[@class='table'][.//td[@class='table-header'][contains(text(), 'Player')]]"
        RESULTS = BASE + "/tbody/tr[not(td[@class='table-header'])]"
        NAME = RESULTS + "/td/a/text()"
        URL = RESULTS +"/td/a/@href"
        NATIONALITY = RESULTS + "//img/@alt"

    class teamAchievements:
        ROWS = "//table[contains(@class, 'achievement-table')]//tr[contains(@class, 'team')]"
        PLACEMENT = ".//div[contains(@class, 'achievement')]/text()"
        TEAM_NAME = ".//td[contains(@class, 'team-name-cell')]//span[@class='team-name']/text()"
        TEAM_URL = ".//td[contains(@class, 'team-name-cell')]//a/@href"
        TOURNAMENT_NAME = ".//td[contains(@class, 'tournament-name-cell')]/a/text()"
        TOURNAMENT_URL = ".//td[contains(@class, 'tournament-name-cell')]/a/@href"
        PLAYER_STATS_URL = ".//td[contains(@class, 'stats-button-cell')]/a/@href"
    
    class personalAchievements:
        TOP_20_PLACEMENT = "//div[contains(@class,'playerTop20')]//span[contains(@class, 'top20ListRight')]/a/text()"
        TOP_20_YEAR = "//div[contains(@class,'playerTop20')]//span[contains(@class, 'top20ListRight')]/span/text()"
        TOP_20_ARTICLE_URL = "//div[contains(@class,'playerTop20')]//span[contains(@class, 'top20ListRight')]/a/@href"
        MAJOR_WINNER_COUNT = "//div[contains(@class, 'majorWinner')]/b"
        MAJOR_MVP_COUNT = "//div[contains(@class, 'majorMVP')]/b"
        MVP_WINNER_COUNT = "//div[contains(@class, 'mvp-count')]//text()"
        MVP_WINNER = "//div[contains(@class, 'trophyHolder')]//span[contains(@title, 'MVP')]/@title"
        EVP =  "//div[contains(@id, 'EVPs')]//tr[contains(@class,'trophy-row')]//div[contains(@class,'trophy-event')]/a/text()"
        

    class Trophies: 
        TOURNAMENT_NAME =  "//div[contains(@id, 'Trophies')]//tr[contains(@class, 'trophy-row')]//div[contains(@class, 'trophy-event')]/a/text()"
        TROPHY_IMG_URL = "//div[contains(@id, 'Trophies')]//tr[contains(@class, 'trophy-row')]//div[contains(@class, 'trophy-detail')]/img/@src"
        TOURNAMENT_URL = "//div[contains(@id, 'Trophies')]//tr[contains(@class, 'trophy-row')]//div[contains(@class, 'trophy-event')]/a/@href"
            
    class Stats: 
        #firepower stats
        KILLS_PER_ROUND = "//div[contains(@data-per-round-title, 'Kills per round') and not(contains(@data-per-round-title, 'Kills per round win')) and contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-data')]//text()"
        KILLS_PER_ROUND_WIN ="//div[contains(@data-per-round-title, 'Kills per round win') and contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-data')]//text()"
        DAMAGE_PER_ROUND = "//div[contains(@data-per-round-title, 'Damage per round') and not(contains(@data-per-round-title, 'Damage per round win')) and contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-data')]//text()"
        DAMAGE_PER_ROUND_WIN ="//div[contains(@data-per-round-title, 'Damage per round win') and contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-data')]//text()"
        ROUNDS_WITH_A_KILL_PERCENTAGE= "//div[contains(@data-per-round-title, 'Rounds with a kill') and contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-data')]//text()"
        RATING_1_0 =  "//div[contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-top')][.//div[contains(@class, 'role-stats-title') and contains(text(), 'Rating 1.0')]]//div[contains(@class, 'role-stats-data')]/text()"
        ROUNDS_WITH_MULTI_KILL_PERCENTAGE = "//div[contains(@data-per-round-title, 'Rounds with a multi-kill') and contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-data')]//text()"
        PISTOL_ROUND_RATING = "//div[contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-top')][.//div[contains(@class, 'role-stats-title') and contains(text(), 'Pistol round rating')]]//div[contains(@class, 'role-stats-data')]/text()"
        
        #entrying stats
        SAVED_BY_TEAMMATE_PER_ROUND ="//div[contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-top')][.//div[contains(@class, 'role-stats-title') and contains(text(), 'Saved by teammate per round')]]//div[contains(@class, 'role-stats-data')]/text()"
        TRADED_DEATHS_PER_ROUND = "//div[contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-top')][.//div[contains(@class, 'role-stats-title') and contains(text(), 'Traded deaths per round')]]//div[contains(@class, 'role-stats-data')]/text()"
        TRADED_DEATHS_PERCENTAGE = "//div[contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-top')][.//div[contains(@class, 'role-stats-title') and contains(text(), 'Traded deaths percentage')]]//div[contains(@class, 'role-stats-data')]/text()"
        OPENING_DEATHS_TRADED_PERCENTAGE = "//div[contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-top')][.//div[contains(@class, 'role-stats-title') and contains(text(), 'Opening deaths traded percentage')]]//div[contains(@class, 'role-stats-data')]/text()"
        ASSISTS_PER_ROUND = "//div[contains(@data-per-round-title, 'Assists per round') and contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-data')]//text()"
        SUPPORT_ROUNDS_PERCENTAGE = "//div[contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-top')][.//div[contains(@class, 'role-stats-title') and contains(text(), 'Support rounds')]]//div[contains(@class, 'role-stats-data')]/text()"
        
        #trading stats
        SAVED_TEAMMATE_PER_ROUND = "//div[contains(@data-per-round-title, 'Saved teammate per round') and contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-data')]//text()"
        TRADE_KILLS_PER_ROUND = "//div[contains(@data-per-round-title, 'Trade kills per round') and contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-data')]//text()"
        TRADE_KILLS_PERCENTAGE = "//div[contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-top')][.//div[contains(@class, 'role-stats-title') and contains(text(), 'Trade kills percentage')]]//div[contains(@class, 'role-stats-data')]/text()"
        ASSISTED_KILLS_PERCENTAGE = "//div[contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-top')][.//div[contains(@class, 'role-stats-title') and contains(text(), 'Assisted kills percentage')]]//div[contains(@class, 'role-stats-data')]/text()"
        DAMAGE_PER_KILL = "//div[contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-top')][.//div[contains(@class, 'role-stats-title') and contains(text(), 'Damage per kill')]]//div[contains(@class, 'role-stats-data')]/text()"

        #opening stats
        OPENING_KILLS_PER_ROUND = "//div[contains(@data-per-round-title, 'Opening kills per round') and contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-data')]//text()"
        OPENING_DEATHS_PER_ROUND = "//div[contains(@data-per-round-title, 'Opening deaths per round') and contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-data')]//text()"
        OPENING_ATTEMPTS_PERCENTAGE = "//div[contains(@data-per-round-title, 'Opening attempts') and contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-data')]//text()"
        OPENING_SUCCESS_PERCENTAGE = "//div[contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-top')][.//div[contains(@class, 'role-stats-title') and contains(text(), 'Opening success')]]//div[contains(@class, 'role-stats-data')]/text()"
        WIN_AFTER_OPENING_KILL_PERCENTAGE = "//div[contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-top')][.//div[contains(@class, 'role-stats-title') and contains(text(), 'Win% after opening kill')]]//div[contains(@class, 'role-stats-data')]/text()"
        ATTACKS_PER_ROUND = "//div[contains(@data-per-round-title, 'Attacks per round') and contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-data')]//text()"

        #clutching stats
        CLUTCH_POINTS_PER_ROUND = "//div[contains(@data-per-round-title, 'Clutch points per round') and contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-data')]//text()"
        LAST_ALIVE_PERCENTAGE = "//div[contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-top')][.//div[contains(@class, 'role-stats-title') and contains(text(), 'Last alive percentage')]]//div[contains(@class, 'role-stats-data')]/text()"
        _1v1_WIN_PERCENTAGE = "//div[contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-top')][.//div[contains(@class, 'role-stats-title') and contains(text(), '1on1 win percentage')]]//div[contains(@class, 'role-stats-data')]/text()"
        TIME_ALIVE_PER_ROUND = "//div[contains(@data-per-round-title, 'Time alive per round') and contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-data')]//text()"
        SAVES_PER_ROUND_LOSS_PERCENTAGE = "//div[contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-top')][.//div[contains(@class, 'role-stats-title') and contains(text(), 'Saves per round loss')]]//div[contains(@class, 'role-stats-data')]/text()"

        #sniping stats
        SNIPER_KILLS_PER_ROUND = "//div[contains(@data-per-round-title, 'Sniper kills per round') and contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-data')]//text()"
        SNIPER_KILLS_PERCENTAGE = "//div[contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-top')][.//div[contains(@class, 'role-stats-title') and contains(text(), 'Sniper kills percentage')]]//div[contains(@class, 'role-stats-data')]/text()"
        ROUNDS_WITH_SNIPER_KILLS_PERCENTAGE = "//div[contains(@data-per-round-title, 'Rounds with sniper kills percentage') and contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-data')]//text()"
        SNIPER_MULTI_KILL_ROUNDS = "//div[contains(@data-per-round-title, 'Sniper multi-kill rounds') and contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-data')]//text()"
        SNIPER_OPENING_KILLS_PER_ROUND = "//div[contains(@data-per-round-title, 'Sniper opening kills per round') and contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-data')]//text()"

        #utility stats
        UTILITY_DAMAGE_PER_ROUND = "//div[contains(@data-per-round-title, 'Utility damage per round') and contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-data')]//text()"
        UTILITY_KILLS_PER_100_ROUNDS = "//div[contains(@data-per-round-title, 'Utility kills per 100 rounds') and contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-data')]//text()"
        FLASHES_THROWN_PER_ROUND = "//div[contains(@data-per-round-title, 'Flashes thrown per round') and contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-data')]//text()"
        FLASH_ASSISTS_PER_ROUND = "//div[contains(@data-per-round-title, 'Flash assists per round') and contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-data')]//text()"
        TIME_OPPONENT_FLASHED_PER_ROUND ="//div[contains(@data-per-round-title, 'Time opponent flashed per round') and contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-data')]//text()"

    class careerStats:
        TOTAL_KILLS = "//div[contains(@class, 'stats-row')]/span[contains(text(),'Total kills')]/following-sibling::span[1]/text()"
        HEADSHOT_PERCENTAGE = "//div[contains(@class, 'stats-row')]/span[contains(text(),'Headshot %')]/following-sibling::span[1]/text()"
        TOTAL_DEATHS = "//div[contains(@class, 'stats-row')]/span[contains(text(),'Total deaths')]/following-sibling::span[1]/text()"
        KD_RATIO = "//div[contains(@class, 'stats-row')]/span[contains(text(),'K/D Ratio')]/following-sibling::span[1]/text()"
        DAMAGE_PER_ROUND = "//div[contains(@class, 'stats-row')]/span[contains(text(),'Damage / Round')]/following-sibling::span[1]/text()"
        GRENADE_DMG_PER_ROUND = "//div[contains(@class, 'stats-row')]/span[contains(text(),'Grenade dmg / Round')]/following-sibling::span[1]/text()"
        MAPS_PLAYED = "//div[contains(@class, 'stats-row')]/span[contains(text(),'Maps played')]/following-sibling::span[1]/text()"
        ROUNDS_PLAYED = "//div[contains(@class, 'stats-row')]/span[contains(text(),'Rounds played')]/following-sibling::span[1]/text()"
        KILLS_PER_ROUND = "//div[contains(@class, 'stats-row')]/span[contains(text(),'Kills / round')]/following-sibling::span[1]/text()"
        ASSISTS_PER_ROUND = "//div[contains(@class, 'stats-row')]/span[contains(text(),'Assists / round')]/following-sibling::span[1]/text()"
        DEATHS_PER_ROUND = "//div[contains(@class, 'stats-row')]/span[contains(text(),'Deaths / round')]/following-sibling::span[1]/text()"
        SAVED_BY_TEAMMATE_PER_ROUND = "//div[contains(@class, 'stats-row')]/span[contains(text(),'Saved by teammate / round')]/following-sibling::span[1]/text()"
        SAVED_TEAMMATES_PER_ROUND = "//div[contains(@class, 'stats-row')]/span[contains(text(),'Saved teammates / round')]/following-sibling::span[1]/text()"
        RATING1_0 = "//div[contains(@class, 'stats-row')]/span[contains(text(),'Rating 1.0')]/following-sibling::span[1]/text()"

class Events:
    class EventProfile:
        EVENT_URL = "//div[@class ='event-hub']//a/@href"
        EVENT_NAME = "//h1[contains(@class, 'event-hub-title')]/text()"
        TEAM_COUNT = "//td[contains(@class,'teamsNumber')]/text()"
        EVENT_START_DATE = "//th[contains(text(), 'Start date')]/parent::tr/td/span/text()"
        EVENT_END_DATE = "//th[contains(text(), 'End date')]/parent::tr/td/span/span/text()"
        PRIZE_POOL = "//td[contains(@class, 'prizepool')]/text()"
        PRIZE_CLUB_SHARE = "//th[contains(text(), 'Club share')]/following-sibling::td"
        PRIZE_PLAYER_SHARE = "//th[contains(text(), 'Player share')]/following-sibling::td"
        EVENT_LOCATION = "//td[contains(@class,'location')]//span/text()"
        LOCATION_FLAG_URL = "//td[contains(@class,'location')]//img/@src"
        MAP_POOL =  "//div[@class = 'map-pool-map-name']"

        #MVP
        EVENT_MVP_NICKNAME = "//div[@class= 'player-name']//a//span[@class = 'bold']/text()"
        EVENT_MVP_URL = "//div[@class= 'player-name']//a/@href"
        
        #EVPS
        EVENT_EVPS_NICKNAME = "//a[contains(@class, 'evp-wrapper')]//div[@class= 'evp-name-top']/text()"
        EVENT_EVPS_URL = "//a[contains(@class, 'evp-wrapper')]/@href"

        #teams       
        TEAM_NAME = "//div[@class='team-name']//div[@class='text-container']//div[@class='text']/text()"
        TEAM_URL = "//div[@class='team-name']//a/@href"
        TEAM_PLACEMENT = "//div[contains(@class,'placement')]/div[not(@class)]/text()"
        
    class EventTeamStats:

        #'teams attended' box
        TEAM_LINEUP = "//div[contains(@class, 'team-box') and .//a[contains(@href, '/team/{team_id}/')]]//div[contains(@class, 'lineup-box')]//div[contains(@class , 'flag-align player')]//text()"
        TEAM_PLAYER_URL = "//div[contains(@class, 'team-box') and .//a[contains(@href, '/team/{team_id}/')]]//div[contains(@class, 'lineup-box')]//div[contains(@class , 'flag-align player')]//a/@href"
        TEAM_COACH = "//div[contains(@class, 'team-box') and .//a[contains(@href, '/team/{team_id}/')]]//div[contains(@class,'coach-text')]/parent::div//div[contains(@class, 'flag-align player')]//text()"
        TEAM_COACH_URL = "//div[contains(@class, 'team-box') and .//a[contains(@href, '/team/{team_id}/')]]//div[contains(@class,'coach-text')]/parent::div//div[contains(@class, 'flag-align player')]//a/@href"
        QUALIFY_METHOD = "//div[contains(@class, 'team-box') and .//a[contains(@href, '/team/{team_id}/')]]//div[contains(@class, 'sub-text event-text')]//text()"
        
        
        #'vrs ranking' box
        VRS_DATE = "//th[contains(text(), 'VRS date')]/following-sibling::td//span"
        VRS_POINTS_BEFORE_EVENT = "//tbody[contains(@class, 'vrs-before')][.//a[contains(@href, '/team/{team_id}/')]]//tr[.//a[contains(@href, '/team/{team_id}/')]]/td[@class='vrs-points']/div[@class='start-only']//div"
        VRS_POINTS_AFTER_EVENT = "//tbody[contains(@class, 'vrs-after')][.//a[contains(@href, '/team/{team_id}/')]]//tr[.//a[contains(@href, '/team/{team_id}/')]]/td[@class='vrs-points']/div[@class='start-only']//div"
        VRS_POINTS_ACQUIRED = "//tbody[contains(@class, 'vrs-after')][.//a[contains(@href, '/team/{team_id}/')]]//tr[.//a[contains(@href, '/team/{team_id}/')]]/td[@class='vrs-points']/div[@class='finished-only']//div[contains(@class, 'finished-points')]"
        VRS_PLACEMENT_BEFORE_EVENT = "//tbody[contains(@class, 'vrs-before')][.//a[contains(@href, '/team/{team_id}/')]]//tr[.//a[contains(@href, '/team/{team_id}/')]]/td[@class = 'vrs-placements']//div[@class = 'start-only']//div[@class = 'vrs-placement-btn']"
        VRS_PLACEMENT_AFTER_EVENT = "//tbody[contains(@class, 'vrs-after')][.//a[contains(@href, '/team/{team_id}/')]]//tr[.//a[contains(@href, '/team/{team_id}/')]]/td[@class = 'vrs-placements']//div[@class = 'start-only']//div[@class = 'vrs-placement-btn']"

        
        #'prize distribution' box
        PRIZE = "//div[@class = 'team' and .//a[contains(@href,'/team/{team_id}/')]]/following-sibling::div[@class='prize']/text()"
        PRIZE_CLUB_SHARE = "//div[@class = 'team' and .//a[contains(@href,'/team/{team_id}/')]]/following-sibling::div[@class='prize club-share']/text()"
        TEAM_PLACEMENT  = "//div[@class = 'team' and .//a[contains(@href,'/team/{team_id}/')]]/following-sibling::div[not(@class)]/text()"
        
class Teams:
    class TeamProfile:
        NAME = "//h1[contains(@class, 'profile-team-name')]"
        LOGO_URL = "//div[contains(@class, 'profile-team-logo-container')]//img/@srcset"
        PLAYER_NICKNAME= "//div[contains(@class, 'playerFlagName')]//span[contains(@class,'text-ellipsis bold')]/text()"
        PLAYER_URL = "//div[contains(@class,'teamProfile')]//a[contains(@class, 'col-custom')]/@href"
        COACH_NICKNAME = "//div[@class = 'profile-team-stat'][.//b[contains(text(), 'Coach')]]//span[@class = 'bold a-default']"
        COACH_URL = "//div[@class = 'profile-team-stat'][.//b[contains(text(), 'Coach')]]//a/@href"
        SOCIAL_MEDIA ="//div[@class = 'socialMediaButtons']//a/@href"
        VALVE_RANKING = "//div[@class = 'regional-wrapper']//b[contains(text(), 'Valve ranking')]/following::a[1]/text()"
        WORLD_RANKING = "//div[@class = 'profile-team-stat']//b[contains(text(), 'World ranking')]/following::a[1]/text()"
        WEEKS_IN_TOP30_FOR_CORE = "//div[@class = 'profile-team-stat'][.//b[contains(text(), 'Weeks in top30 for core')]]//span[@class = 'right']"
        AVERAGE_PLAYER_AGE = "//div[@class = 'profile-team-stat'][.//b[contains(text(), 'Average player age')]]//span[@class = 'right']"

    class Achievements:
        PLACEMENT = "//tr[@class='team']//div[contains(@class, 'achievement')][.//i[contains(@class, 'fa-trophy')]]/text()"
        TOURNAMENT_NAME = ".//td[contains(@class, 'tournament-name-cell')]/a/text()"
        TOURNAMENT_URL = ".//td[contains(@class, 'tournament-name-cell')]/a/@href"

    class UpcomingMatches:
        UPCOMING_MATCHES_ROW = "//h2[@class = 'standard-headline' and contains(text(), 'Upcoming matches')]/following::table[@class = 'table-container match-table'][1]"
        MATCH_URL = "//td[@class = 'matchpage-button-cell']//a/@href"
        
        EVENT_NAME = "//div[@class = 'timeAndEvent']//div[@class = 'event text-ellipsis']//a/text()"
        EVENT_URL = "//div[@class = 'timeAndEvent']//div[@class = 'event text-ellipsis']//a/@href"
        MATCH_DATE = "//div[@class = 'timeAndEvent']//div[@class = 'date']/text()"
        MATCH_HOUR = "//div[@class = 'timeAndEvent']//div[@class = 'time']/text()"
        RIVAL_TEAM_NAME = "//div[@class = 'team2-gradient']//a//div[@class = 'teamName']/text()"
        RIVAL_TEAM_URL = "//div[@class = 'team-flex '][2]//a[@class = 'team-name team-2']/@href"
        MATCH_TYPE = "//div[@class = 'standard-box veto-box']//div[@class = 'padding preformatted-text']/text()"

        
class Ranking:
    class Stats:
        TEAM_ROW = "//div[contains(@class, 'ranked-team')]"
        RANKING_DATE = "//div[@class = 'regional-ranking-header-text']"
        TEAM_NAME = ".//div[contains(@class , 'teamLine sectionTeamPlayers')]//span[@class = 'name']/text()"
        TEAM_URL = ".//div[@class = 'more']//a[@class = 'moreLink']/@href"
        TEAM_LOGO_URL = ".//div[@class='bg-holder']//span[@class='team-logo']/img[not(contains(@class, 'day-only')) and (contains(@class, 'night-only') or not(@class))][1]/@src"
        PLAYER_ROW = ".//table[@class='lineup']//td[@class='player-holder']"
        PLAYER_NICKNAME = ".//div[@class='nick']/text()"
        PLAYER_PICTURE_URL = ".//img[@class='playerPicture']/@src"
        PLAYER_URL = ".//a[@class='pointer']/@href"
        PLAYER_NATIONALITY = ".//div[@class='nick']/img/@alt"
        HLTV_POINTS = ".//div[@class = 'bg-holder']//div[contains(@class , 'teamLine sectionTeamPlayers')]//span[@class = 'points']/text()[1]"
        PLACEMENT = ".//div[@class = 'bg-holder']//div[@class = 'ranking-header']//span[@class = 'position wide-position']/text()"
