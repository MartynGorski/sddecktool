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
            i = i.lstrip("export ")
            i = i[:-19]
            #i = i.rstrip("TDeckDescriptor")
            #i = i.rstrip("is ")
            MainDescriptor.append(i)
            MainDscCounter += 1
            Quantity.append([])
            DeckDivision.append(lines[j+1])
            DeckIdentifier.append(lines[j+2])
            if re.search('Superior =',lines[j+3]):
                Superior.append(lines[j+3])
            else:
                Superior.append("Pass")
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
    f1.write("// Ne pas éditer, ce fichier est auto-généré !\n\n\n")
    for i, j in enumerate(MainDescriptor):
        f1.write(f"export {j} is TDeckDescriptor\n(\n")
        f1.write(f"    {DeckDivision[i]}\n")
        f1.write(f"    {DeckIdentifier[i]}\n")
        if Superior[i] != "Pass":
            f1.write(f"    {Superior[i]}\n")
        f1.write(f"    DeckPackList =\n    [\n")
        for k, l in enumerate(Quantity[i]):
            f1.write(f"        TDeckPackDescription\n        (\n")
            temp = Quantity[i][k]
            f1.write(f"            Quantity = {temp[0]}\n")
            f1.write(f"            DeckPack = {temp[1]}\n")
            f1.write(f"            ExperienceLevel = {temp[2]}\n        ),\n")
        f1.write(f"    ]\n)\n")

importdata("sorteddecks.ndf") 
exportdata()
