from selenium.webdriver import Firefox
from time import sleep
from pprint import pprint # preatty print

browser = Firefox()

browser.get('http://selenium.dunossauro.live/aula_04.html')

#função que pega todos os links no elemento que vc queira e retorna como um dicionario
def get_links(browser, elemento):
    resultado = {}
    element = browser.find_element_by_tag_name(elemento)
    ancoras = element.find_elements_by_tag_name('a')
    for ancora in ancoras:
        resultado[ancora.text] = ancora.get_attribute('href')

    return resultado

#Pegar todas as aulas
sleep(2)
aulas = get_links(browser, 'aside')

pprint(aulas)


#Pegar todos os links de exercicios e acessando o exercicio 3
exercicios = get_links(browser, 'main')
pprint(exercicios)
#acessando o array exercicios na posição desejada que é a exercicio 3
browser.get(exercicios['Exercício 3'])

#pagina inicial e clicando no comece por aqui
main = browser.find_element_by_tag_name('main')
clique_aqui = main.find_element_by_tag_name('a')
pprint(clique_aqui.text)
clique_aqui.click()
