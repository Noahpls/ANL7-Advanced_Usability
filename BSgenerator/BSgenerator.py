from random import randint
from strings import strings
res = ""

for str in strings:
  x = randint(0, (len(str)-1))
  res += str[x]

print(res)
