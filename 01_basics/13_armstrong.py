num = int(input("Enter a number: "))
order = len(str(num))
name ="Ravi Karmakar"

print(num)
print(type(order))

sum_val = sum(int(digit) ** order for digit in str(num))
if num == sum_val:
  print(f"{num} is an Armstrong number.")
else:    
  print(f"{num} is not an Armstrong {name} number.")