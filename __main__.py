import sys
sys.path.append('..')
import json
import pyrebase
from Classes.UserList import UserList
from Classes.WhatsappCrawler import WhatsappCrawler
from Classes.DBManager import DBManager
import time
if __name__ == '__main__':
    dbm = DBManager('./Configurations/')


    # ulc = UserList('./Data/ListOfContacts.txt')
    # users = ulc.get_users()
    #
    # crawler = WhatsappCrawler(users)
    # crawler.crawl()

    obs1 = {"Mamma":{"TS": 1}}
    obs2 = {"Mamma": {"TS": 2}}
    obs3 = {"Deborah Ciculi": {"TS": 1}}
    obs4 = {"Deborah Ciculi": {"TS": 2}}

    dbm.insert_observation(obs1)
    dbm.insert_observation(obs2)
    dbm.insert_observation(obs3)
    dbm.insert_observation(obs4)
