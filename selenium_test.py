from selenium import webdriver
from selenium import common
from selenium.webdriver.common.keys import Keys
import logging as lg

def google():
    chrome = webdriver.Chrome('./chromedriver.exe')
    chrome.maximize_window()
    chrome.get('https://google.com')
    search = chrome.find_elements_by_css_selector('#lst-ib')
    search[0].send_keys('potatoes\n')
    input('...')
    chrome.quit()


def stuff():
    lg.basicConfig(level=lg.INFO,
                   style='{',
                   format='{message}'
                   )
    stuff = 'http://stuff.co.nz'
    chrome = webdriver.Chrome('./chromedriver.exe')
    chrome.maximize_window()
    chrome.get(stuff)
    chrome.find_elements_by_css_selector('#nav > ul > li:nth-child(1) > a')[0].click()
    popular = []
    for i in range(1,11):
        try:
            popular.append(chrome.find_elements_by_css_selector('#viewed > p:nth-child({})'.format(i)))
            #lg.debug('working...')
        except common.exceptions.NoSuchElementException:
            pass
    for i in popular:
        print('[{}] - {}'.format(popular.index(i) + 1, i[0].text))
    popular[int(input('>')) - 1][0].click()
    input('...')
    chrome.quit()

if __name__ == '__main__':
    stuff()
    
