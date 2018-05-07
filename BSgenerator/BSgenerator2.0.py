from random import randint
import os
clear = lambda:os.system('cls')

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

strings = [
  ["Het proces ", "De factor mens ", "Het management ", "De communicatie ", "De kerncompetentie ", "Human capital ", "De organisatie-ontwikkeling ", "De missie ", "Kennismanagement ", "De eerste aanzet "],
  ["moet meerwaarde leveren bij ", "stelt eisen aan ", "dient te faciliteren bij ", "is uitgangspunt bij ", "is onlosmakelijk verbonden met ", "schept voorwaarden voor ", "dient te focussen op ", "stuurt ", "hangt nauw samen met ", "moet een opstap bieden voor "],
  ["de implementatie van ", "de terugkoppeling van ", "het aftimmeren van ", "het aansturen van ", "de ontwikkeling van ", "de flexibilisering van ", "de integratie van ", "de inventarisatie van ", "de definitie van ", "de insteek van "],
  ["complexe ", "optimale ", "in elkaar grijpende ", "eenduidige ", "onderling afhankelijke ", "structurele ", "pro-actieve ", "resultaatgerichte ", "efficiënte ", "consistente "],
  ["supply chain processen ", "business architecture ", "mijlpalen ", "targets ", "business units ", "organisatie-onderdelen ", "scenario's ", "best practices ", "business models ", "conceptplannen "],
  ["waarbij het belang van ", "waarbij de feedback van ", "waarbij het kader voor ", "waarbij afstemming met ", "waarbij de structuur van ", "waarbij de synergie met ", "waarbij de interface met ", "waarbij input van ", "waarbij commitment van ", "waarbij klankborden met "],
  ["strategisch beleid ", "de taskforce ", "de communicatie ", "de werkgroepen ", "new business development ", "de systeemintegratie ", "de markt ", "de stakeholders ", "het management ", "de projectorganisatie "],
  ["moet uitkristalleren.", "voorop staat.", "wordt aangestuurd.", "leading is.", "toegevoegde waarde levert.", "win-win situaties kan veroorzaken.", "moet worden gemanaged.", "voldoende draagvlak heeft.", "doorslaggevend is.", "cruciaal is."]
  ]

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
      print(bcolors.FAIL + "Vul een nummer tussen 0 en " + str(len(str1)-1) + " in" + bcolors.ENDC)
      continue

    if len(str1)-1 >= answer >= 0:
      break

    else:
      clear()
      print(bcolors.FAIL + "Vul een nummer tussen 0 en " + str(len(str1)-1) + " in" + bcolors.ENDC)
      continue
  return answer

for str1 in strings:
  questionStr = showProgress() + "Kies uit:\n"
  for str2 in str1:
    questionStr += str(str1.index(str2)) + "| " + str2 + "\n"
  res += str1[askQuestion()]
  clear()
print(bcolors.UNDERLINE + "Resultaat:\n" + bcolors.ENDC + res)
