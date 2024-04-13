# Author: Sergey Chekhonin
# 2024 No rights protected :)


from bs4 import BeautifulSoup as BSoup

from utils.toolkit import get_response_bypassed, get_html_f

tartget_url = 'https://www.list.am/category/56/222?n=1&cmtype=1&price2=234567&crc=1&gl=2'

html = get_html_f('Parser/src/fixtures/index.html')

parsed_html = BSoup(html,'lxml')
paginator = parsed_html.find('div',class_='dlf').find_all('a') # return bs4.element.ResultSet
for a in paginator:
    print(a.string)
    # вытаскивает данные из тега как string
    # 2
    # 3
    # 4
    # 5
    # 6
    # 7
    # hadjorde >
    # создать условие чтобы числовые значения с ссылко
    # сохранял и выбирал ту ссылку значение которой максимальное!

print(type(paginator))
