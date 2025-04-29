import cloudscraper
from bs4 import BeautifulSoup

url = "https://www.hltv.org/player/7998/-"

# Cria uma sessão que lida com Cloudflare
scraper = cloudscraper.create_scraper()

response = scraper.get(url)

# Verifique se a resposta foi bem-sucedida
if response.status_code == 200:
    print("Página carregada com sucesso!")
    
    # Cria o objeto BeautifulSoup para parsear o HTML
    soup = BeautifulSoup(response.text, 'lxml')
    
    # Exemplo: extrair o nome do jogador
    player_name = soup.find('h1', class_='playerNickname')  # Troque pela classe real do nome
    
    if player_name:
        print("Nome do jogador:", player_name.text)
    else:
        print("Nome do jogador não encontrado.")
else:
    print("Erro ao acessar a página. Status code:", response.status_code)