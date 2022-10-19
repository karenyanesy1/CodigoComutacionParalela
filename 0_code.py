import time #pip install time
#from threading import Thread

def npar(n):
    time_ini = time.time()
    for i in range(n):
        if i % 2 == 0:
            print(i)
       
    #print("Inicio_")
    time.sleep(1)
    #print("Computación Paralela")
    #print ("Fin_")
    time_end = time.time()
    total = time_end - time_ini
    print(total)

npar(10)
#for i in range(5):
    #holamundo()