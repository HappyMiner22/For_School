import time
import urllib.request

def get_price():
    page = urllib.request.urlopen("http://cs.sch.ac.kr/prices-loyalty.py")
    text = page.read().decode("utf-8")

    where = text.find(">$")
    sop = where + 2
    eop = sop + 4

    date = text.find("e on")
    sod = date + 16
    eod = sod + 8

    return float(text[sop:eop]), text[sod:eod]

val1, val2 = get_price()

emergency_buy = input("Buy Beans Now? (y/n) : ")

if emergency_buy == "y":
    print(val1)

else:
    price = 99.99
    date = val2
    while price > 4.74:
        time.sleep(1)
        val1, val2 = get_price()
        price = val1
    print(price, date)