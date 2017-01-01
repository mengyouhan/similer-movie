from bs4 import BeautifulSoup
import requests,os

class SpiderHTML(object):
    # 打开页面
    def getUrl(self,url):
        wb_data = requests.get(url)
        return BeautifulSoup(wb_data.text, 'lxml')


    # 传入图片地址，文件名，保存单张图片
    def saveImg(self, imageURL, fileName):
        img = requests.get(imageURL)
        f = open(fileName, 'wb')  ##写入多媒体文件必须要 b 这个参数！！必须要！！
        f.write(img.content)  ##多媒体文件要是用conctent哦！
        f.close()



# os.makedirs('/Users/user/Desktop/aaa')
# os.chdir('/Users/user/Desktop/aaa')
# imageURL = 'https://img1.doubanio.com/lpic/s27284878.jpg'
# Path = '/Users/user/Desktop'
# fileName = os.path.join(Path,'aaaaa.jpg')
#
# simg = SpiderHTML()
# simg.saveImg(imageURL,fileName)
