#Desafio da aula 04
from selenium.webdriver import Firefox
from time import sleep
from pprint import pprint # preatty print

browser = Firefox()

browser.get('https://selenium.dunossauro.live/aula_04.html')

#clicando no exercício 3
sleep(0.5)
main_ex03 = browser.find_element_by_tag_name('main')
exercicio03 = main_ex03.find_elements_by_tag_name('a')[2]
pprint(exercicio03.text)
exercicio03.click()

#pagina inicial e clicando no comece por aqui
sleep(0.4)
main = browser.find_element_by_tag_name('main')
clique_aqui = main.find_element_by_tag_name('a')
pprint(clique_aqui.text)
clique_aqui.click()

#clicando na resposta errada
sleep(0.5)
def get_respostas(browser, elemento):
    element = browser.find_element_by_tag_name(elemento)
    ancoras = element.find_elements_by_tag_name('a')
    for ancora in ancoras:

        if ancora.get_attribute('attr') == 'errado':
            ancora.click()

escolhas = get_respostas(browser, 'main')

#dando o refresh
browser.refresh()

#Escolhendo o título certo
sleep(3)
def get_titulos(browser, elemento):
    element = browser.find_element_by_tag_name(elemento)
    ancoras = element.find_elements_by_tag_name('a')
    for ancora in ancoras:

        if ancora.text == browser.title:
            ancora[0].click()

escolhas = get_titulos(browser, 'main')
