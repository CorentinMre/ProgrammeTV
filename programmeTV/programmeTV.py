import requests
from bs4 import BeautifulSoup
#import json
from datetime import datetime


class ProgrammeTV:
    def __init__(self) -> None:
        self.heure = datetime.now().strftime("%d-%m-%Y")

        self.url = f"https://webnext.fr/templates/webnext_exclusive/views/includes/epg_cache/programme-tv-rss_{self.heure}.xml"

        self.req = requests.get(self.url)

        self.programme = self._getProgramme()
        

    def _getProgramme(self):

        soup = BeautifulSoup(self.req.text, "html.parser")
        channels = soup.find_all("item")
        
        programme = []
        for channel in channels:
            channelName = channel.find("title").text.split(" | ")

            if programme == [] or programme[-1]["channelName"] != channelName[0]:
                programme.append({"channelName" : channelName[0] , 'emmision':[{"emissionHour" : channelName[1], "emissionName" : channelName[2], "description" : channel.find("description").text}]})
            else:
                programme[-1]["emmision"].append({"emissionHour" : channelName[1], "emissionName" : channelName[2], "description" : channel.find("description").text})

        #with open("data.json", "w") as outfile:
        #    json.dump(programme, outfile)

        return programme

if __name__ == "__main__":

    programme = ProgrammeTV()

    print(programme.programme)
