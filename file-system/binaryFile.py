data = b"This is a binary file.\nIt contains binary data.\n"

with open("binary_file.bin", "wb") as file:
    file.write(data)

print("Binary file created successfully.")
print("File path:", file.name)