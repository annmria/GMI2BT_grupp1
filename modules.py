thousand = list(range(1, 1001))
def nummer (x, y):
    quotients = []
    for number in thousand:
        if number % x==0 & number % y==0:
            quotients.append(number)
    print(quotients)
nummer (7, 11)

import random 
number=random.randint (1, 15)
print ("Välkommen till vårt gissningsspel. Spelet kommer välja ett tal mellan 1-15 och du ska gissa vilket nummer som har valts")
print ("Gissa ett nummer mellan 1-15")
guess =input (int ())

if number != guess:
    
    print("å nej du suger försök igen")   
    
else:
    print(" tjola hej du hade rätt")
    
    
   