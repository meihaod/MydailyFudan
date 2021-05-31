#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   Fred Mei

@License :   (C) Copyright 2013-2017, com.mhd

@Contact :   {19210720004@fudan.edu.cn}

@Software:   PyCharm

@File    :   dailyFudan

@Time    :   2021/5/30 10:27 下午

@Desc    :实现平安复旦的自动化提交，每次提交的信息为上次的信息

'''
import os
import requests
from bs4 import BeautifulSoup
import json
import time

url_login = "https://uis.fudan.edu.cn/authserver/login"
url_dailyFudan = "https://zlapp.fudan.edu.cn/site/ncov/fudanDaily"
url_get_info= 'https://zlapp.fudan.edu.cn/ncov/wap/fudan/get-info'
url_save= 'https://zlapp.fudan.edu.cn/ncov/wap/fudan/save'
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"

class Login_Fudan:

    def __init__(self, username, pwd):
        self.username = username
        self.pwd = pwd
        self.header = {'User-Agent':UA}
        self.data = {'username':self.username,
                     'password':self.pwd
                     }
        self.session=requests.session()

    def logIn(self):
        '''
        登陆复旦uis系统
        :return:
        '''
        response = self.session.get(url_login)
        soup = BeautifulSoup(response.text,'lxml')

        # 筛选出所有post请求体需要的参数（token）
        def has_name_and_value(tag):
            return tag.has_attr('name') and tag.has_attr('value') and 'username' not in tag['name'] and 'password' not \
                   in tag['name']

        for item in soup.body.form.find_all(has_name_and_value):
            self.data.update(zip([item['name']],[item['value']]))
        #登陆账号
        self.session.post(url_login,data=self.data)

    def check(self):
        '''
        判断今日是否已经提交平安复旦
        :return:
        '''
        # 获取上次提交的信息并用json接收，转为字典处理
        self.last_info = json.loads(self.session.get(url_get_info).text)
        self.cur_info = self.last_info['d']['info']
        today = time.strftime('%Y%m%d')
        if self.cur_info['date'] == today:
            print("今日已提交")
            return True
        else:
            print("今日未提交")
            return False

    def checkin(self):
        '''
        提交平安复旦
        :return:
        '''
        old_info  = self.last_info['d']['oldInfo']
        area = old_info['area']
        province = old_info['province']
        city = old_info['city']
        self.cur_info.update(
            {
                'area': area,
                'province':province,
                'city':city,
                'ismoved':'0'
            }
        )
        self.session.post(url_save, data=self.cur_info)
        print('正在提交平安复旦')





if __name__ == '__main__':
    username = os.getenv("USERNAME")
    pwd = os.getenv("PASSWORD")
    login=Login_Fudan(username,pwd)
    login.logIn()
    if not login.check():
       login.checkin()
       login.check()
