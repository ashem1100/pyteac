def main():
    index = input("Enter a time: ")
    num = convert(index)
    if 8.0 >= num >= 7.0:
        print("breakfast time")
    elif 13.0 >= num >= 12.0:
        print("lunch time")
    elif 19.0 >= num >= 18.0:
        print("dinner time")
    else:
        return 0



def convert(time):
    h,m = time.split(":")
    hour = int(h)
    min = int(m)

    result = float(hour+(min/60))

    return result



main()