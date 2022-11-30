from xml.etree import ElementTree
import requests
from flask import Flask
import xmltodict, json
from bs4 import BeautifulSoup
import json
import xml

app = Flask(__name__)
app = Flask('yourapplication')
app = Flask(__name__.split('.')[0])

# tree = ElementTree.parse('./megtrinity.xml')
# root = tree.getroot()

# for item in root:
#     print(item[0].text)


with open('./megtrinity.xml', 'r') as f:
    file = f.read() 

    soup = BeautifulSoup(file, 'xml')
    names = soup.find_all('name')


@app.route("/games")
def get_games():
    listGame = []
    for item in soup.find_all('item'):
        title = item.find('name').string
        stats = item.find('stats')
        minplayer = stats.get('minplayers')
        maxplayer = stats.get('maxplayers')

        dictGame = {
            'id': item.get('objectid'),
            'title': item.find('name').string,
            'thumbnail': item.find('thumbnail').string,
            'date': item.find('yearpublished').string,
            'players': stats.get('maxplayers') if stats.get('minplayers') == stats.get('maxplayers') else stats.get('minplayers') + ' - ' + stats.get('maxplayers'),
            'playtime': stats.get('maxplaytime') if stats.get('minplaytime') == stats.get('maxplaytime') else stats.get('minplaytime') + ' - ' + stats.get('maxplayers')
        }

        listGame.append(dictGame)
    return listGame


gameid = get_games()
print(gameid[0]['id'])

# params = {'game_id': item.get('objectid')}
# response = requests.get('http://127.0.0.1:5000/',
#             params=params)

@app.route("/games/<string:game_id>", methods = ['GET'])
def game_by_id(game_id):
    for item in soup.find_all('item'):
        title = item.find('name').string
        stats = item.find('stats')
        minplayer = stats.get('minplayers')
        maxplayer = stats.get('maxplayers')
        lstcategories = ""
        for category in item.findall('boardgamecategory'):
            lstcategories = lstcategories + ' , ' + category.string
        lstcategories = lstcategories[1:]
        dictGame = {
            'id': item.get('objectid'),
            'title': item.find('name').string,
            'caterogies': lstcategories.string,
            'thumbnail': item.find('thumbnail').string,
            'image': item.find('image').string,
            'date': item.find('yearpublished').string,
            'players': stats.get('maxplayers') if stats.get('minplayers') == stats.get('maxplayers') else stats.get('minplayers') + ' - ' + stats.get('maxplayers'),
            'playtime': stats.get('maxplaytime') if stats.get('minplaytime') == stats.get('maxplaytime') else stats.get('minplaytime') + ' - ' + stats.get('maxplayers')
        }

        if dictGame['id'] == game_id:
            return dictGame
