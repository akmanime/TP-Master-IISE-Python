with open("ex2.txt" , "w") as f:
    for i in range(3):
        p = input(f'la phrase {i+1} : ')
        f.write(f'{p}\n')
with open ("ex2.txt" , "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line)