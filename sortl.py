from spiderA import SpiderHTML
from getUrl import SearchUrl
from collections import Counter

from bs4 import BeautifulSoup
import requests
import os

# 目标url
# url = 'https://movie.douban.com/subject/26683290/'
class SortList(object):
    def __init__(self, searchName):
        self.searchName = searchName
    def start(self):

        ss = SearchUrl(self.searchName)
        url = ss.start()

        class doubanDetil(SpiderHTML):
            def __init__(self, url):
                self.url = url

            def start(self):
                # print(url)
                # print(self.url)
                soup = self.getUrl(self.url)
                titles = soup.select('.recommendations-bd dt a')
                findUrls = [x['href'] for x in titles]

                aboutImg = soup.select('.recommendations-bd dt a img')
                imgNames = [x['alt'] for x in aboutImg]
                imgURLs = [x['src'] for x in aboutImg]
                # print(findUrl,imgName,imgURL)
                chapterInfo = []
                for imgName, imgURL, findUrl in zip(imgNames, imgURLs, findUrls):
                    listof = {
                        'name': imgName,
                        'img': imgURL,
                        'url': findUrl
                    }
                    chapterInfo.append(listof)

                return chapterInfo

        spider = doubanDetil(url)
        f = spider.start()
        allM = []
        for x in f:
            # print('---------' + x['name'])
            subspider = doubanDetil(x['url'])
            ff = subspider.start()
            #     print(ff)

            for y in ff:
                allM.append(y['name'])

        c = Counter(allM)
        sss = c.most_common(1000)
        return sss
