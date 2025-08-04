# model.py

# Klasa za jednu jedinicu (figuru)
class Jedinica:
    def __init__(self, id_jedinice, tip, vlasnik, snaga, kretanje):
        self.id = id_jedinice
        self.tip = tip # npr. 'pesadija', 'konjica'
        self.vlasnik = vlasnik # npr. 'srbija', 'austrougarska'
        self.snaga = snaga
        self.kretanje = kretanje

# Klasa koja predstavlja jedan region na mapi
class Region:
    def __init__(self, ime, susedi):
        self.ime = ime
        self.susedi = susedi # Lista imena susednih regiona
        self.vlasnik = None # Moze biti 'srbija' ili 'austrougarska'
        self.jedinice = [] # Lista jedinica u ovom regionu

# Glavna klasa koja drži celo stanje igre
class StanjeIgre:
    def __init__(self):
        self.mapa = self.kreiraj_mapu()
        self.sve_jedinice = self.kreiraj_jedinice()
        self.postavi_jedinice_na_mapu()
        self.na_potezu = 'srbija'
        self.faza_poteza = 'pomeranje' # Kasnije mozete dodati 'borba', 'mobilizacija'

    def kreiraj_mapu(self):
        # Ovde definišete regione i njihove veze
        # Primer za MVP
        mapa = {
            'Beograd': Region('Beograd', susedi=['Šabac', 'Smederevo']),
            'Šabac': Region('Šabac', susedi=['Beograd', 'Loznica']),
            'Loznica': Region('Loznica', susedi=['Šabac']),
            'Smederevo': Region('Smederevo', susedi=['Beograd']),
        }
        # Inicijalno vlasništvo
        mapa['Beograd'].vlasnik = 'srbija'
        mapa['Smederevo'].vlasnik = 'srbija'
        mapa['Šabac'].vlasnik = 'austrougarska'
        mapa['Loznica'].vlasnik = 'austrougarska'
        return mapa

    def kreiraj_jedinice(self):
        # Kreiramo početne jedinice
        return {
            'srb_pesadija_1': Jedinica('srb_pesadija_1', 'pešadija', 'srbija', snaga=5, kretanje=1),
            'au_pesadija_1': Jedinica('au_pesadija_1', 'pešadija', 'austrougarska', snaga=5, kretanje=1)
        }

    def postavi_jedinice_na_mapu(self):
        self.mapa['Beograd'].jedinice.append(self.sve_jedinice['srb_pesadija_1'])
        self.mapa['Šabac'].jedinice.append(self.sve_jedinice['au_pesadija_1'])

    # TODO: Dodati metode za logiku igre
    # def pomeri_jedinicu(self, id_jedinice, odakle, kuda): ...
    # def resi_borbu(self, region_borbe): ...
    # def zavrsi_potez(self): ...