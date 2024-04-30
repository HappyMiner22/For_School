
'''fruits = ["Cherry", "Apple", "Raspberry"]

for fruit in fruits: # for 뒤에 변수를 새로 선언할 수도 있다. / for 변수 in 반복 가능한 개체 -> format
    print(fruit)
'''

#메커니즘 -> iterable 불러오고, 변수에 저장하고 반복. 변수에 모든 값이 저장되는 것은 아니다. 출력값을 볼 수 있듯이.. 리스트형 변수의 마지막만 저장되어 출력되는 것을 볼 수 있다.

'''combs = []

for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y :
            combs.append((x, y))

print(combs)'''

for x in range(9):
    print()
    for y in range(5):
        if x >= y:
            print("*", end="")

for i in range(4):
    print()
    for j in range(4):
        if j >= i:
            print('*', end="")