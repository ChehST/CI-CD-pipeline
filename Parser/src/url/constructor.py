""" URL construcor that manage to do manipulations
on url address
"""


from const import *


# PAR-23
#      BASE_URL   |   CATHEGORY    |  page_paginator  |  request  |  Filter...
# https://www.list.am/category/   56   /1   ?   n=0 & cmtype=1 & price2=234567 & crc=1 & gl=2
# https://www.list.am/category/56/1?n=0&cmtype=1&price2=234567&crc=1&gl=2
# notice!: we can swap filters themself

