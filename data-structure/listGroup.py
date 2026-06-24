from collections import defaultdict

# names = ["Ravi", "Abhi", "Priya", "Aditi", "Pashu"]

i = 1
names = []


attend = defaultdict(list)

while i <= 5:
  names.append(input("Enter name: "))
  i += 1
  
for word in names:
  attend[word[0]].append(word)

print(attend)


# count = defaultdict(int)
# for ch in "RaviKarmakar":
#   count[ch] += 1
  
# print(count)