file_path = 'whitelist_branches.txt'

with open(file_path, 'r') as file:
    for line in file:
        print(line.strip())
