from random import randint
from strings import strings
import os
clear = lambda:os.system('cls')

class bcolors:
    h = '\033[95m'
    end = '\033[0m'
    underl = '\033[4m'


res = ""

def showProgress():
  if res != "":
    return "Uw kunstwerk tot nu toe:\n" + res + "\n \n"
  else:
    return ""

def askQuestion():
  while True:
    try:
      answer = int(input(questionStr))
    except ValueError:
      clear()
      print(bcolors.h + "Vul een nummer tussen 0 en " + str(len(str1)-1) + " in" + bcolors.end)
      continue

    if len(str1)-1 >= answer >= 0:
      break

    else:
      clear()
      print(bcolors.h + "Vul een nummer tussen 0 en " + str(len(str1)-1) + " in" + bcolors.end)
      continue
  return answer

for str1 in strings:
  questionStr = showProgress() + "Kies uit:\n"
  for str2 in str1:
    questionStr += str(str1.index(str2)) + "| " + str2 + "\n"
  res += str1[askQuestion()]
  clear()
print(bcolors.underl + "Resultaat:\n" + bcolors.end + res)
