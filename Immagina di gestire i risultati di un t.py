#Immagina di gestire i risultati di un torneo sportivo attraverso una tupla contenente le informazioni sulle partite. 
#Ogni voce della tupla rappresenta una partita e contiene le seguenti informazioni: squadra di casa, squadra ospite, 
#punteggio della squadra di casa, punteggio della squadra ospite.
tupla_partite = (
    ("SquadraA", "SquadraB", 3, 2),
    ("SquadraC", "SquadraD", 1, 1),
    ("SquadraB", "SquadraC", 2, 4),
    ("SquadraD", "SquadraA", 0, 3),
    ("SquadraB", "SquadraD", 1, 2),
)
#Definisci le seguenti funzioni utilizzando le funzioni predefinite sum, min, max per le liste:
#media_gol_partite(tupla_partite): una funzione che accetti come parametro la tupla delle partite e restituisca la media dei gol segnati in tutte le partite.
#media_gol_squadra(tupla_partite, squadra): una funzione che accetti come parametri la tupla delle partite e il nome di una squadra, e restituisca la media dei gol segnati dalla squadra in tutte le partite in cui ha partecipato.
#partita_con_piu_gol(tupla_partite): una funzione che restituisca una tupla contenente la partita con il maggior numero di gol segnati e i relativi punteggi.
#partita_con_meno_gol(tupla_partite): una funzione che restituisca una tupla contenente la partita con il minor numero di gol segnati e i relativi punteggi.
#percentuale_vittorie_squadra(tupla_partite, squadra): una funzione che restituisca la percentuale di partite vinte dalla squadra rispetto al totale delle partite disputate.
#Prevedi un menu di scelta che consenta all'utente di selezionare un'operazione tra le opzioni disponibili.
Sgol=0
Mgol=0
SgolA=0
SgolB=0
SgolC=0
SgolD=0
for squadre,reti in tupla_partite:
    for squadra1,squadra2 in squadre:
        for reti1,reti2 in reti:
            Sgol+=reti1+reti2
            if(squadra1=="SquadraA"):
                SgolA+=reti1
            if(squadra2=="SquadraA"):
                SgolA+=reti2
            if(squadra1=="SquadraB"):
                SgolB+=reti1
            if(squadra2=="SquadraB"):
                SgolB+=reti2
            if(squadra1=="SquadraC"):
                SgolC+=reti1
            if(squadra2=="SquadraC"):
                SgolC+=reti2
            if(squadra1=="SquadraD"):
                SgolD+=reti1
            if(squadra2=="SquadraD"):
                SgolD+=reti2


print("1)media gol tutte di tutte le partite")
print("2)media gol di ogni squadra")
print("3)media gol di ogni squadra")
print("4)partita con più gol")
print("5)partita con meno gol")
scelta=input("Inserisci opzione che vuoi scegliere:")
if(scelta==1):
    print("la media dei gol segnati in ogni partita è:",Mgol=Sgol/6)
if(scelta==2):
    scelta2=input("inserisci la squadra:")
    if(scelta2=="SquadraA"):
        print("Il totale dei gol segnati dalla squadraA è:",SgolA)
    if(scelta2=="SquadraB"):
        print("Il totale dei gol segnati dalla squadraA è:",SgolB)
    if(scelta2=="SquadraC"):
        print("Il totale dei gol segnati dalla squadraA è:",SgolC)
    if(scelta2=="SquadraD"):
        print("Il totale dei gol segnati dalla squadraA è:",SgolD)
            
     
     
            