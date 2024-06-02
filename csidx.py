text = input("Input: ")
for i in text:
    if i in ["a","e","i","o","u","A","E","I","O","U"]:
        print("", end="")
    else:
        print(i, end="")
print("")