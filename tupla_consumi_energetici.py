tupla_consumi_energetici = (
    ("Milano", [
        ("gennaio", ("elettrico", 300)),
        ("gennaio", ("gas", 150)),
        ("febbraio", ("elettrico", 280)),
        ("febbraio", ("gas", 120)),
        ("marzo", ("elettrico", 290)),
        ("marzo", ("gas", 130)),
        ("aprile", ("elettrico", 270)),
        ("aprile", ("gas", 140)),
        ("maggio", ("elettrico", 285)),
        ("maggio", ("gas", 135)),
        # Aggiungi altri mesi e consumi
    ]),
    ("Brescia", [
        ("gennaio", ("elettrico", 280)),
        ("gennaio", ("gas", 140)),
        ("febbraio", ("elettrico", 260)),
        ("febbraio", ("gas", 130)),
        ("marzo", ("elettrico", 290)),
        ("marzo", ("gas", 130)),
        ("aprile", ("elettrico", 310)),
        ("aprile", ("gas", 120)),
        ("maggio", ("elettrico", 295)),
        ("maggio", ("gas", 145)),
        # Aggiungi altri mesi e consumi
    ]),
    # Aggiungi altre città
     ("Como", [
        ("gennaio", ("elettrico", 280)),
        ("gennaio", ("gas", 140)),
        ("febbraio", ("elettrico", 260)),
        ("febbraio", ("gas", 130)),
        ("marzo", ("elettrico", 290)),
        ("marzo", ("gas", 130)),
        ("aprile", ("elettrico", 310)),
        ("aprile", ("gas", 120)),
        ("maggio", ("elettrico", 295)),
        ("maggio", ("gas", 145)),
        # Aggiungi altri mesi e consumi
    ]),
)
#Definisci una funzione analizza_consumi_energetici che riceva come parametro il nome della città e il nome della risorsa energetica e 
# restituisca una tupla con la seguente struttura:
def analizza_consumi_energetici(citta, risorsa):
    # Restituisci una tupla con la seguente struttura
    # (media_risorsa, (max_risorsa, meseMax_risorsa)
    media_risorsa=0
    max_risorsa=0
    meseMax_risorsa=0
    cont+=0
    contM=0
    for citta,dati in tupla_consumi_energetici:
        cont+=1
        for mese,*risorsa,costo in dati: 
           contM+=costo 
           if(risorsa=="eletrico"):              
                if(max_risorsa<costo):
                    max_risorsa=costo
            
                if(risorsa=="gas"):              
                    if(max_risorsa<costo):
                        max_risorsa=costo      
        if(citta=="Milano"):
               if(max_risorsa>costo):
                   meseMax_risorsa=max_risorsa
        if(citta=="Brescia"):
               if(max_risorsa>costo):
                   meseMax_risorsa=max_risorsa

        if(citta=="Como"):
               if(max_risorsa>costo):
                   meseMax_risorsa=max_risorsa    
        media_risorsa=contM/cont
        


        return(media_risorsa, (max_risorsa, meseMax_risorsa))
   
citta=input("inserisci la citta che vuoi visualizzare:")
risorsa=input("inserisci la risorsa che vuoi visualizzare:")
# Esempio di utilizzo

risultato_analisi = analizza_consumi_energetici("Milano", "elettrico")
print(risultato_analisi)

