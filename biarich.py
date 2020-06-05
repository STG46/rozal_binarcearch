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
a = int(input())
b = int(input())
mass = []
massinput = []
file_name = "rozal_Rna_input.txt"
file_name1 = "rozal_output.txt"
f = open(file_name, 'r')
mass = [int(x) for x in f.read().split()]
massoutput = []
massinput = mass[a:]
mass = mass[0:a]
f.close()
for i in range(len(massinput)):
    massoutput.append(binary_search(massinput[i], mass))
f = open(file_name1, 'w')
f.write(' '.join([str(x) for x in massoutput]))
f.close()
