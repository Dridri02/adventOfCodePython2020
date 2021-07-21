# import os

def part1(path):
    file=open(path)
    data=file.readlines()
    for i in range(len(data)):
        for j in range(len(data)):
            nombrei = int(data[i])
            nombrej = int(data[j])
            if nombrei+nombrej == 2020:
                return nombrei*nombrej
def part2(path):
    file=open(path)
    data=file.readlines()
    longueur = len(data)
    for i in range(longueur):
        for j in range(longueur):
            for k in range(longueur):
                nombrei = int(data[i])
                nombrej = int(data[j])
                nombrek = int(data[k])
                if nombrei+nombrej+nombrek == 2020:
                    return nombrei*nombrej*nombrek

# print(os.listdir())
# print(part1("/home/coder/adventOfCodePython2020/dataJour1.txt"))
# print(part2("/home/coder/adventOfCodePython2020/dataJour1.txt"))