import cloudscraper
from bs4 import BeautifulSoup as BSoup
# Add imports here

from const import *

# returns requests Response object. It is able to bypass CFP
def get_response_bypassed(url):
    scraper = cloudscraper.create_scraper()
    try:
        requested_html = scraper.get(url)
        return requested_html
    except:
        print(requested_html.status_code)
        return requested_html.status_code

# Ad counter function. It count ads per 1 page PAR-23
def ad_counter(ads):
    pass

# function that return html code from file
def get_html_f(file):
    with open(file,'r',encoding="utf-8") as html:
        html_plain = html.read()
    return html_plain


# page's link dict 'page num as a key':'link to page'
links = {} # page's link dict

# Return dict with pages and hrefs ; Input bsoup object
def get_page_dict(parsed_page):
    for page in parsed_page.find('div',class_='dlf').find_all('a'):
        page_num = page.string
        page_link = page.get('href')
        # print(page_num, page_link)
        if page_num and page_link:
            links[page_num] = page_link
    return links

# remove non digit key pairs
def remove_non_numeric_keys(dictionary):
    keys_to_remove = [key for key in dictionary.keys() if not key.isdigit()]
    for key in keys_to_remove:
        del dictionary[key]
    return links

# get max values link
def get_highest_link(links):
    remove_non_numeric_keys(links)
    max_key = max(links.keys(), key=lambda x: int(x))
    max_link = links[max_key]

    return max_link

def get_highest_key(links):
    remove_non_numeric_keys(links)
    print
    max_key = max(links.keys(), key=lambda x: int(x))
    return max_key

# Cyclic function that count total pages with ads in the cathegory
def get_last_page():
    previous_last_page = 0
    target_url_cathPart = BASE_URL + CATHEGORY_LOCK
    target_url_reqPart = "?n=1&cmtype=1&price2=234567&crc=1&gl=2"
    page = 1
    print('we start scan from this address:', target_url_cathPart + str(page) + target_url_reqPart)
    url_gen= target_url_cathPart + str(page) + target_url_reqPart

    while True:
        html = get_response_bypassed(url_gen).text
        soup_html = BSoup(html,'lxml')
        get_page_dict(soup_html)
        highest_page = get_highest_key(links)

        if highest_page == previous_last_page:
            break
            
        previous_last_page = highest_page
        url_gen = target_url_cathPart + str(highest_page) + target_url_reqPart
        previous_last_page = highest_page
    
    print('There are: ' + str(highest_page) + ' pages in cathegory')
    return int(highest_page)

### PAR-23 Ads per page counter
def count_ads_at_page():
    counter = 0
    plain_html = get_html_f('src/fixtures/index.html')
    parsed_page = BSoup(plain_html,'lxml') #parse html
    contentr = parsed_page.find(id="contentr") # find wrap for div 'dl'

    if contentr:
        dl_divs = contentr.find_all(class_="dl") # there are 2 divs named 'dl'
        # Пройти по каждому контейнеру dl и найти все ссылки внутри него
        for dl_ad in dl_divs:
            ad_links = dl_ad.find_all('a') # there two dl_ad elements in dl_div

    ad_list = ad_links[:-7] # cut off last 7 elements because these is paginators hrefs
    # 
    for ad in ad_list:
        counter+=1
    return counter

def counter_ads_at_page_request(url):
    counter = 0
    plain_html = get_response_bypassed(url).text
    parsed_page = BSoup(plain_html,'lxml') #parse html
    contentr = parsed_page.find(id="contentr") # find wrap for div 'dl'

    if contentr:
        dl_divs = contentr.find_all(class_="dl") # there are 2 divs named 'dl'
        # Пройти по каждому контейнеру dl и найти все ссылки внутри него
        for dl_ad in dl_divs:
            ad_links = dl_ad.find_all('a') # there two dl_ad elements in dl_div

    ad_list = ad_links[:-7] # cut off last 7 elements because these is paginators hrefs
    # 
    for ad in ad_list:
        counter+=1
    return counter

