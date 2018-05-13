import re
import os
from dictionary import dictionary
clear = lambda:os.system('cls')

botName = "BOT"
userName = "USER"
chatHistory = []

def askQuestion(questionStr, followUpQuestion=[]):
  while True:
    formattedQuestion  = formatText(botName, questionStr, True)
    answer = input(formattedQuestion + "\n" + formatText(userName, "", True))
    formattedAnswer = formatText(userName, answer, True)
    chatHistory.append(formattedAnswer)
    chatHistory.append(formattedQuestion)

    for keyword in list(dictionary.keys()):
      if bool(re.search(keyword, answer.lower())):
        break
    else:
      questionStr = "Ik begrijp niet wat u zegt"
      chatHistory.append(formatText(botName, questionStr, True))
      continue
    break
  return keyword

def showChatHistory():
  print("Chat:")
  for line in chatHistory:
    print(line)

def formatText(name, text, ret=False):
  formattedText = '{:<4s} {:<1s}'.format(name, "| " + text)
  if ret == True:
    return (formattedText)
  else:
    print(formattedText)
  

def main():
  questionStr = "Waar kan ik u mee helpen? "
  userInput = ""
  while True:
    showChatHistory()
    clear()
    userInput = askQuestion(questionStr)
    if userInput == "endchat":
      clear()
      showChatHistory()
      break
    else:
      questionStr = dictionary[userInput]

main()
