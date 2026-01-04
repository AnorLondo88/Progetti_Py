
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Parte 1 – Variabili e Tipi di Dati------------------------------------

nome = "Paolo"
eta = 35
saldo_conto = 1580.53
vip = True

destinazioni = ["Atene", "New York", "Roma", "Parigi", "Tokyo"]

prezzi_medi = {
    "Atene": 100.50,
    "New York": 1000.50,
    "Roma" : 200.10,
    "Parigi" : 99.65,
    "Tokyo" : 1200.00
}

#Parte 2 – Programmazione ad Oggetti (OOP)----------------------------

class Cliente:
    def __init__(self, nome, eta, vip):
        self.nome = nome
        self.eta = eta
        self.vip = vip

    def stampa_info(self):
        print(f"Nome: {self.nome}, Età: {self.eta}, VIP: {self.vip}")

class Viaggio:
    def __init__(self, destinazione, prezzo, durata_giorni):
        self.destinazione = destinazione
        self.prezzo = prezzo
        self.durata_giorni = durata_giorni

class Prenotazione: 
    def __init__(self, cliente, viaggio):
        self.cliente = cliente
        self.viaggio = viaggio

    def importo_finale(self):
        if self.cliente.vip:
            sconto = self.viaggio.prezzo * 0.10
            return round(self.viaggio.prezzo - sconto, 2)
        return round(self.viaggio.prezzo, 2)
    
    def dettagli(self):
        self.cliente.stampa_info()
        prezzo = self.viaggio.prezzo
        finale = self.importo_finale()

        print(
            f"Destinazione: {self.viaggio.destinazione} | "
            f"Prezzo: {prezzo:.2f}€ | "
            f"Durata giorni: {self.viaggio.durata_giorni} | "
            f"Importo finale: {finale:.2f}€"
        )

cliente1 = Cliente("Paolo", 35, True)
viaggio1 = Viaggio("Tokyo", prezzi_medi["Tokyo"], 10)
prenotazione1 = Prenotazione(cliente1, viaggio1)
prenotazione1.dettagli()  

#Parte 3 – NumPy--------------------------------------------------------------------

prezzi = np.random.uniform(200, 2000, 100)

media = prezzi.mean()
minimo = prezzi.min()
massimo = prezzi.max()
dev_std = prezzi.std()
percentuale_sopra_media = (prezzi > media).mean() * 100

print("Prezzo medio:", round(media, 2))
print("Prezzo minimo:", round(minimo, 2))
print("Prezzo massimo:", round(massimo, 2))
print("Deviazione standard:", round(dev_std, 2))
print("Percentuale sopra la media:", round(percentuale_sopra_media, 2), "%")

#Parte 4 – Pandas---------------------------------------------------------------------

dati = {
    "Cliente": ["Paolo", "Anna", "Luca", "Paolo", "Anna"],
    "Destinazione": ["Tokyo", "Roma", "Parigi", "Tokyo", "Roma"],
    "Prezzo": [1200.00, 200.10, 99.65, 1200.00, 200.10],

    #per convertire in date
    "Giorno_Partenza": pd.to_datetime([                             
        "2023-01-10", "2023-01-11", "2023-01-11",
        "2023-01-12", "2023-01-12"
    ]),
    "Durata": [10, 5, 4, 10, 5]
}

df = pd.DataFrame(dati)

# Incasso = Prezzo 
df["Incasso"] = df["Prezzo"]

print(df)

#totale incasso                         
incasso_totale = df["Incasso"].sum()

#incasso medio --> raggruppo riga destinazione dopo prendo colonna incasso e calcolo media
incasso_medio_dest = df.groupby("Destinazione")["Incasso"].mean()

#top 3 destinazioni vendute --> prendo colonna destinazione, conta quate volte compare, prendo i primi3
top_destinazioni = df["Destinazione"].value_counts().head(3)


print(incasso_totale)
print(incasso_medio_dest)
print(top_destinazioni)

#Parte 5 – Matplotlib--------------------------------------------------------------------------------------

#raggruppo righe dstinazione e sommo incasso
incasso_per_dest = df.groupby("Destinazione")["Incasso"].sum()

plt.figure()
plt.bar(incasso_per_dest.index, incasso_per_dest.values)
plt.title("Incasso per destinazione")
plt.xlabel("Destinazione")
plt.ylabel("Incasso (€)")
plt.show()

#raggruppo righe Giorno_partenza e sommo incasso
incasso_giornaliero = df.groupby("Giorno_Partenza")["Incasso"].sum()

plt.figure()
plt.plot(
    incasso_giornaliero.index,
    incasso_giornaliero.values,
    #per non far sembrare continui i valori
    marker="o"
)
plt.title("Andamento giornaliero degli incassi")
plt.xlabel("Data")
plt.ylabel("Incasso (€)")
#ruotare le etichette di 45 gradi per evitare sovrapposizioni e renderli leggibili
plt.xticks(rotation=45)
plt.show()

#prendo colonna destinazione, guardo riga per riga e conto quante volte compare
vendite_dest = df["Destinazione"].value_counts()
plt.figure()
plt.pie(
    #dimensione --> più alto è il numero, più grande è la fetta
    vendite_dest.values,
    #nome devo usare l'inidice -->.index
    labels=vendite_dest.index,
    #per far vedere la percentuale (un decimale)
    autopct="%1.1f%%"
)
plt.title("Percentuale di vendite per destinazione")
plt.show()

#Parte 6 – Analisi Avanzata---------------------------------------------------------------------------

categoria_dest = {
    "Atene": "Europa",
    "Roma": "Europa",
    "Parigi": "Europa",
    "Tokyo": "Asia",
    "New York": "America"
   }

#.map sostiuisco ogni destinazione con categorie corrispondente --> nuova colonna con Europa/Asia/America
df["Categoria"] = df["Destinazione"].map(categoria_dest)

#incasso totale
incasso_per_cat = df.groupby("Categoria")["Incasso"].sum()
print("Incasso totale per categoria:")
print(incasso_per_cat)

#incasso per categoria
durata_media_cat = df.groupby("Categoria")["Durata"].mean()
print("\nDurata media per categoria:")
print(durata_media_cat)

#salvo DataFrame in CSV
df.to_csv("prenotazioni_analizzate.csv")

#Parte 7 — Estensioni----------------------------------------------------------------------------------------

def top_clienti(df, n=3):
    return df["Cliente"].value_counts().head(n)

print("Top clienti:")
print(top_clienti(df, 3))

#barra
incasso_medio_cat = df.groupby("Categoria")["Incasso"].mean()
#linea
durata_media_cat = df.groupby("Categoria")["Durata"].mean()

categorie = incasso_medio_cat.index

fig, ax1 = plt.subplots()

#due assi incasso(€) - durata (giorni) sono scale diverse
# Barre: incasso medio
ax1.bar(categorie, incasso_medio_cat.values)
ax1.set_xlabel("Categoria")
ax1.set_ylabel("Incasso medio (€)")
ax1.set_title("Incasso medio e durata media per categoria")

#secondo asse asse y per linea
ax2 = ax1.twinx()
ax2.plot(categorie, durata_media_cat.loc[categorie].values, marker="o")
ax2.set_ylabel("Durata media (giorni)")

plt.show()

print(df[["Destinazione", "Categoria"]])
