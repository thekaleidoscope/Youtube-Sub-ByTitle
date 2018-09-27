from bs4 import BeautifulSoup as bs
import requests
import sys

r = requests.get("https://www.youtube.com/results?search_query=" +
                 "+".join(sys.argv[1].split(" ")))
page = r.text
soup = bs(page, 'html.parser')
vids = soup.findAll('a', attrs={'class': 'yt-uix-tile-link'})
videolist = []
for v in vids:
    tmp = 'https://www.youtube.com' + v['href']
    videolist.append(tmp)
print(videolist[0])
