# Guilherme Junqueira - Simple Crawler

import urllib.request
import re

try:
    url = "http://g1.com.br" #start
    page = urllib.request.urlopen(url)
    html = str(page.read())
    links = re.findall('"((http)s?://.*?)"', html)
except:
    print("Erro start")
crawl = []
crawled = [url]

while True:
    for link in links:
        if link[0] not in crawl:
            print("Novo link: ", link[0])
            crawl.append(link[0])

    for link in crawl:
        if link not in crawled:
            try:
                print("Fazendo crawling: ", link)
                page = urllib.request.urlopen(link)
                html = str(page.read())
                links = re.findall('"((http)s?://.*?)"', html)
                crawled.append(link)
                break
            except:
                print("Erro")
                crawled.append(link)
                break




