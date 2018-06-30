from random import randint
from strings import strings

res = ""

#Iterates through the (9) arrays
for str in strings:
  #Adds a randomly picked string from each array to the result
  x = randint(0, (len(str)-1))
  res += str[x]

print(res)
