import random 

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
            
    
    
   