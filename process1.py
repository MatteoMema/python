from multiprocessing import Process
"""
multiprocessing è una libreria per la creazione,la comunicazione e la sincronizazzione
tra processi nella programmazione parallela e concorrente
Process è una classe per creare processi eseguendo una funzione(o metodo)specificata come target.
"""

def process_function(data):
    result = data * 2
    print(result)

if__name__="_main_":
    data_list = [1, 2, 3, 4]
    processes=[]

    for data in data_list:
    p = Process(target=process_function,args=(data,))
    processes.append(p)
    p.start() #avvia l'esecuzione processo separato


    for p in processes:
        p.join()#Blocca il processa principale fino a quando il proceso separato non termina





