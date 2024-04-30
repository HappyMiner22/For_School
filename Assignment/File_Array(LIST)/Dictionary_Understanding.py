'''line = "101;Johnny 'wave-boy' Jones;USA;8.32;Fish;21"

s = {}
(s['id'], s['name'], s['country'], s['average'], s['board'], s['age']) = line.split(";")

print("ID: " + s['id'])
print("Name: " + s['name'])
print("Country: " + s['country'])
print("Average: " + s['average'])
print("Board type: " + s['board'])
print("Age: " + s['age'])'''

'''def find_details(id2find):
    surfers_f = open("surfing_data.csv")
    for eachline in surfers_f:
        s = {}
        (s['id'], s['name'], s['country'], s['average'], s['board'], s['age']) = eachline.split(";")

        if id2find == int(s['id']):
            surfers_f.close()
            return(s)
    surfers_f.close()
    return({})

find_id = int(input("Enter the surfer's id to find surfer's info: "))
surfer = find_details(find_id)

if surfer:
    print("ID: " + surfer['id'])
    print("Name: " + surfer['name'])
    print("Country: " + surfer['country'])
    print("Average: " + surfer['average'])
    print("Board type: " + surfer['board'])
    print("Age: " + surfer['age'])
'''
'''import sqlite3

import sqlite3
def find_details(id2find):
    db = sqlite3.connect("surfersDB.sdb")
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    cursor.execute("select * from surfers")
    rows = cursor.fetchall()

    for row in rows:
        if row['id'] == id2find:
            s = {}
            s['id'] = str(row['id'])
            s['name'] = row['name']
            s['country'] = row['country']
            s['average'] = str(row['average'])
            s['board'] = row['board']
            s['age'] = str(row['age'])
            cursor.close()
            return (s)
        cursor.close()
        return ({})

lookup_id = int(input("Enter the Surfer: "))
surfer = find_details(lookup_id)

if surfer:
    print("ID: " + surfer['id'])
    print("Name: " + surfer['name'])
    print("Country: " + surfer['country'])
    print("Average: " + surfer['average'])
    print("Board type: " + surfer['board'])
    print("Age: " + surfer['age'])'''


'''f = open("Imagine.txt")
text = f.read()

def wCount(word):
    wlist = []
    for wd in text.split():
        wlist.append(wd)

    cnt = wlist.count(word)
    return cnt

w = "imagine"
n = wCount(w)

print(w + ':' + str(n))'''

'''scores = {}

result_f = open("result.txt")

for line in result_f:
    (name, score) = line.split()
    scores[score] = name

result_f.close()


print("Top Scores were : ")
for each_score in scores.keys():
    print('Surfer ' + scores[each_score] + ' scored ' + each_score)

print("Top Scores were : ")
for each_score in sorted(scores.keys(), reverse=True):
    print('Surfer ' + scores[each_score] + ' scored ' + each_score)'''

'''def find_id(id):
    info_f = open("surfing_data.csv")
    for line in info_f:
        s = {}
        (s['id'], s['name'], s['region'], s['average'], s['board'], s['age']) = line.split(';')
        if id == int(s['id']):
            info_f.close()
            return s

    info_f.close()
    return {}

find = int(input("Surfer ID? : "))
surfer = find_id(find)

if surfer:
    print("ID:              " + surfer['id'])
    print("Name:            " + surfer['name'])
    print("Region:          " + surfer['region'])
    print("Average:         " + surfer['average'])
    print("Board type:      " + surfer['board'])
    print("Age:             " + surfer['age'])'''

'''def wCount(word):
    wlist = []
    for wd in text.split(): # text 변수의 내용을 공백문자로 분리한 리스트
        wlist.append(wd)
    cnt = wlist.count(word) # 리스트의 count 메서드 적용
    return cnt

f = open("Imagine.txt")

text = f.read() # 파일 읽기, 전역 변수(global variable) -> 전역변수의 선언 위치는 함수를 정의한 위치보다 아래여도 괜찮음. //
w = "Imagine"
n = wCount(w) # 함수 호출
print(w + ":" + str(n)) # 단어 개수 출력
'''

def exam():
    f = open("Imagine.txt")
    d = {}
    for line in f:
        ws = line.split()
        for t in ws:
            if t not in d:
                d[t] = 1
            else:
                d[t] += 1
    return d
s = exam()

for w, c in sorted(s.items()):
    print(w, c)
    