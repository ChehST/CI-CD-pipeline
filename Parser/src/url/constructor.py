""" URL construcor that manage to do manipulations
on url address
"""


from ..const import *

target_url_cathPart = BASE_URL + CATHEGORY_LOCK
target_url_reqPart = "?n=1&cmtype=1&price2=200000&crc=1&gl=2"

def build_path(page_num):
    target_url_cathPart = BASE_URL + CATHEGORY_LOCK
    target_url_reqPart = "?n=1&cmtype=1&price2=200000&crc=1&gl=2"
    req_url = target_url_cathPart + page_num +target_url_reqPart
    return req_url

# PAR-23
#      BASE_URL   |   CATHEGORY    |  page_paginator  |  request  |  Filter...
# https://www.list.am/category/   56   /1   ?   n=0 & cmtype=1 & price2=234567 & crc=1 & gl=2
# https://www.list.am/category/56/1?n=0&cmtype=1&price2=234567&crc=1&gl=2
# notice!: we can swap filters themself

