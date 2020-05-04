#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 11:38:34 2019

@author: mc
"""
import time

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import datetime
import time

class WhatsappCrawler:

    def __init__(self, users):
        self.users = users
        self.driver = None

    def crawl(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://web.whatsapp.com/")

        input('Enter anything after scanning QR code')

        while True:
            for name in self.users:

                search_box = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]')
                '''insert user name to search and press enter'''
                search_box.send_keys(name)
                search_box.send_keys(Keys.RETURN)


                '''get last access'''
                try:
                    last_access = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/header/div[2]/div[2]/span').text
                except NoSuchElementException:
                    last_access = 'offline'

                if last_access != 'online':
                    status = 'offline'
                else:
                    status = 'online'

                print('User: ', name)
                print('Status:', status)
                print('DT:', datetime.datetime.now())
                print()



                time.sleep(1)



