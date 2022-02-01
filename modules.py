# import random 
import csv
import json

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



def program_lab2(csvFilePath, json_obj):

    csvFilePath = 'labb2_personer_vt22.csv'
    #jsonFilePath = 'labb2_personer_vt22.json'
    
    data = {} #behövs nog inte
    with open ("labb2_personer_vt22.json", "w", encoding="utf-8") as json_obj:
    json.dump(json_obj, ensure_ascii=False, indent=4)
    


    print("1: läs originalfil, 2: visa json data, 3: lägg till person, 4: ta bort person, 5: spara fil, 6: avsluta")
    
    menu_options = {
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6'
    }
    
    def print_menu():
        for personer in menu_options.keys():
            print (personer, '--', menu_options[personer])
    
    while [1, 5]:
        print_menu()
        #print("1=: read original file")            
        #print("2=: show json data")            
        #print("3=: add a person")            
        #print("4=: remove a person")            
        #print("5=: save file")            
        #print("6=: exit")            
        option= int(input("Välj 1-6: "))

        if option == 1:
            with open(csvFilePath, "r" ) as csvFile:
                csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                   print(rows)
            
        elif option == 2:
            with open(json_obj, 'r', encoding="utf-8") as jsonFile:
                jsonFile(json.dump(json_obj, indent=4))

        elif option == 3:
            with open(json_obj, 'a', encoding="utf-8") as jsonFile:
                 input("\n Lägg til person: ")

        elif option == 4:
            with open(json_obj, 'd', encoding="utf-8") as jsonFile:
                print()
                
        elif option == 5:
            with open(json_obj, "w", encoding="utf-8") as 
        
        else:
            print("Avslutar programet")

    program_lab2 ()