import re
import os
from dictionary import * #<-- importeert dictionary en endKeyword
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

    #iterates through all of the keys in the dictionary
    for keyword in list(dictionary.keys()):
      #if a keyword is found, exit the loop and return the found keyword
      if bool(re.search(keyword, answer.lower())):
        foundKeywords.append(keyword)
    #if the input doesn't contain any know keywords, continue in this loop and change the questionStr to the standard answer
    if foundKeywords == []:
      questionStr = idkAnswer
      chatHistory.extend([formatText(botName, questionStr, True)])
      continue
    break
  return foundKeywords
  #return keyword

#shockingly enough displays the chat history
def showChatHistory(lastFamousWords=""):
  print("Chat:")
  for line in chatHistory:
    print(line)
  print(lastFamousWords)

#prints (or returns, if needed) the message with the name of the person who sent the message in a nice way
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
    showChatHistory()
    clear()
    if questionStr == idkAnswer:
        questionStr =  standardQuestion
    inputKeywords = askQuestion(questionStr)
    questionStr = ""
    #for each keyword in the input add the response to the questionStr
    for keyword in inputKeywords:
      questionStr+= (dictionary[keyword])+"\n"
    questionStr+= formatText(botName, "Heeft u verder nog vragen?", True)
    #if the endKeyword is called in the input, the chat will be ended with the response to the other keywords
    if endKeyword in inputKeywords:
      clear()
      showChatHistory(questionStr)
      break
  formatText(botName, "Bye ;(")

main()
