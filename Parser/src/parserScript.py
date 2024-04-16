#!/usr/local/bin/python3

# Author: Sergey Chekhonin
# 2024 No rights protected :)


from bs4 import BeautifulSoup as BSoup

from utils.toolkit import get_response_bypassed, get_html_f,\
    get_page_dict, remove_non_numeric_keys , get_high_link

tartget_url = 'https://www.list.am/category/56/222?n=1&cmtype=1&price2=234567&crc=1&gl=2'


### PAR-31 Creating funcionality for paginator max page
### searching

# 1. Load markup from fixture; 
html = get_html_f('fixtures/index.html')

# 2. Return soup object to parse new dict
soup_html = BSoup(html,'lxml')

# 3. Get dict with numerik keys to links
new_list = get_page_dict(soup_html)

# 4. Clean out alphabethic keys from list
remove_non_numeric_keys(new_list)

# 5. get the highest link from page
print(get_high_link(new_list))
