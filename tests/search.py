from app.services.players.search import HLTVPlayerSearch

def test_search():
    search = HLTVPlayerSearch(query="s1mple")  # Substitua pelo nome de um jogador conhecido
    result = search.search_players()
    print(result)

if __name__ == "__main__":
    test_search()