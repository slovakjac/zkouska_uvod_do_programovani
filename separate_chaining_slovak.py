#HASHOVÁNÍ - SEPARATE CHAINING
#Jáchym Slovák, 2. ročník B-FGG
#Choceň, 4. 2. 2026
#Úvod do programování MZ370P19  

class Hashovacitabulka:
    def __init__(self,velikost=10):
        self.velikost=velikost
        self.kose=[]
        for i in range(self.velikost):
            self.kose.append([])
        
    def hashovaci_funkce(self,klic):
        prvni_znak=klic[0]
        acsii_znaku=ord(prvni_znak)
        index=acsii_znaku%self.velikost
        return index
    
    def pridani(self,klic,hodnota):
        index_kose=self.hashovaci_funkce(klic)
        self.kose[index_kose].append([klic,hodnota])


tabulka=Hashovacitabulka()
vstup="vstup_separate_chaining.txt"

try:
    with open(vstup,"r",encoding="utf-8") as f:
        cislo_radku=0
        for radek in f:
            cislo_radku+=1
            radek=radek.strip()
            if not radek:
                continue
            if ";" in radek:
                casti= radek.split(";")

                if len(casti)==2:
                    klic=casti[0].strip()
                    hodnota=casti[1].strip()
                    tabulka.pridani(klic,hodnota)
                elif len(casti)>2:
                    klic=casti[0].strip()
                    hodnota=casti[1].strip()
                    tabulka.pridani(klic,hodnota)
                    print(f"Pozor! Na řádku {cislo_radku} bylo nalezeno více hodnot. Uložen pouze klíč a první hodnota.")

                else:
                    print(f"Chyba, na řádku {cislo_radku} chybí hodnota. Řádek přeskočen.")
            else:
                print(f"Chyba. Na řádku {cislo_radku} chybí oddělovač ';'.")
    with open("vystup_sc_slovak.txt", "w", encoding="utf-8") as o:
        for i in range(10):
            kos=tabulka.kose[i]
            pocet=len(kos)

            seznam=[]
            for dvojice in kos:
                seznam.append(f"({dvojice[0]}: {dvojice[1]})")
            vypis_kosu=",".join(seznam)
            o.write(f"Koš {i}, (počet: {pocet}): {vypis_kosu}\n")

    print("Hotovo. Výsledky jsou uloženy v souboru vystup_sc_slovak.txt.")

except FileNotFoundError:
    print(f"Chyba, soubor {vstup} nebyl nalezen")
except Exception as e:
    print(f"Neočekávaná chyba {e}")




        