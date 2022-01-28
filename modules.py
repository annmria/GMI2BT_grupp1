# import random 

# def nummer (x, y):
#     thousand = list(range(1, 1001))
#     quotients = []
#     for number in thousand:
#         if number % x==0 and number % y==0:
#             quotients.append(number)
#     print(quotients)


# def spel ():
#     number=random.randint (1, 15)
#     guess =0
#     print ("Välkommen till vårt gissningsspel. Spelet kommer välja ett tal mellan 1-15 och du ska gissa vilket nummer som har valts")
#     while guess<5:
#         gissning = int (input ("Gissa ett nummer mellan 1-15 (du har 5 försök)"))
#         guess +=1
#         if number!= gissning:
#             print("å nej du suger försök igen")   
#         elif number==gissning:
#             print("tjola hej du hade rätt")
#             break
#         else:
#             print("du har slut på försök och förlorade")
#             break
            
    
    
# meny med 6 val: läs in originalfil (csv), visa json-data, lägg till person, ta bort person, spara fil, avsluta
# {} to create a dictionary, [] to index it
import csv
import json

def labb2_personer_vt22(csvFilePath, jsonFilePath):

    csvFilePath = 'labb2_personer_vt22.csv'
    jsonFilePath = 'labb2_personer_vt22.json'

    data = {}

    menu = {}
    menu['1'] = "read original file"
    menu['2'] = "show json data"
    menu['3'] = "add a person"
    menu['4'] = "remove a person"
    menu['5'] = "save file"
    menu['6'] = "exit"

    if menu == 1:
     with open(csvFilePath) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for rows in csvReader:
            id = rows['id']
            data[id] = rows

    elif menu == 2:
        with open(jsonFilePath, 'r') as jsonFile:
            jsonFile.read(json.dumps(data, indent=4))

# elif menu == 3:
#     with open(csvFilePath, 'a') as csvFile:
#         csvAppend = csv.DictAppend(csvFile)
#         input("\n Lägg til person: ")

# elif menu == 4:
#     with open(csvFilePath, 'w') as csvFile:

labb2_personer_vt22 ()