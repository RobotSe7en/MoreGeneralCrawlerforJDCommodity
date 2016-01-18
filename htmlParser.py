'''
Created on 2016年1月17日

@author: wangpeng
'''
#coding=utf8=

from bs4 import BeautifulSoup
import re,urllib
from builtins import str, input
import json


class htmlParser(object):
    
    
    def getNewUrl(self, pageUrl, soup):
        newUrls = set()
        
        # /list.html?cat=9987%2C653%2C655&page=2&JL=6_0_0
        links = soup.find_all('a', class_='pn-next',href=re.compile(r"/list.html\?cat=652,12345,12347&page=\d+\&go=0&JL=6_0_0"))
        # print(links)
        for link in links:
            newUrl = link['href']
            newFullUrl = urllib.parse.urljoin(pageUrl,newUrl)
            newUrls.add(newFullUrl)
        return newUrls
        
    
    
    def getNewData(self, pageUrl, soup):
        resData = {}
        
#         while True:
        try:
            # 获取商品列表的子树<li>...</li>
            commodityNameTemp = soup.find_all('li',class_='gl-item')
                
            # 对每一个商品进行遍历，获得对应商品名称、data-sku、价格
            count = 1
            for li in commodityNameTemp:
                # print(li.find('div',class_='j-sku-item').get('data-sku'),'\n')
                name = li.find('div',class_='p-name').find('em').get_text()
                resData['Name'+str(count)] = name
                sku = li.find('div',class_='j-sku-item').get('data-sku')
                resData['Sku'+str(count)] = sku
                temp = BeautifulSoup(urllib.request.urlopen('http://p.3.cn/prices/get?skuid=J_'+sku).read(),'lxml',from_encoding='utf-8')
                price = json.loads(temp.find('p').get_text())
                resData['Price'+str(count)] = price[0]['p']
                count = count + 1
        except:
            return resData
            
        return resData
    
    
    def parse(self,pageUrl,pageCont):
        if pageUrl is None or pageCont is None:
            return
        soup = BeautifulSoup(pageCont,'lxml',from_encoding='utf-8')
        newUrl = self.getNewUrl(pageUrl,soup)
        newData = self.getNewData(pageUrl,soup)
        return newUrl,newData
        
    
    



