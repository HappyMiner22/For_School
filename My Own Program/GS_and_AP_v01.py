#다음에 추가할 기능

def GS_SUM(f, r, n):
    result = float(f * (r**n - 1) / (r-1))
    return result

def GS():
    general = input("등비수열의 일반항을 입력하시오 (예시 : 2 * 3 ** (n-1)) : ")
    n = 1
    first_term = eval(general)
    print(f'{general}의 첫번째 항은 {first_term}.')

    after_star = general.split('*')[1].strip()
    r = eval(after_star)
    ratio = int(r)
    print(f'{general}의 공비는 {ratio}.')

    n = int(input('몇 번째 항을 구하는지 입력하시오 : '))
    last = eval(general)
    print(f'{general}의 {n}번째 항은 {last}.')

    k = input("등비수열의 합을 구하시겠습니까? : ")
    if k == 'y':
        result = GS_SUM(first_term, ratio, n)
        print(f'등비수열{general}의 {n}항까지의 합은 {result}.')
        return result


def AP():
    general = input("등차수열의 일반항을 입력하시오 : ")
    n = 1
    first_term = eval(general)
    print(f'{general}의 첫번째 항은 {first_term}.')

    n = int(input('몇 번째 항을 구하는지 입력하시오 : '))
    last = eval(general)
    print(f'{general}의 {n}번째 항은 {last}.')

    a = input("지금까지 나온 값을 갖고 등차수열의 합을 구하시겠습니까? : ")

    if a == 'y':
        result = float(n * (first_term + last) / 2)
        print(f'등차수열{general}의 {n}항까지의 합은 {result}.')
        return result

question = input("등차수열의 첫째항, 마지막 항을 구하시겠습니까? y/n : ")

if question == 'y':
    print(AP())
elif question == 'n':
    print(GS())