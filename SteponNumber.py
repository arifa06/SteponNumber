def steponNumber ():
    # Mencari pola dari nilai genap
    # Memecah menjadi masing-masing variabel x dan y
    xgenap = [0, ]
    for i in range(11):
        if i % 2 == 0:
            i += 2
            xgenap.append(i)
            xgenap.append(i*1)
        
    ygenap = []
    for i in range(11):
        if i % 2 == 0:
            i += 0
            ygenap.append(i)
            ygenap.append(i*1)
    ygenap.append(12) 

    xygenap = list(zip(xgenap,ygenap))
    nilaigenap = (0,2,4,6,8,10,12,14,16,18,20,22,24)
    koorgenap = list(zip(xgenap,ygenap,nilaigenap))

    # Mencari pola dari nilai ganjil
    # Memecah menjadi masing-masing variabel x dan y
    xganjil = [1, ]
    for i in range(1,12):
        if i % 2 == 0:
            pass
        else:
            i += 2
            xganjil.append(i)
            xganjil.append(i*1)
        
    yganjil = []
    for i in range(12):
        if i % 2 == 0:
            pass
        else:
            i += 0
            yganjil.append(i)
            yganjil.append(i*1)
    yganjil.append(13)

    xyganjil = list(zip(xganjil,yganjil))
    nilaiganjil = (1,3,5,7,9,11,13,15,17,19,21,23,25)
    koorganjil = list(zip(yganjil,yganjil,nilaiganjil))

    # Gabungan Genap dan Ganjil
    xygabungan = xygenap+xyganjil
    xygabungan.sort()
    
    koorgabungan = koorganjil+koorgenap
    koorgabungan.sort()
    
    # Cek keberadaan nilai dari suatu koordinat
    if (4,2,6) in koorgabungan:
        i = koorgabungan.index((4, 2, 6))
        print('Secara berurutan X, Y, Nilai adalah',koorgabungan[i])
    if (6,6,12) in koorgabungan:
        i = koorgabungan.index((6, 6, 12))
        print('Secara berurutan X, Y, Nilai adalah',koorgabungan[i])

steponNumber()