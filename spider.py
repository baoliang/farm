#-*- encoding:utf-8 -*-
import gevent
import pymongo
from gevent import monkey
monkey.patch_all()
from gevent.pool import Pool
import requests
from bs4 import BeautifulSoup
import sys  
from PyQt4.QtGui import *  
from PyQt4.QtCore import *  
from PyQt4.QtWebKit import *  
db = pymongo.Connection('127.0.0.1', 27017)['test']  
class Render(QWebPage):  
  def __init__(self, url):  
    self.app = QApplication(sys.argv)  
    QWebPage.__init__(self)  
    self.loadFinished.connect(self._loadFinished)  
    self.mainFrame().load(QUrl(url))  
    self.app.exec_()  
  
  def _loadFinished(self, result):  
    self.frame = self.mainFrame()  
    self.app.quit()  


p = Pool(2)#设置并发数为2
def down(url):
    soup = BeautifulSoup(requests.get(url).content)
    data_l =  soup.find_all(id='productRows')[0].find_all('table')[1].find_all('tr')
    for i, data in enumerate(data_l):
        print i
        if len(data.find_all('td')) != 0:
            if data.find_all('td')[0].a:
                href = data.find_all('td')[0].a.get('href')
                if href:
                    r = Render("http://www.abcam.com/"+href)  
                    html = r.frame.toHtml() 
                    html = unicode(html)
                    soup_detail = BeautifulSoup(html).find_all('table')[0].find_all('tr')[1].find_all('td')
                    item =  [td.string for td in soup_detail[:3]]

                    dic = {"id": item[0], "unit": item[1].split(" ")[1], 'price': item[2]}
                    print dic
                    db["yaopin"].insert(dic)
                        
urls = ['http://www.abcam.com/index.html?pageconfig=catalog_byproducttype&intProductTypeID=1']
for url in urls:
    p.spawn(down, url)

p.join()