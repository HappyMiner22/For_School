highest_score = 0
result_f = open('result.txt')

for line in result_f: #file을-> 라인만큼 반복한다. .... // in 뒤가 iterable, for 변수
    if float(line) > highest_score:
        highest_score = float(line)

result_f.close()

print("The highest score was:")
print(highest_score)
