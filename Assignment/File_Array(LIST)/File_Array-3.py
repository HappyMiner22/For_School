scores = []
result_f = open("result.txt")

for line in result_f:
    (name, score) = line.split()
    scores.append(float(score))

result_f.close()

scores.sort()
scores.reverse()

print(scores[0])
print(scores[1])
print(scores[2])