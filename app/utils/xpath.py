
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

    class Achievements:
        ROWS = "//table[contains(@class, 'achievement-table')]//tr[contains(@class, 'team')]"
        PLACEMENT = ".//div[contains(@class, 'achievement')]/text()"
        TEAM_NAME = ".//td[contains(@class, 'team-name-cell')]//span[@class='team-name']/text()"
        TEAM_URL = ".//td[contains(@class, 'team-name-cell')]//a/@href"
        TOURNAMENT_NAME = ".//td[contains(@class, 'tournament-name-cell')]/a/text()"
        TOURNAMENT_URL = ".//td[contains(@class, 'tournament-name-cell')]/a/@href"
        PLAYER_STATS_URL = ".//td[contains(@class, 'stats-button-cell')]/a/@href"