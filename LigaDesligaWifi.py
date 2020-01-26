from selenium import webdriver
import time
import threading
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


keys = {
    'siteurl': 'http://192.168.1.1/login.cgi',
    'siteurl2': 'http://192.168.1.1/wlbasic.cgi',
    'admin': 'admin',
    'password': '5d526ae03701'

}


def order(k):

    # BUSCANDO DADOS E ENVIANDO PARA TELA DE LOGIN
    on_off = ''
    driver.get(k['siteurl'])
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
    driver.get(k['siteurl2'])


# CHECK E UNCHECK INPUT RADIO DO WIFI

    print("Clicando no SETUP/WIRELESS SETTINGS/BASIC SETTINGS/ENABLE/APPLY")
    try:
        x = driver.find_element_by_name('wlanDisabled')
        x.click()
    except:
        print('não consegui encontrar o botão de check')


# VERIFICAÇÃO SE O ROTEADOR ESTÁ LIGADO OU DESLIGADO
    try:
        driver.find_element_by_xpath(
            '//*[@id="configwlan"]/table[1]/tbody/tr[1]/td[2]/input')
    except:
        on_off = 'Ligar'

    else:
        on_off = 'Desligar'

# FINALIZAÇÃO DO PROGRAMA CLICANDO NO ALERT OK INFORMANDO AO USUÁRIO
    try:
        driver.find_element_by_xpath('//*[@id="manDdnsApply"]').click()
    except:
        print('n consegui clicar')

    try:
        time.sleep(1)
        alert = driver.switch_to_alert()
    except:
        print('n consegui achar o alert')
    else:
        alert.accept()
        driver.close()

    print(f'aperte enter para {on_off}')


if __name__ == "__main__":

    while True:
        driver = webdriver.Chrome('chromedriver')
        order(keys)
        # criar uma contagem de minutos
        input('')
