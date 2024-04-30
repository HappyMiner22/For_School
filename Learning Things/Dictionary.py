print("컴퓨터 공학과 20244049 변호석")
'''scores = []
names = []

result_f = open("result.txt")

for line in result_f:
    (name, score) = line.split()
    scores.append(float(score))
    names.append(name)

result_f.close()

scores.sort()
scores.reverse()

names.sort()
names.reverse()

print("The Highest Score was :")

print(names[0]+' with ' +str(scores[0]))
print(names[1]+' with '+str(scores[1]))
print(names[2]+' with '+str(scores[2]))'''

scores = {}
result_f = open("result.txt")

for line in result_f:
    (name, score) = line.split()
    scores[score] = name

result_f.close()

print("The Top Score was : ")
for each_score in sorted(scores.keys(), reverse=True):
    print('Surfer ' + scores[each_score] + ' scored ' + each_score)