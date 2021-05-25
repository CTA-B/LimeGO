import pandas as pd
import urllib
import json
import selenium
import xlsxwriter
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from getpass import getpass
from convtools import conversion as c
from pprint import pprint
import time

#https://go.lime-go.com//395012/Organization/pase100011/
#BRAND DELIVERY LOGO
print("  ____  _____            _   _ _____    _____  ______ _      _______      ________ _______     __")
print(" |  _ \|  __ \     /\   | \ | |  __ \  |  __ \|  ____| |    |_   _\ \    / /  ____|  __ \ \   / /")
print(" | |_) | |__) |   /  \  |  \| | |  | | | |  | | |__  | |      | |  \ \  / /| |__  | |__) \ \_/ / ")
print(" |  _ <|  _  /   / /\ \ | . ` | |  | | | |  | |  __| | |      | |   \ \/ / |  __| |  _  / \   /  ")
print(" | |_) | | \ \  / ____ \| |\  | |__| | | |__| | |____| |____ _| |_   \  /  | |____| | \ \  | |   ")
print(" |____/|_|  \_\/_/    \_\_| \_|_____/  |_____/|______|______|_____|   \/   |______|_|  \_\ |_|   ")
print("")
#https://api-iam.intercom.io/messenger/web/ping
#Meddelande
print(' © 2021 - Brand Delivery - Alla rättigheter tillhör Sellotonin AB')
print(" Skapat av: Tobias Helling")
print(" https://go.lime-go.com")

url = "https://go.lime-go.com/"
 
#Logga in på Lime
 
#username = input(" E-postadress: ")
#password = getpass(" Lösenord: ")

username = "Benjamin@sellotonin.com"
password = "sello"

#Välj ringlista
 
#rlista = input("Ringlista ID: ")

class LimeGO: 
 
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe')
 
    def login(self):
        
        self.driver.get(url)
        time.sleep(3)
 
        user_ = self.driver.find_element_by_class_name('UserName').send_keys(username)
        time.sleep(2)
 
        _pass = self.driver.find_element_by_class_name('Password').send_keys(password)
        time.sleep(2)
 
        self.driver.find_element_by_id('logonbutton').click()
        time.sleep(5)
 
    def find_company(self):
        
        baseLink = "https://go.lime-go.com/395012/Organization/pase"

        lst=[] 
        for k in range(10011,20011,1):
            link = baseLink + str(k)
            self.driver.get(link)

            #Convert what I want
            converter = c.list_comp({
                "f_namn": c.item("data", "name"),
                "org_nr": c.item("data", "organizationNumber"),
                "Phone Number": c.item("data", "centralPhoneNumber", "normalized")
            }).gen_converter()  # install "black" to see formatted sources
            
            res = self.driver.find_element_by_tag_name("pre").text
            lst.append(json.loads(res))
                
            prepared_data=lst
            xd = pd.json_normalize(prepared_data)
            xd.to_excel('10k.xlsx', index=False)
lime = LimeGO()
lime.login()
lime.find_company()