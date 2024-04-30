from urllib import request
import time

def get_price():
    page = request.urlopen("http://cs.sch.ac.kr/prices-loyalty.py")
    text = page.read().decode("utf8")

    where = text.find('>$')
    sop = where + 2
    eop = sop + 4

    date = text.find("e on")
    sod = date + 16
    eod = sod + 8

    return float(text[sop:eop]), text[sod:eod]

p, d = get_price()

price_now = input("Do you want to see the price now (y/n)? ")
if price_now == 'y':
    print(p)

else:
    p, d = get_price()
    price = 99.99
    while price > 4.74:
        time.sleep(1)
        price = p
    print(p, d)