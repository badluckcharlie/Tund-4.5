idkood = input("Sisestage ID kood: ")

if len(idkood) != 11 or not idkood.isdigit():
    print("Viga! ID kood peab olema 11 numbrit pikk ja sisaldama ainult numbreid.")
else:
    first_digit = int(idkood[0])
    if first_digit in [1, 3, 5]:
        print("See on mees")
    elif first_digit in [2, 4, 6]:
        print("See on naine")
    else:
        print("Viga! Esimene number ei vasta.")
    if first_digit in [1, 2]:
        century = 1800
    elif first_digit in [3, 4]:
        century = 1900
    elif first_digit in [5, 6]:
        century = 2000
    else:
        print("Viga!")
    year = century + int(idkood[1:3])
    month = int(idkood[3:5])
    day = int(idkood[5:7])
    print(f"Sünnikuupäev: {day:02d}.{month:02d}.{year}")
    hospital_index = int(idkood[7:10])
    if hospital_index in range(1, 11):
        print("Kuressaare Haigla")
    if hospital_index in range(11, 20):
        print("Tartu Ülikooli Naistekliinik")
    if hospital_index in range(21, 151):
       print("Ida-Tallinna Keskhaigla, Pelgulinna Sünnitusmaja (Tallinn)")
    if  hospital_index in range(151, 161):
        print("Keila Haigla")
    if hospital_index in range(161, 221):
        print("Rapla Haigla, Loksa Haigla, Hiiumaa Haigla (Kärdla)")
    if hospital_index in range(221, 271):
        print("Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)")
    if hospital_index in range(271, 371):
        print("Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla")
    if hospital_index in range(371, 421):
        print("Narva Haigla")
    if hospital_index in range(421, 471):
        print("Pärnu Haigla")
    if hospital_index in range(471, 491):
        print("Haapsalu Haigla")
    if hospital_index in range(491, 521):
        print("Järvamaa Haigla (Paide)")
    if hospital_index in range(521, 571):
        print("Rakvere Haigla, Tapa Haigla")
    if hospital_index in range(571, 601):
        print("Valga Haigla")
    if hospital_index in range(601, 651):
        print("Viljandi Haigla")
    if hospital_index in range(651, 701):
        print("Lõuna-Eesti Haigla (Võru), Põlva Haigla")
