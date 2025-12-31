# Definire le variabili necessarie per rappresentare:
# Nome, cognome e codice fiscale di un paziente (stringhe).
# Età e peso del paziente (interi e float).
# Lista delle analisi effettuate (lista di stringhe).
# Creare una classe Paziente con:
# Attributi: nome, cognome, codice_fiscale, eta, peso, analisi_effettuate.
# Metodo scheda_personale() che restituisca una stringa con i dati principali del paziente.
# Creare una classe Medico con:
# Attributi: nome, cognome, specializzazione.
# Metodo visita_paziente(paziente) che stampi quale medico sta visitando quale paziente.
# Creare una classe Analisi che contenga:
# Tipo di analisi (es. glicemia, colesterolo).
# Risultato numerico.
# Metodo valuta() che stabilisca se il valore è nella norma (criteri inventati da voi).Parte 3 – Uso di NumPy
# Supponiamo che il centro raccolga i risultati di un certo esame per 10 pazienti.
# Rappresentare i valori in un array NumPy.
# Calcolare con NumPy: media, valore massimo, valore minimo e deviazione standard.
# Parte 4 – Integrazione OOP + NumPy
# Aggiornare la classe Paziente inserendo un attributo risultati_analisi che sia un array NumPy contenente i valori numerici delle analisi svolte.
# Creare un metodo statistiche_analisi() che calcoli:
# Media dei valori
# Minimo e massimo
# Deviazione standard
# utilizzando NumPy.
# Parte 5 – Applicazione completa
# Creare un piccolo programma principale (main) che:
# Inserisca almeno 3 medici e 5 pazienti.
# Ogni paziente deve avere almeno 3 risultati di analisi.
# Stampi la scheda di ogni paziente.
# Mostri quale medico visita quale paziente.
# Stampi le statistiche delle analisi per ciascun paziente.

import numpy as np

#-------------variabili e tipi di dati---------------------------------#

nome = "Paolo"
cognome = "Rossi"
codice_fiscale = "RSSPLA88L08E514E"
eta = 37
peso = 76.5
analisi_effettuate = ["emoglobina", "linfociti", "ferritina"]

#-------------------classi e OOP---------------------------------------#

class Paziente:
    def __init__(self, nome, cognome, codice_fiscale, eta, peso, analisi_effettuate, risultati_analisi):
        self.nome = nome
        self.cognome = cognome
        self.codice_fiscale = codice_fiscale
        self.eta = eta
        self.peso = peso
        self.analisi_effettuate = analisi_effettuate

        self.risultati_analisi = np.array(risultati_analisi, dtype=float)
    

    def scheda_personale(self):
        return (f"dati paziente: nome: {self.nome}. cognome: {self.cognome}. codice fiscale: {self.codice_fiscale}. anni: {self.eta}. peso: {self.peso}. analisi effettuate:{self.analisi_effettuate}.")
    
#--------------------- Integrazione OOP + NumPy ---------------------#

    def statistiche_analisi(self):
        print("Media:", np.mean(self.risultati_analisi))
        print("Min:", np.min(self.risultati_analisi))
        print("Max:", np.max(self.risultati_analisi))
        print("Deviazione standard:", np.std(self.risultati_analisi))


# paziente_2 = Paziente("Paolo", "Rossi", "RSSPLA88L08E514E", 37, 76.5, ["emoglobina", "linfociti", "ferritina"])
# print(paziente_2.scheda_personale())

class Medico:
    def __init__(self,nome, cognome, specializzazione):
        self.nome = nome
        self.cognome = cognome
        self.specializzazione = specializzazione

    def visita_paziente(self, paziente):
        print(f"Il medico {self.nome} {self.cognome} specializzato in {self.specializzazione} sta visitando il paziente {paziente.nome} {paziente.cognome}")

class Analisi:
    def __init__(self, tipo_analisi, valore_analisi):
        self.tipo_analisi = tipo_analisi
        self.valore_analisi = valore_analisi

    def valuta(self):
        if 50 <= self.valore_analisi <= 100:
            print(f"{self.tipo_analisi}: valori nella norma")
        else:
            print(f"{self.tipo_analisi}: valori fuori norma")

p = Paziente("Paolo", "Rossi", "RSS...", 37, 76.5,
             ["glicemia", "emoglobina", "ferritina"],
             [49, 140, 80])

p.statistiche_analisi()

paziente_1 = Paziente("Paolo", "Rossi", "RSSPLA88L08E514E", 37, 76.5, [], [])
medico_1 = Medico("Francesco", "Verdi", "Cardiologia")           
medico_1.visita_paziente(paziente_1)


analisi_1 = Analisi("glicemia", 49)
analisi_2 = Analisi("emoglobina", 140)
analisi_3 = Analisi("ferritina", 80)

analisi_1.valuta()
analisi_2.valuta()
analisi_3.valuta()

#--------------------------------uso di Numpy---------------------------------#

risultato_10_pazienti = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], dtype=float)

print("Media:", np.mean(risultato_10_pazienti)) 
print("Min:", np.min(risultato_10_pazienti))
print("Max:", np.max(risultato_10_pazienti))
print("Deviazione standard:", np.std(risultato_10_pazienti))

#------------------------------- Integrazione OOP + NumPy -----------------------#
def main():
    medici = [Medico("Francesco", "Verdi", "Cardiologia"), 
              Medico("Luca", "Rossi", "Endocrinologia"),
              Medico("Silvia", "Bianchi", "Nerurologia")]
    
    pazienti = [
        Paziente("Paolo", "Rossi", "RSSPLA88L08E514E", 37, 76.5, 
        ["glicemia", "colesterolo", "trigliceridi"], 
        np.array([92, 110, 200])),
    
        Paziente("Sara", "Conti", "CNTSRA90A01F205X", 35, 60.2, 
        ["glicemia", "colesterolo", "trigliceridi"], 
        np.array([80, 15, 999])),

        Paziente("Marta", "Greco", "GRCMRT92D45L219Z", 33, 55.8,
        ["glicemia", "colesterolo", "trigliceridi"], 
        np.array([85, 150, 99])), 

        Paziente("Luca", "Fontana", "FNTLCU85C12H501B", 40, 82.0, 
        ["glicemia", "colesterolo", "trigliceridi"], 
        np.array([605, 1, 1190])), 

        Paziente("Davide", "Riva", "RVADVD88E20M052Q", 36, 90.3, 
        ["glicemia", "colesterolo", "trigliceridi"], 
        np.array([110, 200, 110]))] 

    for i, paziente in enumerate(pazienti):
        medico = medici[i % len(medici)]

        print(paziente.scheda_personale())
        medico.visita_paziente(paziente)
        paziente.statistiche_analisi() 

main()        
    



        