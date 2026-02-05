#INTERPOLACE - METODA IDW
#Jáchym Slovák, 2. ročník B-FGG
#Choceň, 5. 2. 2026
#Úvod do programování MZ370P19

from math import sqrt

class Bod:
    def __init__(self, x, y, z):
        self.x=float(x)
        self.y=float(y)
        self.z=float(z)
    
class IDW:
    def __init__(self, seznam_znamych_bodu):
        self.zname_body=seznam_znamych_bodu

    def interpolace(self, x_novy, y_novy, k):
        vsechny_vzdalenosti=[]
        for b in self.zname_body:
            s=sqrt((x_novy-b.x)**2 + (y_novy-b.y)**2)

            if s==0:
                return b.z
            vsechny_vzdalenosti.append([s,b])
        vsechny_vzdalenosti.sort(key=lambda x: x[0])
        nejblizsi_sousedi=vsechny_vzdalenosti[0:k]

        horni_suma=0
        dolni_suma=0

        for radek in nejblizsi_sousedi:
            vzdalenost=radek[0]
            bod=radek[1]
            vaha=1/vzdalenost
            horni_suma=horni_suma+(bod.z*vaha)
            dolni_suma=dolni_suma+vaha
        return horni_suma/dolni_suma
    
zname_body=[]
try:
    with open("zname_body_idw.txt","r") as f:
        cislo_radku_prvni=0
        for radek in f:
            cislo_radku_prvni+=1
            radek_cisty=radek.strip()
            if not radek_cisty:
                continue
            if ";" in radek_cisty:
                casti=radek_cisty.split(";")
                if len(casti)==3:
                    zname_body.append(Bod(float(casti[0]),float(casti[1]),float(casti[2])))
                else:
                    print(f"Na řádku číslo {cislo_radku_prvni} jsou neplatné souřadnice. Řádek přeskočen.")
            else:
                print(f"Chyba. Na řádku číslo {cislo_radku_prvni} chybí oddělovač ';'. Řádek přeskočen.")
except FileNotFoundError:
    print("Chyba. Soubor nenalezen.")
except ValueError:
    print("Chyba. Vstupní data musí být čísla ve správném formátu.")
except Exception as e:
    print(f"Neočekávaná chyba {e}")
pocet_dostupnych_bodu=len(zname_body)

while True:
    try:
        k_vstup=int(input(f"Zadejte počet nejbližších sousedů (k) - maximálně {pocet_dostupnych_bodu}: "))
        if 0<k_vstup<=pocet_dostupnych_bodu:
            break
        else:
            print(f"Neplatný rozsah")
    except ValueError:
        print("Zadejte číslo.")

interpolacni_nastroj=IDW(zname_body)

try:
    with open("vystup_idw_slovak.txt", "w") as o:
        with open("nezname_body.txt","r") as v:
            cislo_radku=0
            for radek in v:
                cislo_radku+=1
                radek_cisty=radek.strip()
                if not radek_cisty:
                    continue
                if ";" in radek_cisty:
                    casti=radek_cisty.split(";")
                    if len(casti)==2:
                        x_hledane=float(casti[0])
                        y_hledane=float(casti[1])
                        vypocitane_z=interpolacni_nastroj.interpolace(x_hledane,y_hledane,k_vstup)
                        o.write(f"{x_hledane}; {y_hledane}; {vypocitane_z:.4f}\n")
                    else:
                        print(f"Na řádku číslo {cislo_radku} je neplatný počet souřadnic. Řádek přeskočen.")
                else:
                    print(f"Chyba. Na řádku číslo {cislo_radku} chybí oddělovač ';'. Řádek přeskočen.")
    print("Hotovo. Výsledky jsou v souboru 'vystup_idw_slovak.txt'.")
except FileNotFoundError:
    print("Chyba! Soubor nenalezen.")
except Exception as e:
    print(f"Neočekávaná chyba {e}.")