indx = input("Enter a name:")
list = [char for char in indx]

i=0
while i < len(list):
    if list[i] in "ABCDEFGHIJKMLNOPQRSTUVWSYZ":
        list.insert(i,"_")



    i+=1

str="".join(list)
result = str.lower()
print(result)