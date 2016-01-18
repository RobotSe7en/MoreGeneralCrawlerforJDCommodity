'''
Created on 2016年1月17日

@author: wangpeng
'''
#coding=utf8=
import xlwt
from openpyxl import Workbook

class crawlerOutput(object):
    
    def __init__(self):
        self.datas = []
        
    def collectData(self,data):
        if data is None:
            return
        self.datas.append(data)

    
    def outPutHtml(self):
        fout = open('outPutofJDPhone.txt','w',encoding='UTF-8')
        wb = xlwt.Workbook(encoding='ascii')
        ws = wb.add_sheet('Sheet1')
        wb1 = Workbook()
        ws1 = wb1.active
        count = 1
        ws.write(count-1,0,'编号')
        ws.write(count-1,1,'名称')
        ws.write(count-1,2,'价格')
        ws1['A'+str(count)] = '编号'
        ws1['B'+str(count)] = '名称'
        ws1['C'+str(count)] = '价格'
        for data in self.datas:
            for i in range(1,int(len(data)/3+1)):
                count = count + 1
                ws.write(count-1,0,data['Sku'+str(i)])
                ws.write(count-1,1,data['Name'+str(i)])
                ws.write(count-1,2,data['Price'+str(i)])
                ws1['A'+str(count)] = data['Sku'+str(i)]
                ws1['B'+str(count)] = data['Name'+str(i)]
                ws1['c'+str(count)] = data['Price'+str(i)]
                # print(data['Name'+str(i)],data['Price'+str(i)])
                fout.writelines(data['Name'+str(i)]+'---->')
                fout.writelines(data['Price'+str(i)]+'\n')
        wb.save('PriceofSmartRing.xls')
        wb1.save('PriceofSmartRing.xlsx')
        fout.close()
    
    
    
    



