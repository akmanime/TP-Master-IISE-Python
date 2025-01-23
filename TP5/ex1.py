with open ("exemple.txt" , "w") as f:
    f.write('first line\n')
    f.write('second line\n')
    f.write('third line\n')
    f.write('fourth line\n')
    f.write('fifth line\n')

with open ("exemple.txt" , "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line)