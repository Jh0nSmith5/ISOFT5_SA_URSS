
#? Este proyecto representa la versión 2 de la aplicación Scorpions Foods:

#* 1.- Aqui se realiza el mensaje de bienvenida y el menú de la aplicación.
#* 2.- Se registra al usuario solicitando su nombre y correo electrónico con una validación sencilla.

import time 

#! Aqui se realiza el mensaje de bienvenida y el menú de la aplicación.
def imprimir_bienvenida_y_menu():
    print("🦂🦂 Bienvenido(a) a la App ScorpionsFood 🦂🦂\n")
    time.sleep(2)
    print("El menú es el siguiente:")
    print("  1.- Escorpión al chocolate 🍫🦂")
    print("  2.- Escorpión a la mexicana 🍽️🌶️🦂")
    print("  3.- Escorpión a la KFC 🍗🍟🦂\n")

#! validar_email_simple recibe un parámetro email que debería ser un str (cadena) y devuelve un valor de tipo (booleano).
## Debe contener exactamente un '@'.
## Parte local y dominio no vacíos.
## El dominio debe tener al menos un punto '.'.
## En el dominio solo se permiten letras, números, guiones '-' y puntos '.'.

def validar_email(email: str) -> bool:

    if email.count("@") != 1: #! exactamente un '@'
        return False
    
    parte_local, parte_dominio = email.split("@", 1)

    if not parte_local or not parte_dominio: #! no puede estar vacío
        return False

    if "." not in parte_dominio: #! dominio debe tener al menos un punto
        return False

    #! for c in parte_dominio: #! caracteres permitidos en el dominio
    ## c.isalnum() --> metodo que verifica si el carácter es alfanumérico (letra o número).
    ## c i n "-." --> verifica si el carácter es un guion o un punto.
    ## (c.isalnum() or c in "-.") verifica si el carácter es alfanumérico o un guion/punto.
    ## if not (c.isalnum() or c in "-.") detecta si hay un carácter no permitido.
    for c in parte_dominio:     
        if not (c.isalnum() or c in "-."):
            return False

    #! TLD no vacío (lo que va después del último punto)
    ## 1.- Genericos (gTLD): .com, .net, .org, .info, .xyz
    ## 2.- Nacionales (ccTLD): .mx, .es, .fr, .uk, .jp
    ## 3.- Patrocinados (sTLD): .edu, .gov, .mil, .int
    if not parte_dominio.split(".")[-1]:
        return False
    return True

#! prompt: str) -> str: Recibe un parametro llamado prompt que debe ser una cadena de texto (str)
#! prompt es un mensaje que se muestra al usuario para solicitarle una entrada input ()

#todo: ¿que hace strip()?

def pedir_no_vacio(prompt: str) -> str:
    while True:
        val = input(prompt).strip() 
        if val:
            return val
        print("⚠️  Este campo no puede estar vacío. Intenta de nuevo.\n")

def registrar_usuario() -> None:
    nombre = pedir_no_vacio("Ingresa tu nombre: ")
    email = pedir_no_vacio("Ingresa tu correo electrónico: ")
    while not validar_email(email):
        print("⚠️ Correo electrónico inválido. Inténtalo de nuevo.")
        print("   Reglas:")
        print("   - Debe tener exactamente un '@'")
        print("   - El dominio debe tener al menos un punto (ej. dominio.com)")
        print("   - Después de '@' usa solo letras, números, '-' y '.'\n")
        email = pedir_no_vacio("Ingresa tu correo electrónico: ")
    print(f"✅ Usuario '{nombre}' registrado con éxito. Correo: {email}")

def main() -> None:
    imprimir_bienvenida_y_menu()
    registrar_usuario()
    print("\nGracias por visitar ScorpionsFood. ¡Buen provecho! 🦂")

#todo: ¿que hace aqui)?
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nSaliendo... ¡Hasta pronto!")