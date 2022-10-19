import time #pip install time
from threading import Thread
from tkinter import N

def npar(n):
    time_ini = time.time()
    for i in range (n):
        if i % 2 == 0:
            print(i)
npar(1000)  
 
#def holamundo():
time_ini = time.time()
print("Inicio:",time_ini)

    #Proceso
    #i = 0

    #for _ in range(10):
       #i += 1
    #print("Hola mundo")
    #Proceso
    #print ("Fin_")
#time_end = time.time()
#total = time_end - time_ini
#print(total)
    

for i in range(0):
    t = Thread(target=npar(1000), args=()) #target nombre de la funcion
    t.start()
    
npar(1000)
time_end = time.time()
print("Final: ",time_end)
total = time_end - time_ini
print("total: ", total)