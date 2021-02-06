# -*- coding:utf-8 -*-

# 引入相关的包，urllib与bs4，是获取和解析网页最常用的库
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time,os,tkinter
from tkinter import messagebox
import string
from decimal import *

import webbrowser

if __name__ == '__main__':
    print('Bank of China--------GBP Monitor')
    level = float(input("**Set the level you want to monitor:\n"))
    while True:
        # signal.signal(signal.SIGTERM, exit)
        # 打开链接
        html = urlopen("https://www.boc.cn/sourcedb/whpj/")

        # 通过urlopen获得网页对象，将其放入BeautifulSoup中，bsObj存放的目标网页的html文档

        bsObj = BeautifulSoup(html.read(),features="html.parser")
        # print(bsObj.find('div'))
        table_node = bsObj.find_all('table')




        text_0 = table_node[1].find_all('td')

        text_1 = table_node[1].find_all('td', text="英镑")[0]

        #index_0 confirm the row of GBP, because sometimes the oder change on the page
        index_0 = text_0.index(text_1)

        #index 3 means the sold price of the bank
        text = float(table_node[1].find_all('td')[index_0 + 3].get_text())



        num_GB = text


        print('\nCurrent GBP:'+str(num_GB))



        if(num_GB < level):
            #messagebox.showinfo("Check", "GBP is under"+str(level))
            print("ALERT!!! CHECK GBP: UNDER "+str(level))
            Check_Web = int(input("\nEnter 1 for Checking details 0 for continue:"))
            if(Check_Web == 1):
                webbrowser.open_new_tab('https://www.boc.cn/sourcedb/whpj/')
            else:
                print("System pause,press any button to continue")
                os.system("pause")
			
            



        time.sleep(120)








