indx = input("Insert Coin: ")

fe =50

while fe != 0:
    if int(indx) == 5:
        fe=45
    elif int(indx) ==10:
        fe = 40
    elif int(indx) == 25:
        fe = 25
    else:
        fe = 50

print("Amount Due: " + str(fe))