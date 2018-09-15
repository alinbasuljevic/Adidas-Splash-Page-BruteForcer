from bs4 import BeautifulSoup as bs
import requests
import time, threading
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


task_count = input('Enter number of tasks: ')

print ('Starting', + int(task_count), 'tasks...')

def main():
    s = requests.Session()
    url = 'https://www.adidas.com/yeezy'
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko), Chrome/68.0.3440.106 Safari/537.36',
               'upgrade-insecure-requests':'1',
               'dnt':'1'}
    splash_page = s.get(url, headers=headers)
    soup = bs(splash_page.text, 'lxml')
    status_checker = True
    while status_checker:
        if 'WAITING' in soup.text:
            print ('Waiting in Splash...')
            time.sleep(2)
            pass
        else:
            print ('Past Splash! Opening Chrome Instance!')
            chrome_options = Options()
            chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            driver = webdriver.Chrome(chrome_options=chrome_options)
            driver.get('https://www.adidas.com')
            cookies = driver.get_cookies()
            for cookie in cookies:
                s.cookies.set(cookie['name'], cookie['value'])
            driver.get('https://www.adidas.com/yeezy')
            break



for i in range(int(task_count)):
    t = threading.Thread(target=main)
    time.sleep(3)
    t.start()

