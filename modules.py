import random 
import csv
import json
from shutil import ExecError


def nummer (x, y):
    thousand = list(range(1, 1001))
    quotients = []
    for number in thousand:
        if number % x==0 and number % y==0:
            quotients.append(number)
    print(quotients)
def spel ():
    number=random.randint (1, 15)
    guess =0
    print ("Välkommen till vårt gissningsspel. Spelet kommer välja ett tal mellan 1-15 och du ska gissa vilket nummer som har valts")
    while guess<5:
        gissning = int (input ("Gissa ett nummer mellan 1-15 (du har 5 försök)"))
        guess +=1
        if number!= gissning:
            print("å nej du suger försök igen")   
        elif number==gissning:
            print("tjola hej du hade rätt")
            break
        else:
            print("du har slut på försök och förlorade")
            break
            
    
    


# {} to create a dictionary, [] to index it




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
            print (personer, '--', menu_options[personer]) #en funktion som printar en meny
    
    while [1, 5]:
        print_menu()        
        option= int(input("Välj 1-6: "))
            
        if option == 1:
            try:
                with open(csvFilePath, "r", encoding="utf-8-sig" ) as csvFile:
                    csvReader = csv.DictReader(csvFile)    
                    for rows in csvReader:
                        print(rows)
                        key =rows["användarnamn"]
                        data [key] = rows
            except FileNotFoundError:
                    print("File not found. Check filepath/name")    
            with open ("labb2_personer_vt22.json", "w", encoding="utf-8-sig") as json_obj:
                json.dump(data, json_obj, ensure_ascii=False, indent=4)       
            
        elif option == 2:
           try: 
                open_file= open("labb2_personer_vt22.json", "r", encoding="utf-8-sig")
                load_data=json.load(open_file)
                output= json.dumps(load_data, indent=4, ensure_ascii=False)
                open_file.close()
                print(output)
           except FileNotFoundError:
               print("File not found. Check filepath/name")    

        elif option == 3:
            temp_dict ={}
            användarnamn =input("ange användarnamn: ")
            förnamn =input("ange förnamn: ")
            efternamn =input("ange efternamn: ")
            epost =input("ange epost: ")
            user_dict ={ "användarnamn":  användarnamn,
                          "förnamn": förnamn,
                           "efternamn":  efternamn,
                           "epost": epost,} #sparar all input i en dict
            try:
                with open("labb2_personer_vt22.json", 'r', encoding="utf-8-sig") as fil:
                    add_to_json=json.load(fil)
                    for key, value in add_to_json.items():
                        temp_dict[key]=value
                    temp_dict[användarnamn]=user_dict
            except FileNotFoundError:
                    print("File not found. Check filepath/name")     
            with open ("labb2_personer_vt22.json", "w", encoding="utf-8-sig") as json_obj:     
                json.dump(temp_dict, json_obj, ensure_ascii=False, indent=4)
                 
        elif option == 4:
            användarnamn =input("ange användarnamn på personen du vill ta bort: ") 
            new_dict={}
            try:
                with open("labb2_personer_vt22.json", 'r', encoding="utf-8-sig") as json_obj:
                    json_dict =json.load(json_obj) 
                    for key in json_obj:
                        print(key, ",", json_dict[key])
                    del json_dict[användarnamn] #raderar användarnamn från användaren
                    for key, value in json_dict.items():
                        new_dict[key] = value
                    for key, value in new_dict.items():
                     print(key, value)
            except FileNotFoundError:
                print("File not found. Check filepath/name")
            except KeyError:
                print("key not found. Check spelling")          
            with open ("labb2_personer_vt22.json", 'w', encoding="utf-8-sig") as new_json:
                json.dump(new_dict, new_json, ensure_ascii=False ,indent=4) #bygger upp allt igen
                
        elif option == 5:
            header_list=[] #tomma listor som man kan fylla längre ner
            row_list= []
            try:
                with open("labb2_personer_vt22.json", "r", encoding="utf-8-sig") as jsonF:
                    jsonD= json.load(jsonF)
                    for v_json in jsonD.values():
                        #print(v_json)  Kan kolla så det funkar.
                        for k in v_json.keys():
                            if k not in header_list:
                                header_list.append(k) #lägger till saker om det inte redan finns.
                        row_list.append(v_json.copy()) 
            except FileNotFoundError:
                print("File not found. Check filepath/name")  
                
            print(header_list) # så att man kan se sakerna i terminalen bara, så slipper man kolla filerna om man inte orkar med det.
            print(row_list)
            
            with open (csvFilePath, "w", newline="", encoding="utf-8-sig") as csvfil:
                skrivarObj= csv.DictWriter(csvfil, fieldnames=header_list)
                skrivarObj.writeheader()
                for data in row_list:
                    skrivarObj.writerow(data)
            print("Nu har filerna blivit uppdaterade")
        
        else:
            print("Avslutar programet")
            exit()




