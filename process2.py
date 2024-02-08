import os
from multiprocessing import Process,Queue,current_process
"""-- Queue:classe che rappresenta una coda condivisa tra processi.
È utilizzata per  consetire la comunicazione tra processi,
consentendo loro di scambiarsi dati in modo sicuro.
put(item):Aggiunge un elemento alla coda.
get():Rimuove e restituisce un elemento dalla coda.
empty():Restituisce True se la coda è vuota,altrimenti restitusce False.
full():Restituisce  True se la coda è piena,altrimenti restitusce False.
qsize():Restitusce il numero di elementi presenti nella coda.
close():Chiude la coda.
-- current_procces: funzione che restituisce un oggetto Process
che rappresenta il processo in esecuzione."""
def process_id():
    print(f"sever PID: {os.getpid()}, Process Name:{ current_process().name}, Procces PID: {current_process().pid}")

    def process_id():
        print(f"Server PID: {os.getpid()}, Process Name: { current_process().name}, Process PID: }current_process().pid}")


    def process_function(data, sesult_queue):
        process_id()
        process_id()
        print("Elabora:",data)
        result=data*2
        result_queue.put(result)


    if __name__=="_main_":
        data_list=[1,2,3,4]
        result_queue=Queue()
        result_queue=Queue()
        processes=[]

        for data in data_list:
            p=Process(target=process_function,args=(data,result_queue))
            processes.append(p)
            p.start()


            for p in processes:
                p.join()


            print("il main stampa i risultati")
            while not result_queue.empty():
                result=result_queue.get()
                print(result)