# HomeWork about API (smartest superHero) by Igor Golovin

import requests
# import json
from pprint import pprint
base_url_cdn = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api"
base_url = "https://akabab.github.io/superhero-api/api"

myHeroesID = {}
def getSmartestSuperHerobyID(lstIDs = []):
#    response = requests.get(base_url_cdn + "/all.json")
    response = requests.get(base_url_cdn + "/all.json")
    for hero in response.json():
        if hero.get("id", 0) in lstIDs:
            myHeroesID[hero.get("name", "")] = hero.get("powerstats",
                                                       {}).get("intelligence", 0)
    # pprint(myHeroesID)
    pprint((sorted(myHeroesID.items(), key=lambda item:
    item[1],  reverse=True)))
    # name (key) and value
    # res = next(iter(dict(sorted(myHeroesID.items(), key=lambda item:
    # item[1], reverse=True)).items()))
    # just a name
    resKey = next(iter(dict(sorted(myHeroesID.items(), key=lambda item:
    item[1], reverse=True))))
    print(resKey)
    # print(f"res: {res}, type: {type(res)}")

myHeroes = {
    "Hulk": 0,
    "Captain America": 0,
    "Thanos": 0
}

def getSmartestSuperHero():
    resp = requests.get(base_url_cdn + "/all.json")
    for hero in resp.json():
        name = hero.get("name", "")
        if name in myHeroes:
            # intelligence
            myHeroes[name] = hero.get("powerstats", {}).get("intelligence", 0)
#    print(myHeroes)
    # name (key) and value
    res = next(iter(dict(sorted(myHeroes.items(), key=lambda item:
    item[1], reverse=True)).items()))
    # just a name
    res = next(iter(dict(sorted(myHeroes.items(), reverse=True))))
    print(f"res: {res}")

if __name__ == '__main__':
    print("let's start!")
    print()
    # getSmartestSuperHerobyID([35, 69, 104, 149])
    getSmartestSuperHerobyID([1,2,3])
    getSmartestSuperHero()
    print(f"Done.")