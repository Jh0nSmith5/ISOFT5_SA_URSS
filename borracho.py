import time

def tomar(nombre):
    print(f"{nombre} tomando cerveza...")
    time.sleep(1)
    print(f"{nombre} dejo de tomar")

def usar_baño(nombre):
    print(f"{nombre} orinando...")
    time.sleep(1)
    print(f"{nombre} salió del baño.")

def cantar(nombre):
    print(f"{nombre} cantando...")
    time.sleep(1)
    print(f"{nombre} dejo de cantar")

def llamar(nombre):
    print(f"{nombre} llamando a su ex...")
    time.sleep(1)
    print("Llamada rechazada")

def borrachito(nombre1,nombre2,nombre3,nombre4,nombre5):
        tomar(nombre1)
        time.sleep(1)
        usar_baño(nombre2)
        time.sleep(1)
        cantar(nombre3)
        time.sleep(1)
        llamar(nombre4)
        time.sleep(1)
        tomar(nombre5)
        time.sleep(1)
        print("Fin de un ciclo...")

borrachito("Andres", "Jhonat", "Cesar", "Brenda", "Victor")
time.sleep(1)
borrachito("Cesar", "Brenda", "Jhonat", "Victor", "Andres")
time.sleep(1)
borrachito("Brenda", "Victor", "Andres", "Jhonat", "Cesar")
time.sleep(1)
borrachito("Victor", "Andres", "Cesar", "Brenda", "Jhonat")
time.sleep(1)

#si
