import re
import os
from dictionary import * #<-- imports dictionary and endKeyword
clear = lambda:os.system('cls')

botName = "BOT"
userName = "USER"
standardQuestion = "Waar kan ik u mee helpen?"
idkAnswer = "Ik begrijp niet wat u zegt"
chatHistory = []

#askQuestion asks the user a question, then checks if this contains any of the keywords stated in the dictionary
def askQuestion(questionStr, followUpQuestion=[]): #followUpQuestion seems a little too ambitious for now
  while True:
    foundKeywords = []
    formattedQuestion  = formatText(botName, questionStr, True)
    answer = input(formattedQuestion + "\n" + formatText(userName, "", True))
    formattedAnswer = formatText(userName, answer, True)
    chatHistory.extend([formattedQuestion, formattedAnswer])

    #Iterates through all of the keys in the dictionary
    for keyword in list(dictionary.keys()):
      #If a keyword is found, exit the loop and return the found keyword
      if bool(re.search(keyword, answer.lower())):
        foundKeywords.append(keyword)
    #If the input doesn't contain any know keywords, continue in this loop and change the questionStr to the standard answer
    if foundKeywords == []:
      questionStr = idkAnswer
      #chatHistory.extend([formatText(botName, questionStr, True)])
      continue
    else:
      break
  return foundKeywords

#Shockingly enough displays the chat history
def showChatHistory(lastFamousWords=""):
  print("Chat:")
  for line in chatHistory:
    print(line)
  print(lastFamousWords)

#Prints (or returns, if needed) the message with the name of the person who sent the message in a nice way
def formatText(name, text, ret=False):
  formattedText = '{:<4s} {:<1s}'.format(name, "| " + text)
  if ret == True:
    return (formattedText)
  else:
    print(formattedText)
  

def main():
  questionStr = standardQuestion
  inputKeywords = ""
  while True:
    clear()
    if questionStr == idkAnswer:
        questionStr =  standardQuestion
    inputKeywords = askQuestion(questionStr)
    questionStr = ""
    #For each keyword in the input add the response to the questionStr
    for keyword in inputKeywords:
      #chatHistory
      questionStr+= (dictionary[keyword])+"\n"
    questionStr+= formatText(botName, "Heeft u verder nog vragen?", True)
    #If the endKeyword is called in the input, the chat will be ended with the response to the other keywords
    if endKeyword in inputKeywords:
      clear()
      showChatHistory(questionStr)
      break
  formatText(botName, "Bye ;(")

main()
