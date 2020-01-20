from selenium import webdriver
import time
import threading
import pyautogui
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


keys = {
    'siteurl': 'http://192.168.1.1/index.cgi',
    'admin': 'admin',
    'password': '5d526ae03701'

}


def order(k, ligaDesliga):
    # tela de login
    ligaDesliga = ligaDesliga
    driver.maximize_window()
    driver.get(k['siteurl'])
    time.sleep(1)
    print('pegando login e senha')
    try:
        driver.find_element_by_xpath(
            '//*[@id="username"]').send_keys(k["admin"])
    except:
        print('não consegui encontrar o login')
    else:
        print('consegui encontrar o login, indo pra senha')
    try:

        driver.find_element_by_xpath(
            '//*[@id="password"]').send_keys(k["password"])
    except:
        print('não consegui encontrar o senha')
    else:
        print('consegui encontrar o senha, clicando ok')

    try:
        driver.find_element_by_xpath('//*[@id="btn"]').click()
    except:
        print('n consegui clicar')
    else:
        print('clicado...')

    time.sleep(1)
    print("Clicando no SETUP/WIRELESS SETTINGS/BASIC SETTINGS/ENABLE/APPLY")

    if ligaDesliga == 0:
        xy = [[55, 202], [83, 246], [528, 251],
              [461, 340], [515, 402], [1142, 168]]

    else:
        xy = [[55, 202], [83, 246], [528, 251],
              [461, 340], [511, 635], [1142, 168]]

    try:
        for count, ele in enumerate(xy):
            pyautogui.moveTo(xy[count][0], xy[count][1], .15)
            print(xy[count][0], xy[count][1])
            print('click!')
            pyautogui.click()

    except:
        print('passou com ressalvas')


if __name__ == "__main__":
    ligaDesliga = 1
    while True:
        driver = webdriver.Chrome('chromedriver')
        if ligaDesliga == 0:
            ligaDesliga = 1
        else:
            ligaDesliga = 0
        order(keys, ligaDesliga)
        # criar uma contagem de minutos
        print('reiniciando em 2 horas')

        if ligaDesliga == 0:
            input('Aperte Enter pra Ligar')
        else:
            input('Aperte Enter pra Desligar')
