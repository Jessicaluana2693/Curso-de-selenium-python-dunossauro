from selenium.webdriver import Firefox
from urllib.parse import urlparse
browser = Firefox()

browser.get('http://selenium.dunossauro.live/aula_04_a.html')

url_mais_atual = urlparse(browser.current_url)

# SEMPRE ATIVAR O AMBIENTE VENV
# venv\Scripts\activate

# NAVEGANDO NO browser
# browser.get('site-a') - vai ser direcionado para o site a
# browser.back() - vai voltar uma "página" atras, como se fosse o btn voltar
# browser.forward() - vai uma página a frente, como se fosse o btn avançar
#browser.refresh() - da um F5 na página
#browser.title - retorna o título da página atual

#VERIFICANDO SE ESTAMOS NA URL CORRETA
#EXEMPLO
# from urllib.parse import urlparse - Parse analisa texto
# urlparse(browser.current_url) - Esta é uma biblioteca nativa python
# scheme = protocolo usado ex: https
# netloc = url de fato ex: site.com
# path = diretorio mais atual em que a url esta ex: aula_04_a
