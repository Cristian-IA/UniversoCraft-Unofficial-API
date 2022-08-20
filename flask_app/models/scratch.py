import requests
from bs4 import BeautifulSoup
class Scratch:
    def __init__(self, name, url):
        self.name = name
        self.url = url

    @classmethod
    def get_user(cls,user):
        URL = "https://stats.universocraft.com/stats.php?player=" + user
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        player = {}
        results = soup.find_all("div", class_="game")
        attr = soup.find('div', class_='player-status').find_all('p')
        last_time = soup.find('div', class_='player-description').find_all('p')
        player['nick'] = soup.find('h1').get_text()
        player['rank'] = attr[0].get_text()
        if len(attr) > 1:
            player['isPremium'] = 'Si'
        else:
            player['isPremium'] = 'No'
        player['last_time'] = last_time[0].get_text() + ' ' + last_time[1].get_text()
        player['head'] = soup.find('div','player-image-border').find('img')['src']
        player['skin'] = soup.find('div','player-image-border').find('img')['src'].replace('head','skin')

        string = ''
        for result in results:
            string += result.find("h2", class_="game-header-title").get_text() + ': \n'
            titles = result.find_all("p", class_="game-stat-title")
            values = result.find_all("p", class_="game-stat-count")
            for i in range(len(titles)):
                string += titles[i].get_text() + ':' + values[i].get_text() + '\n'
                

        return player 


    
        


    
