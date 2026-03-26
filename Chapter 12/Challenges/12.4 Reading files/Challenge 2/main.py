file_name = input()

pear_file = open(file_name)

pear_data = pear_file.read()

pear_file.close()

print(pear_data)