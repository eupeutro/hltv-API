
class Players:
    class Profile:
        URL = "//link[@rel='canonical']//@href"
        NICKNAME = "//h1[@class='playerNickname']/text()"
        NAME = "//div[@class='playerRealname']/text()"
        AGE = "//div[@class='playerInfoRow playerAge']//span[@itemprop='text']/text()"
        NATIONALITY = "//div[@class='playerRealname']//img[@alt]"
        CURRENT_TEAM = "//div[@class='playerInfoRow playerTeam']//span[@itemprop='text']/text()"
        CURRENT_TEAM_URL = "//div[@class= 'playerInfoRow playerTeam']//a/@href"
        RATING = "//div[@class='player-stat']//span[@class='statsVal']//p/text()"