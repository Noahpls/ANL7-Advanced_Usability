from random import randint
from strings import strings
import os
clear = lambda:os.system('cls')

class bcolors:
    HEADER = '\033[95m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'


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
      print(bcolors.HEADER + "Vul een nummer tussen 0 en " + str(len(str1)-1) + " in" + bcolors.ENDC)
      continue

    if len(str1)-1 >= answer >= 0:
      break

    else:
      clear()
      print(bcolors.HEADER + "Vul een nummer tussen 0 en " + str(len(str1)-1) + " in" + bcolors.ENDC)
      continue
  return answer

for str1 in strings:
  questionStr = showProgress() + "Kies uit:\n"
  for str2 in str1:
    questionStr += str(str1.index(str2)) + "| " + str2 + "\n"
  res += str1[askQuestion()]
  clear()
print(bcolors.UNDERLINE + "Resultaat:\n" + bcolors.ENDC + res)
