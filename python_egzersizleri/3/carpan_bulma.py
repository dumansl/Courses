def carpanlar(sayi):
    liste = []
    for i in range(1,sayi+1):
        if sayi % i == 0 :
            liste.append(i)
    print(liste)

carpanlar(25)
