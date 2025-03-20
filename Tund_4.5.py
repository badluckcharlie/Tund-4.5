idkood = input("Sisestage ID kood: ")

if len(idkood) != 11 or not idkood.isdigit():
    print("Viga! ID kood peab olema 11 numbrit pikk ja ainult numbreid.")
else:
    first_digit = int(idkood[0])
    if first_digit in [1, 3, 5]:
        gender="Mees"
    elif first_digit in [2, 4, 6]:
        gender="Naine"
    else:
        print("Viga! Esimene number ei vasta.")
    if first_digit in [1, 2]:
        age = 1800
    elif first_digit in [3, 4]:
        age = 1900
    elif first_digit in [5, 6]:
        age = 2000
    else:
        print("Viga!")
    year = age + int(idkood[1:3])
    month = int(idkood[3:5])
    day = int(idkood[5:7])
    hospital_index = int(idkood[7:10])
    if hospital_index in range(1, 11):
        birthplace="Kuressaare Haigla"
    if hospital_index in range(11, 20):
        birthplace="Tartu Ülikooli Naistekliinik"
    if hospital_index in range(21, 151):
       birthplace="Ida-Tallinna Keskhaigla, Pelgulinna Sünnitusmaja (Tallinn)"
    if  hospital_index in range(151, 161):
        birthplace="Keila Haigla"
    if hospital_index in range(161, 221):
        birthplace="Rapla Haigla, Loksa Haigla, Hiiumaa Haigla (Kärdla)"
    if hospital_index in range(221, 271):
        birthplace="Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)"
    if hospital_index in range(271, 371):
        birthplace="Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla"
    if hospital_index in range(371, 421):
        pbirthplace="Narva Haigla"
    if hospital_index in range(421, 471):
        birthplace="Pärnu Haigla"
    if hospital_index in range(471, 491):
        birthplace="Haapsalu Haigla"
    if hospital_index in range(491, 521):
        birthplace="Järvamaa Haigla (Paide)"
    if hospital_index in range(521, 571):
        birthplace="Rakvere Haigla, Tapa Haigla"
    if hospital_index in range(571, 601):
        birthplace="Valga Haigla"
    if hospital_index in range(601, 651):
        birthplace="Viljandi Haigla"
    if hospital_index in range(651, 701):
        birthplace="Lõuna-Eesti Haigla (Võru), Põlva Haigla"
    print(f"See on {gender}, tema sünnipäev on {day}.{month}.{year} ja sünnikoht on {birthplace}.")

    w1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    w2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    
    checksum = 0
    for i in range(10):
        checksum += int(idkood[i]) * w1[i]
    
    lastdigit = checksum % 11
    if lastdigit >= 10:
        checksum = 0
        for i in range(10):
            checksum += int(idkood[i]) * w2[i]
        lastdigit = checksum % 11
        if lastdigit >= 10:
            lastdigit = 0
    arvud = []
    idkoodid = []
    if lastdigit != int(idkood[10]):
        print("Viga! ID kood ei ole korrektne.")
        arvud.append(idkood)
    else:
        print("ID kood on korrektne.")
        idkoodid.append(idkood)