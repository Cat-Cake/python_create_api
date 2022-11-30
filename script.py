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


get_games()

# @app.route("/games/")
# def hello_world():
#     return "<p>Hello, World!</p>"
