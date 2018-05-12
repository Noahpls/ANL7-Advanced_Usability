import re
import os
clear = lambda:os.system('cls')

questionStr = "Vraag? "

keywords = ["informatie", "xd", "lol", "endchat"]
chatHistory = []

def askQuestion():
  while True:
    answer = input(questionStr)
    for keyword in keywords:
      if bool(re.search(keyword, answer.lower())):
        chatHistory.append(answer)
        break
    else:
      print("Dit is geen keyword")
      continue
    break
  return keyword

def main():
  clear()
  askQuestion()
  print("\nChat history:")
  for line in chatHistory.__reversed__():
    print(line + "\n")

main()