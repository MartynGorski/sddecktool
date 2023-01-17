import re

MainDescriptor = []
DeckDivision = []
DeckIdentifier = []
Superior = []
Quantity = []
TempArray = []
MainDscCounter = -1

def importdata(filename):
    global MainDescriptor, DeckDivision, DeckIdentifier, Superior, Quantity, TempArray, MainDscCounter
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    for j, i in enumerate(lines):
        if re.search('expor.+', i):
            i = i.strip("export ")
            i = i.rstrip(" is TDeckDescriptor")
            MainDescriptor.append(i)
            MainDscCounter += 1
            Quantity.append([])
            DeckDivision.append(lines[j+1])
            DeckIdentifier.append(lines[j+2])
            Superior.append(lines[j+3])
        if re.search('Quanti.+', i):
            i = i.lstrip("Quantity = ")
            TempArray.append(i)
            lines[j+1] = lines[j+1].lstrip("DeckPack = ")
            TempArray.append(lines[j+1])
            lines[j+2] = lines[j+2].lstrip("ExperienceLevel = ")
            TempArray.append(lines[j+2])
            Quantity[MainDscCounter].append(TempArray)
            TempArray = []


def exportdata():
    global MainDescriptor, DeckDivision, DeckIdentifier, Superior, Quantity, TempArray, MainDscCounter
    f1 = open("exporttest.ndf", "w")
    for i, j in enumerate(MainDescriptor):
        f1.write(f"export {j} is TDeckDescriptor\n(\n")
        f1.write(f"\tDeckDivision = {DeckDivision[i]}\n")
        f1.write(f"\tDeckIdentifier = {DeckIdentifier[i]}\n")
        f1.write(f"\tSuperior = {Superior[i]}\n")
        f1.write(f"\tDeckPackList = \n\t[\n")
        for k, l in enumerate(Quantity[i]):
            f1.write(f"\t\tTDeckPackDescription\n\t\t(\n")
            temp = Quantity[i][k]
            f1.write(f"\t\t\tQuantity = {temp[0]}\n")
            f1.write(f"\t\t\tDeckPack = {temp[1]}\n")
            f1.write(f"\t\t\tExperienceLevel = {temp[2]}\n\t\t),\n")
        f1.write(f"\t]\n)\n")

importdata("testfile3.txt")        
exportdata()
