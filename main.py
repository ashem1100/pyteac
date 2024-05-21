index = input("Enter a text: ")
x , opr , y = index.split(" ")

match opr:
    case "+":
      print(float(x) + float(y))
    case "-":
      print(float(x) - float(y))
    case "*":
      print(float(x) * float(y))
    case "/":
      print(float(x) / float(y))
