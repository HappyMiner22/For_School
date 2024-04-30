text = """
Soonchunhyang University
Department of Computer Science and Engineering
"""
# 파일 쓰기
f = open()
f.write(text)
f.close()
# 파일 읽기
f = open("test.txt")
lines = f.read()
print(lines.upper())