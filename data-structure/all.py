# list = [1, 2, 3, 4, 5]
# tup = (10, 20, 30, 30, 30)
dict = {"name": "Ravi Karmakar", "age": 24, "city": "Bangalore", "country": "India"}
# set = {1, 2, 3, 4, 5}

# print("List:", list[0])
# print("Tuple:", tup[0])
# print("Dictionary:", dict["name"])
# print("Set:", set)

# print("Reverse List:", list[::-1])

# for i in range(len(list)-1, -1, -1):
#     print(list[i])

# print("last element index of list:", len(list)-1)
# for i in range(len(list)-1, -1, -1):
#   print(list[i])
# print(list[3:9])

# tup =("Ravi",21,"mca","Male")
# dict = {"Ravi" : tup}

# print("Name:",dict["Ravi"][0])
# print("Age:",dict["Ravi"][1])
# print("Course:",dict["Ravi"][2])
# print("Gender:",dict["Ravi"][3])

# print(tup.count(30))
# print(tup.index(30))
# print("Dict all keys and values0:", dict)
# print(dict["name"])
# print(dict.get("name"))
# dict.update({"age": 22})
# print(dict.get("age"))
# print(dict.pop("country"))
# print("Dict all keys and values1:", dict)
# dict["house"] = "Old Malda"
# print(dict.get("house"))
# print(dict.keys())

# print("Dict all keys and values2:", dict)

matrix1 = [[1, 2, 3], [6, 7, 8], [9, 10, 11]]
matrix2 = [[3, 5, 7], [1, 3, 5], [1, 22, 0]]
for i in range(len(matrix1)):
  for j in range(len(matrix2)):
    matrixResult[i][j] = matrix1[i][j] + matrix2[i][j]

for row in matrixResult[i][j]:
  print(row)