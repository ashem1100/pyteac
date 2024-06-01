
fe =50

while fe>0:
    indx = input("Insert Coin: ")

    if indx in ("5","10","25"):

        fe -= int(indx)
        if fe >= 0:
            print("Amount Due: "+ str(fe))
        elif fe <0:
            print("Change Owed: "+ str(fe*(-1)))

    else:
        print(fe)
        continue