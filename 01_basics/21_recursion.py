# def recursion(n, i):
#   num = i + 1
#   print(f"{n} * {num} = {n * num}")
  
#   if(num <= 9):
#     recursion(n, num)
#   else:
#     return
  
  
# number = int(input("Enter your number: "))  
# recursion(number, 0)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# write a pgm to take user age and has to take 
# is education at that particular age till 18 years 
# and at the end print all education values at once 

# studentData = []

# def eduCollData(strAge):
#   endAge = 18
  
#   if(strAge <= endAge): 
#     studentData.append(input(f"Enter your education qualification for {strAge}th age: "))
#     eduCollData(strAge + 1)
#   else:
#    return
 
# eduCollData(10)

# for i in range(len(studentData)):
#   print(f"At {i + 10}th age, education qualification is: {studentData[i]}")

# ----------------------------------------------------------


def recursion(n):
  if (n == 0):
    return 1
  else:
   return n * recursion(n - 1)
 
num = int(input("Enter your number: "))
print(recursion(num))