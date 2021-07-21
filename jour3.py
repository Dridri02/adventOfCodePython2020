# import os
# print(os.listdir())

def compterArbresRencontres(data,pasVertical,pasHorizontal):
    positionHorizontale=0
    nombreArbresRencontres=0
    compteurVertical=0
    while compteurVertical+pasVertical <len(data):
        compteurVertical = compteurVertical+pasVertical
        ligne = data[compteurVertical]
        positionHorizontale= (positionHorizontale+pasHorizontal)%len(ligne.strip())  
        if(ligne[positionHorizontale]== "#"):
                nombreArbresRencontres=nombreArbresRencontres+1
    return nombreArbresRencontres


def part1(path):
    file=open(path)
    data=file.readlines()  
    return compterArbresRencontres(data,1,3)


print(part1("/home/coder/adventOfCodePython2020/dataJour3.txt"))


def part2(path):
    file=open(path)
    data=file.readlines() 
    return compterArbresRencontres(data,1,1)*compterArbresRencontres(data,1,3)*compterArbresRencontres(data,1,5)*compterArbresRencontres(data,1,7)*compterArbresRencontres(data,2,1)


print(part2("/home/coder/adventOfCodePython2020/dataJour3.txt"))