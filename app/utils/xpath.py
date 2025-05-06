
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
            

