scores = []
result_f = open("result.txt")

for line in result_f:
    (name, score) = line.split()
    scores.append(float(score))

result_f.close()

scores.sort()

sorted_scores = scores[0], scores[1], scores[2]

f = open("sorted_scores.txt", "w")

for s_s in sorted_scores:
    text = (s_s)

print(s_s)
