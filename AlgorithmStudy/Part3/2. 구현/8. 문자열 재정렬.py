import sys

data = sys.stdin.readline().strip()
text = []
num = 0
for i in data:
    if i.isalpha():
        text.append(i)
    else:
        num += int(i)

text.sort()
res = ''.join(text)
print(res + str(num))
