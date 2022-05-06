from selenium.webdriver import Firefox
from time import sleep
url = 'https://curso-python-selenium.netlify.app/aula_03.html'

browser = Firefox()

browser.get(url)

sleep(2)

a = browser.find_element_by_tag_name('a')

# print(f'texto de a: {a.text}')
# print(f'texto de p: {p.text}')

for click in range(0,11):
    pzes = browser.find_elements_by_tag_name('p')
    a.click()
    print(f'Valor do ultimo p: {pzes[-1].text} valor de click: {click}')
    print(f'Os valores são iguais {pzes[-1].text == str(click)}')


browser.quit()
