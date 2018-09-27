from bs4 import BeautifulSoup as bs
import requests
import sys


def link(link):

    r = requests.get(link)
    page = r.text
    soup = bs(page, 'html.parser')
    vids = soup.findAll('a', attrs={'class': 'yt-uix-tile-link'})
    videolist = []
    for v in vids:
        tmp = 'https://www.youtube.com' + v['href']
        videolist.append(tmp)

    return videolist[0]
