#Desafio da aula 04
from selenium.webdriver import Firefox
from time import sleep
from urllib.parse import urlparse
from pprint import pprint # preatty print


browser = Firefox()

browser.get('https://selenium.dunossauro.live/aula_04.html')

#clicando no exercício 3
sleep(0.5)
main_ex03 = browser.find_element_by_tag_name('main')
exercicio03 = main_ex03.find_elements_by_tag_name('a')[2]
exercicio03.click()

#pagina inicial e clicando no comece por aqui
sleep(0.4)
main = browser.find_element_by_tag_name('main')
clique_aqui = main.find_element_by_tag_name('a')
clique_aqui.click()

#clicando na resposta errada
sleep(0.5)
def get_respostas(browser, elemento):
    element = browser.find_element_by_tag_name(elemento)
    ancoras = element.find_elements_by_tag_name('a')
    for ancora in ancoras:

        if ancora.get_attribute('attr') == 'errado':
            ancora.click()
            break

escolhas = get_respostas(browser, 'main')

#pagina 2
sleep(2)
browser.refresh() #se nao der refresh nao aparece nada
sleep(5)
def get_respostas(browser, elemento):
    element = browser.find_element_by_tag_name(elemento)
    ancoras = element.find_elements_by_tag_name('a')
    for ancora in ancoras:

        if ancora.get_attribute('attr') == 'certo':
            ancora.click()
            break

escolhas = get_respostas(browser, 'main')

#Você está na pagina 3
sleep(2)
url_parseada = urlparse(browser.current_url)
url_pars2 = url_parseada.path[1:] #o path sem a barra
elementos = browser.find_elements_by_tag_name('a')

for elemento in elementos:
    if elemento.text == url_pars2:
        elemento_certo = elemento.get_attribute('href')
        browser.get(elemento_certo)
        break
#Dar o refresh pro diabão
sleep(2)
browser.refresh()
#vencemos!
sleep(2)
browser.quit()
