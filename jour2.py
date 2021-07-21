# import os

def compterOccurence(lettre,string):
    compteur=0
    for i in range(len(string)):
        if(string[i]==lettre):
            compteur=compteur+1
    return compteur


def part1(path):
    file=open(path)
    data=file.readlines()
    compteur=0
    for i in range(len(data)):
        ligne = data[i]
        ligneSplit = ligne.split("-")
        min=int(ligneSplit[0])
        max = int(ligneSplit[1].split()[0])
        lettre = ligneSplit[1].split()[1].strip(":")
        pwd = ligneSplit[1].split(":")[1].strip()
        print(min)
        print(max)
        print(lettre)
        print(pwd)
        if(compterOccurence(lettre,pwd)<= max and compterOccurence(lettre,pwd) >= min):
            compteur = compteur + 1 
        
    return compteur

def part2(path):
    file=open(path)
    data=file.readlines()
    compteur=0
    for i in range(len(data)):
        ligne = data[i]
        ligneSplit = ligne.split("-")
        premierePosition=int(ligneSplit[0])-1
        deuxiemePosition = int(ligneSplit[1].split()[0])-1
        lettre = ligneSplit[1].split()[1].strip(":")
        pwd = ligneSplit[1].split(":")[1].strip()
        if((pwd[premierePosition] == lettre and pwd[deuxiemePosition] != lettre) or (pwd[deuxiemePosition] == lettre and pwd[premierePosition] != lettre)):
            compteur = compteur + 1 
        
    return compteur

# print(os.listdir())
# print(part1("/home/coder/adventOfCodePython2020/dataJour2.txt"))
# print(part2("/home/coder/adventOfCodePython2020/dataJour2.txt"))