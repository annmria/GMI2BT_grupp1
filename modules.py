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

jsonFile= 'labb2_personer_vt22.json'


def program_lab2():

    csvFilePath = 'labb2_personer_vt22.csv'
    data = {} 
    
    
    
    menu_options = {
        1: '1: read original file to json',
        2: "2: show current json data",
        3: '3: add a person',
        4: '4: remove a person',
        5: '5: save file',
        6: '6: exit'
    }
    
    def print_menu():
        for personer in menu_options.keys():
            print (personer, '--', menu_options[personer])
    
    while [1, 5]:
        print_menu()         
        option= int(input("Välj 1-6: "))

        if option == 1:
            with open(csvFilePath, "r", encoding="utf-8-sig" ) as csvFile:
                csvReader = csv.DictReader(csvFile)
                for rows in csvReader:
                    print(rows)
                    key =rows["användarnamn"]
                    data [key] = rows
            with open ("labb2_personer_vt22.json", "w", encoding="utf-8-sig") as json_obj:
                json.dump(data, json_obj, ensure_ascii=False, indent=4)       
            
        elif option == 2:
           open_file= open(jsonFile, "r")
           load_data=json.load(open_file)
           output= json.dumps(load_data, indent=4, ensure_ascii=False)
           open_file.close()
           print(output)

        elif option == 3:
            temp_dict ={}
            användarnamn =input("ange användarnamn: ")
            förnamn =input("ange förnamn: ")
            efternamn =input("ange efternamn: ")
            epost =input("ange epost: ")
            user_dict ={ "användarnamn":  användarnamn,
                          "förnamn": förnamn,
                           "efternamn":  efternamn,
                           "epost": epost,}
            with open("labb2_personer_vt22.json", 'r', encoding="utf-8-sig") as fil:
                add_to_json=json.load(fil)
                for key, value in add_to_json.items():
                    temp_dict[key]=value
                temp_dict[användarnamn]=user_dict
            with open ("labb2_personer_vt22.json", "w", encoding="utf-8-sig") as json_obj:     
                json.dump(temp_dict, json_obj, ensure_ascii=False, indent=4)
                 
        elif option == 4:
            with open(json_obj, 'd', encoding="utf-8") as jsonFile:
                print()
                
        elif option == 5:
            with open(json_obj, "w", encoding="utf-8") as jsonFile:
                print()
        
        else:
            print("Avslutar programet")

program_lab2()

