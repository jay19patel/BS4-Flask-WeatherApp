
import requests
from bs4 import BeautifulSoup

url ="https://weather.com/en-DM/weather/tenday/l/28d595bc7ffad1010c416552a79bd576c69a3443d730c27784a0911b2e078f98"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


class Weather:
    def location():
        location = soup.find('span',{'class':'LocationPageTitle--PresentationName--1AMA6'}).text
        return location

    def info():    
        info = soup.find('p',{'class':'DailyContent--narrative--3Ti6_'}).text
        return info
    def temp():
        temp = soup.find('span',{'class':'DailyContent--temp--1s3a7'}).text
        return temp

    def humidity():
        humidiy = soup.find('span',{'class':'DetailsTable--value--2YD0-'}).text
        return humidiy
    
    def Moonrise():
        Moonrise = soup.find(attrs={'data-testid':'MoonriseTime'}).text
        return Moonrise


    def allDays():    

        mydaydata =[]         
        for wed in soup.find_all('details',{'class':'DaypartDetails--DayPartDetail--2XOOV Disclosure--themeList--1Dz21'}):
            day = wed.find('h3',{'class':'DetailsSummary--daypartName--kbngc'}).text
            temp = wed.find('span',{'class':'DetailsSummary--highTempValue--3PjlX'}).text
            mydaydata.append([day,temp])
        return mydaydata