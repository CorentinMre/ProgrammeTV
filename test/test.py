import requests
from bs4 import BeautifulSoup

nowUrl = "https://www.programme-tv.net/programme/en-ce-moment.html"
nightUrl = "https://www.programme-tv.net/programme/toutes-les-chaines"
yesterdayUrl = "https://www.programme-tv.net/programme/toutes-les-chaines/2022-07-07/"

def getProgramme(url:str = nowUrl):

    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    programme = []
    index = 0
    for i in range (32):
        info = soup.find_all("img", {"class": "content-lightMode"})
        programme.append({"channelNumber" : soup.find_all("p", {"class": "gridRow-cardsChannelNumber"})[i].text,
                    "channelLogo" : info[i].get("data-src") if info[i].get("data-src") != None else info[i].get("src"),
                    "channelName" : soup.find_all("img", {"class": "content-lightMode"})[i].get("alt"),
                    "now": {
                        "startingHour" : soup.find_all("p", {"class": "mainBroadcastCard-startingHour"})[index].text.replace(" ", "").replace("\n", ""),
                        "title" : soup.find_all("h3", {"class": "mainBroadcastCard-title"})[index].text.replace("  ", "").replace("\n", ""),
                        "duration" : soup.find_all("span", {"class": "mainBroadcastCard-durationContent"})[index].text.replace(" ", "").replace("\n", ""),
                        "type" : soup.find_all("p", {"class": "mainBroadcastCard-format"})[index].text.replace("  ", "").replace("\n", ""),
                    },
                    "later": {
                        "startingHour" : soup.find_all("p", {"class": "mainBroadcastCard-startingHour"})[index+1].text.replace(" ", "").replace("\n", ""),
                        "title" : soup.find_all("h3", {"class": "mainBroadcastCard-title"})[index+1].text.replace("  ", "").replace("\n", ""),
                        "duration" : soup.find_all("span", {"class": "mainBroadcastCard-durationContent"})[index+1].text.replace(" ", "").replace("\n", ""),
                        "type" : soup.find_all("p", {"class": "mainBroadcastCard-format"})[index+1].text.replace("  ", "").replace("\n", ""),
                    }
                    })
        index += 2
    return programme



print(getProgramme())
