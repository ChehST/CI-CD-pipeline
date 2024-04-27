#!/usr/local/bin/python3

# Author: Sergey Chekhonin
# 2024 No rights protected :)


from bs4 import BeautifulSoup as BSoup

from .const import BASE_URL
from .const.codes import CATHEGORY_LOCK
from .utils.toolkit import count_ads_at_page, get_last_page,counter_ads_at_page_request

last_page = get_last_page()
target_url_cathPart = BASE_URL + CATHEGORY_LOCK
target_url_reqPart = "?n=1&cmtype=1&price2=200000&crc=1&gl=2"
ads_last_page = counter_ads_at_page_request(target_url_cathPart + str(last_page) +target_url_reqPart)

total_ads = (last_page * 100) + ads_last_page
print(f"There are '{total_ads}' rent ads by owners up to 200000 dram in Yerevan area")
