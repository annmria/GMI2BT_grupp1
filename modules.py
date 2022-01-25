
thousand = list(range(1, 1001))

# a = 5
# b = 2

# result = numbers in thousand / b
# print(result)

#print(thousand)

    # if quotients == quotients:
    #     result = int(quotients)
    # else:
    #     result = 0

def nummer (x, y):
    quotients = []
    for number in thousand:
        if number % x==0 & number % y==0:
            quotients.append(number)
    print(quotients)
nummer (7, 11)