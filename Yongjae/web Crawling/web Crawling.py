import selenium
from selenium import webdriver
from time import sleep
import openpyxl
import os

options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options,executable_path=r'C:/Users/82102/Desktop/-algorithm-/Yongjae/web Crawling/chromedriver.exe')
driver.get('https://fcbayern.com/en/matches/statistics')
# driver.get('https://fcbayern.com/en/matches/statistics')


player_list = []
i = 1
for i in range(1, 33):
    player_name = driver.find_element_by_xpath(f'//*[@id="fcb-teaser-container"]/div/div/div[4]/div/div/div/div/div[3]/ul/li[1]/div/div[2]/div[{i}]/div/header/h4').text
    player_list.append(player_name)

j = 1
player_img_list = []
for j in range(1, 33):
    player_img = driver.find_element_by_xpath(f'//*[@id="fcb-teaser-container"]/div/div/div[4]/div/div/div/div/div[3]/ul/li[1]/div/div[2]/div[0={j}]/div/div/div[1]/div/div/img')
    player_img_list.append(player_img)

print(player_img_list)
print(player_list)