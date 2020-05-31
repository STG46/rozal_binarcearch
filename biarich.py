def binary_search(ch, mass):
    nach = 0
    kon = len(mass) - 1
    while nach < kon:
        prom = int((nach + kon) / 2)
        if mass[prom] < ch:
            nach = prom + 1
        else:
            kon = prom
        print(prom)
    if ch == mass[kon]:
        return kon + 1
    else:
        return -1
file_name = "rozal_Rna_input.txt"
file_name1 = "rozal_output.txt"
f = open(file_name, 'r')
a = readlines
b = readlines
mass.append([int(x) for x in readlines.split()])
massinput = [int(x) for x in input().split()]
f.close()
massoutput =[]
for i in range(len(massinput)):
    massoutput.append(binary_search(massinput[i], mass))
print(massoutput)
