# HomeWork about API (smartest superHero) by Igor Golovin

import requests
# import json
from pprint import pprint
base_url_cdn = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api"
base_url = "https://akabab.github.io/superhero-api/api"

myHeroesID = {}
def getSmartestSuperHerobyID(lstIDs = []):
    myHeroesID = {}
    for id in lstIDs:
        resp = requests.get(base_url_cdn + "/id/"+str(id)+".json")
        name = resp.json().get('biography',{}).get("fullName", '')
        # myHeroesID[resp.json().get('biography',{}).get("fullName", '')] = resp.json().get('powerstats',{}).get("intelligence", 0)
        myHeroesID[resp.json().get("name", '')] = resp.json().get('powerstats', {}).get(
        "intelligence", 0)
    pprint(myHeroesID)
    res = next(iter(dict(sorted(myHeroesID.items(), key=lambda item:  item[1], reverse=True))))
    return res

myHeroes = {
    "Hulk": 0,
    "Captain America": 0,
    "Thanos": 0
}

def getSmartestSuperHero(heroesDict):
    myHeroes = {}
    resp = requests.get(base_url_cdn + "/all.json")
    for hero in resp.json():
        name = hero.get("name", "")
        if name in heroesDict:
            # intelligence
            myHeroes[name] = hero.get("powerstats", {}).get("intelligence", 0)
    # just a name
    res = next(iter(dict(sorted(myHeroes.items(), reverse=True))))
    return  res
    print(f"res: {res}")

if __name__ == '__main__':
    heroesDict = {
        "Hulk": 0,
        "Captain America": 0,
        "Thanos": 0
    }

    heroesList = [1,2,3]
    print("let's start!")
    print()
    print(f"smartest hero from dict: {getSmartestSuperHero(heroesDict)}")
    print(f"smartest hero by IDs: {getSmartestSuperHerobyID(heroesList)}")
    print(f"Done.")
