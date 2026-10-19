n = int(input("Introduceti numarul de elemente: "))

sir = []
for i in range(n):
    x = int(input(f"sir[{i}] = "))
    sir.append(x)

linii = int(input("Introduceti numarul de linii: "))
coloane = int(input("Introduceti numarul de coloane: "))

matrice = []
for i in range(linii):
    linie = []
    for j in range(coloane):
        x = int(input(f"matrice[{i}][{j}] = "))
        linie.append(x)
    matrice.append(linie)

print("\nSirul:")
for i in sir:
    print(i, end = ' ')

print("\nMatricea:")
for linie in range(len(matrice)):
    for coloana in range(len(matrice[linie])):
        print(matrice[linie][coloana], end = " ")
    print()