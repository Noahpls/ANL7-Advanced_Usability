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
      answer = int(input(questionStr)) #Ask the user for an input number
    except ValueError: #If the given answer is not a number
      clear()
      print(bcolors.h + "Vul een nummer tussen 0 en " + str(len(zinsdeel)-1) + " in" + bcolors.end)
      continue #Restart from the beginning of the loop

    if (0 <= answer <= len(zinsdeel)-1): #If the answer is a number in the possible range
      break                          #Exit the question loop and return the answer

    else: #If the answer is a number, but it is not inside the range
      clear()
      print(bcolors.h + "Vul een nummer tussen 0 en " + str(len(zinsdeel)-1) + " in" + bcolors.end)
      continue #Restart from the beginning of the loop
  return answer #Return the correct input to the program

for zinsdeel in strings:
  questionStr = showProgress() + "Kies uit:\n" #Show the user the progress
  for woordgroep in zinsdeel: #Show every phrase with the place in the array
    questionStr += str(zinsdeel.index(woordgroep)) + "| " + woordgroep + "\n"
  res += zinsdeel[askQuestion()] #Ask the user the question and add the result to the result
  clear() #Empty the screen
print(bcolors.underl + "Resultaat:\n" + bcolors.end + res) #Show the end result
