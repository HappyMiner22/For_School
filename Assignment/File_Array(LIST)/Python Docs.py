print("컴퓨터공학과 20244049 변호석")
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

g = [[row[i] for row in matrix] for i in range(4)]

print(g)

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])


print(transposed)

transposed_2 = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed_2.append(transposed_row)

print(transposed_2)

print(list(zip(*matrix)))