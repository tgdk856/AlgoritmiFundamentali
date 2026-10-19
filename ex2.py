nume_fisier = input("Introduceti numele fisierului: ")

try:
    with open(nume_fisier, "r") as fisier:
        sir = []

        for linie in fisier:
            for numar in linie.split():
                sir.append(int(numar))

    print("Numerele citite din fisier:")
    print(*sir)

except FileNotFoundError:
    print("Eroare: Fisierul nu exista!")

except ValueError:
    print("Eroare: Fisierul contine valori care nu sunt numere!")