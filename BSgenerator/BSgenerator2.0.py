from random import randint
import os
clear = lambda:os.system('cls')


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

for str1 in strings:
  if res != "":
    print("Uw kunstwerk tot nu toe:\n" + res + "\n \n")
  question = "Kies uit:\n"
  for str2 in str1:
    question += "|[" + str(str1.index(str2)) + "] " + str2 + "\n"
  answer = int(input(question))
  res += str1[answer]
  clear()
print("Resultaat:\n" + res)

