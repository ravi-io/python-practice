list1 = []

def checkNumber(list1):
  num = int(input("Enter a number to search: "))
  if num in list1:
    print(f"{num} is present in the list.")
  else:
    print(f"{num} is not present in the list.")

for i in range(6):
  list1.append(int(input("Enter a number: ")))

checkNumber(list1)