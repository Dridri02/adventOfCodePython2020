#import os
#print(os.listdir())
import string

ChampsObligatoiresRenseignesInitial =	{
  "byr": False,
  "iyr": False,
  "eyr": False,
  "hgt": False,
  "hcl": False,
  "ecl": False,
  "pid": False,
}

def compterPasserportsValides(data):
    nombrePasserportsValides=0
    nombreLigne = len(data)
    renseignementChampsObligatoire=ChampsObligatoiresRenseignesInitial.copy()
    for i in range(nombreLigne):
        ligne = data[i]
        ligne = ligne.strip() 
        if ligne == "":
            passeportValide = True
            for cle, valeur in renseignementChampsObligatoire.items():
                if valeur == False:
                    print(valeur)
                    passeportValide = False
            if passeportValide:
                nombrePasserportsValides = nombrePasserportsValides +1 
            renseignementChampsObligatoire=ChampsObligatoiresRenseignesInitial.copy()
        else:
            keysValues = ligne.split(" ")
            for j in range(len(keysValues)):
                key = keysValues[j].split(":")[0]
                value = keysValues[j].split(":")[0]
                renseignementChampsObligatoire[key]=True
# il n'y a pas de saut de ligne après le dernier passeport mais
# il faut le traiter tout de meme 
    return nombrePasserportsValides



def part1(path):
    file=open(path)
    data=file.readlines()  
    return compterPasserportsValides(data)




def compterPasserportsValidesAvecControleChamps(data):
    nombrePasserportsValides=0
    nombreLigne = len(data)
    renseignementChampsObligatoire=ChampsObligatoiresRenseignesInitial.copy()
    for i in range(nombreLigne):
        ligne = data[i]
        ligne = ligne.strip() 
        if ligne == "":
            passeportValide = True
            for cle, valeur in renseignementChampsObligatoire.items():
                if valeur == False:
                    print(valeur)
                    passeportValide = False
            if passeportValide:
                nombrePasserportsValides = nombrePasserportsValides +1 
            renseignementChampsObligatoire=ChampsObligatoiresRenseignesInitial.copy()
        else:
            keysValues = ligne.split(" ")
            for j in range(len(keysValues)):
                key = keysValues[j].split(":")[0]
                value = keysValues[j].split(":")[1]
                renseignementChampsObligatoire[key]=controlerChamp(key,value)
# il n'y a pas de saut de ligne après le dernier passeport mais
# il faut le traiter tout de meme 
    return nombrePasserportsValides


def controlerChamp(key,value):
    if key == "byr":
        value= int(value)
        return value // 1000> 0 and value // 10000 == 0 and value >= 1920 and value <= 2002
    elif key == "iyr":
        value= int(value)
        return value // 1000> 0 and value // 10000 == 0 and value >= 2010 and value <= 2020
    elif key == "eyr":
        value= int(value)
        return value // 1000> 0 and value // 10000 == 0 and value >= 2020 and value <= 2030
    elif key == "hgt":
        unite = value[len(value)-3:len(value)]
        print(value[0:len(value)-3])
        quantite = int(value[0:len(value)-3])
        if unite=="cm":
            return quantite >= 150 and quantite<= 193
        elif unite =="in":
            return quantite >=59 and quantite <= 76
        else:
            return False
    elif key == "hcl":
        return  len(value)==7 and value[0]== "#" and all(c in string.hexdigits for c in value[1:len(value)])
    elif key == "ecl":
        return  value in ["amb","blu","brn","gry","grn","hzl","oth"]
    elif key == "pid":
        return len (value) == 9 and all(c in string.digits for c in value[0:len(value)])
    else:
        return False

#print(part1("/home/coder/work/adventOfCodePython2020/dataJour4.txt"))


def part2(path):
    file=open(path)
    data=file.readlines()  
    return compterPasserportsValidesAvecControleChamps(data)



print(part2("/home/coder/work/adventOfCodePython2020/dataJour4.txt"))
