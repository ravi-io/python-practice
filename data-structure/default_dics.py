from collections import defaultdict

students = defaultdict(list)

students["name"].append("Ravi Karmakar")
students["age"].append(22)
students["age"].append(24)
students["city"].append("Bangalore")
students["country"].append("India")

print("Students Dictionary:", students)