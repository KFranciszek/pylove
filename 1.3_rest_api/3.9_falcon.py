import requests
from pprint import pprint as pp
next_page = 'http://swapi.co/api/starships/?page=1'
pilot_list = []

def bmi(weight, height):
    bmi = weight/(height**2)
    return bmi

while next_page:
    resp = requests.get(next_page).json()
    pilot_list.extend(resp['results'])
    next_page = resp['next']

for i in pilot_list:
    if i['name'] == 'Millennium Falcon':
        pilots = i['pilots']
        for j in pilots:
            temp = requests.get(j).json()
            wt, ht = int(temp['mass']), (int(temp['height'])/100)
            print(temp['name'],round(bmi(wt,ht),2))
