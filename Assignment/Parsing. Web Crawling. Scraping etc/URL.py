from urllib import request, parse
import time

token = 'ZQAAATFXQnYDw3tWLLIKpCwb9kA4-pbq2g72kN8YbjT0NWW-VGiJ7gHinTS0Gy7TixKC98VUwywNMqWRJ-RzylkbAYK_Hi7t6u3RpRWusIPJLWFU'
Band_Key = 'AAAb_r1pS-hNWRGcdKO6aa9t'


def Send_Message(bk, content, do_push=False):  # 인수에 여러가지를 넣을 수 있음
    url = 'https://openapi.band.us/v2.2/band/post/create'
    req = request.Request(url)
    data = {'access_token': token, 'band_key': bk, 'content': content, 'do_push': do_push}
    post_data = parse.urlencode(data).encode('utf8')
    res = request.urlopen(req, post_data)
    print(f'전송 완료, {content}')


def get_price():
    page = request.urlopen("http://cs.sch.ac.kr/prices-loyalty.py")
    text = page.read().decode("utf8")
    where = text.find('>$')
    start_of_price = where + 2
    end_of_price = start_of_price + 4
    return float(text[start_of_price:end_of_price])


price_now = input("Do you want to see the price now (Y/N)? ")
if price_now == 'Y':
    msg = "Buy now!, price $" + str(get_price())
    Send_Message(Band_Key, msg)

else:
    price = 99.99
    while price > 4.74:
        time.sleep(2)
        price = get_price()

    msg = "Buy!, price $" + str(price)
    Send_Message(Band_Key, msg)
#내일 할 공부 : 무엇이 라이브러리고 무엇이 모듈인지, 둘의 차이점은 무엇인지 확실하게 알아두기.
