import re
import sys

import requests

from bs4 import BeautifulSoup as bs

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

def get_video_meta(dom):
    content = dom.find('div', class_='yt-lockup-content')
    dtitle = content.find('a', class_='yt-uix-tile-link')
    dchannel = content.find_all('a', href=re.compile("^\/channel\/"))

    if len(dchannel) == 0:
        return None

    cc = False
    container = dom.find('div', class_='yt-lockup-badges')
    if container != None:
        badges = container.find('li', class_='yt-badge-item')
        for badge in badges:
            if badge.text == 'CC':
                cc = True

    return [dtitle.text, dchannel[0].text, dtitle['href'], cc]

def parse(dom):
    # div#results
    # -- ol.item-section
    # -- -- div.yt-lockup.yt-lockup-video
    # -- -- -- div.yt-lockup-badges
    # -- -- -- -- li.yt-badge-item
    # -- -- -- -- -- span.yt-badge == "CC"
    ret = []

    results = dom.find('div', id='results')
    isection = results.find('ol', class_='item-section')
    videos = isection.select('div.yt-lockup.yt-lockup-video')

    ret = list(map(get_video_meta, videos))

    return [v for v in ret if v is not None]

def links(link):
    req = requests.get(link)
    page = req.text
    soup = bs(page, 'html.parser')

    return parse(soup)
