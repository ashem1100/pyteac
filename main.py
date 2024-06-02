indx = input().strip()
list=[char for char in indx]
i=0

while i<=len(list):
  if list[i] in ("ioeauIOEAU"):
    list.remove(list[i])
    i=i+1
  else:
    i=i+1



result = "".join(list)

print(result)