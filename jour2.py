import os

def part1(path):
    file=open(path)
    data=file.readlines()
    compteur=0
    for i in range(len(data)):
        string = data[i]
        print(string)



print(os.listdir())
print(part1("/home/coder/adventOfCodePython2020-1/dataJour2.txt"))