# Progetto 1

# Progetto: Gestione Biblioteca Digitale
# Traccia
# In una biblioteca digitale si vuole realizzare un piccolo sistema software per gestire libri, utenti e prestiti.Il programma deve sfruttare variabili, tipi di dati, strutture di controllo e soprattutto la programmazione orientata agli oggetti (OOP).
#  Consegna 





# Parte 1 – Variabili e tipi di dati

# Dichiarare e stampare alcune variabili di esempio:
# Titolo di un libro (stringa)
# Numero di copie disponibili (intero)
# Prezzo medio di un libro (float)
# Stato "disponibile/non disponibile" (booleano)(Esempio: titolo = "Il Signore degli Anelli", copie = 5, ecc.)

titolo_libro = "19Q4"
numero_copie = 1000
prezzo_medio = 22.50
stato_disponibile = True

# print("Titolo:", titolo_libro)
# print("copie:", numero_copie)
# print("prezzo medio:", prezzo_medio)
# print("disponibilità:", stato_disponibile)

# Parte 2 – Strutture dati

# Creare una lista con almeno 5 titoli di libri.
# Creare un dizionario che mappi il titolo del libro al numero di copie disponibili.
# Creare un insieme (set) che contenga tutti gli utenti registrati alla biblioteca.

lista_libri = [
    "19Q4",
    "La fondazione",
    "Se questo è un uomo",
    "La casa",
    "Nel segno della pecora",
]

dizionario_libri = {
    "19Q4": 5,
    "La fondazione": 1,
    "Se questo è un uomo": 9,
    "Neuromante": 1,
    "Nel segno della pecora": 6,
}

set_utenti_registrati = {
    "Mario Rossi",
    "Silvia Verdi",
    "Maria Verdi",
    "Paolo Bianchi",
}

# print("lista Libri:", lista_libri)
# print("numero copie:", dizionario_libri)
# print("utenti registrati:", set_utenti_registrati)

# Parte 3 – Classi e OOP

# Creare una classe Libro con attributi:
# titolo
# autore
# anno
# copie_disponibili

# Aggiungere un metodo info() che restituisca una stringa descrittiva del libro.
# Creare una classe Utente con attributi:
# nome
# eta
# id_utente
# Aggiungere un metodo scheda() che stampi i dati dell’utente.

# Creare una classe Prestito che colleghi un Utente a un Libro e contenga:
# utente (oggetto Utente)
# libro (oggetto Libro)
# giorni (numero di giorni del prestito)
# Aggiungere un metodo dettagli() che stampi tutte le informazioni sul prestito.

class Libro:
    def __init__(self,titolo, autore, anno, copie_disponibili):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.copie_disponibili = copie_disponibili

    def info(self):
         return f"{self.titolo} di {self.autore} - anno di uscita: {self.anno}. Copie disponibili: {self.copie_disponibili}"   
    
class Utente:
    def __init__(self, nome, eta, id_utente):
        self.nome = nome
        self.eta = eta    
        self.id_utente = id_utente

    def scheda(self):
        print(f"nome: {self.nome}, anni: {self.eta}, id_utente: {self.id_utente}")

class Prestito:
    def __init__(self, utente, libro, giorni):
        self.utente = utente
        self.libro = libro
        self.giorni = giorni

    def dettagli(self):
        print(f"prestito: {self.utente.nome} ha noleggiato {self.libro.titolo} per {self.giorni} giorni.")

libro1 = Libro("19Q4", "Haruki Murakami", 2009, 5)
libro2 = Libro("La fondazione", "Isaac Asimov", 1942, 1)
libro3 = Libro("Se questo è un uomo", "Primo Levi", 1947, 9)
libro4 = Libro("Neuromante", "William Gibson", 1984, 1)
libro5 = Libro("Nel segno della pecora", "Haruki Murakami", 1982, 6)

print()
print(libro1.info())
print(libro2.info())
print(libro3.info())
print(libro4.info())
print(libro5.info())
print()

utente1 = Utente("Mario Rossi", 35, "MRO0951")
utente2 = Utente("Silvia Verdi", 19, "SVE1015")
utente3 = Utente("Maria Verdi", 59, "MVE0475")
utente4 = Utente("Paolo Bianchi", 79, "PBI0098")

utente1.scheda()
utente2.scheda()
utente3.scheda()
utente4.scheda()
print()


# Parte 4 – Funzionalità
# Creare una funzione presta_libro(utente, libro, giorni) che:
# Verifichi se il libro ha almeno 1 copia disponibile
# Se sì → riduca il numero di copie e crei un nuovo oggetto Prestito
# Se no → stampi un messaggio di errore
# Simulare almeno 3 prestiti con utenti e libri diversi.
# Stampare a video:
# L’elenco aggiornato delle copie disponibili per ciascun libro
# I dettagli di ogni prestito effettuato

def presta_libro(utente, libro, giorni):
    if libro.copie_disponibili > 0:
        libro.copie_disponibili -= 1
        prestito = Prestito(utente, libro, giorni)
        print(f"Prestito effettuato da {utente.nome}. Libro: {libro.titolo}. Giorni: {giorni}")
        return prestito
    else:
        print(f"Errore! nessuna copia disponibile : {libro.titolo}")
        return None
    
lista_libri = [libro1, libro2, libro3, libro4, libro5]
lista_prestiti=[]

p1 = presta_libro(utente1, libro1, 15)
if p1 is not None:
    lista_prestiti.append(p1)

p2 = presta_libro(utente2, libro4, 12)
if p2 is not None:
    lista_prestiti.append(p2)


p3 = presta_libro(utente3, libro4, 2)
if p3 is not None:
    lista_prestiti.append(p3)

p4 = presta_libro(utente4, libro2, 5)
if p4 is not None:
    lista_prestiti.append(p4)

print()

for libro in lista_libri:
    print("copie disponibili: ", libro.info())
    print()

for prestito in lista_prestiti:
    prestito.dettagli()
    print()

    

    











    
            