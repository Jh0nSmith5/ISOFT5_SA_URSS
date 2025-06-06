#wena noshe
import re

users = {
    "admin": "admin@example.com"
}

menu_items = {
    "hamburguesa": "35.00",
    "hot dog": "25.00",
    "refresco": "20.00",
    "agua fresca": "20.00"
}

def selector():
    print("\nBienvenido a Gordiburger - ¡Tu lugar favorito para comer!\n")
    print("¿Tiene cuenta? [S/N]")
    respuesta = input().upper().strip()
    if respuesta == "S":
        login()
    elif respuesta == "N":
        signup()
    else:
        print("Opción inválida")
        selector()

def validacion_user(user):
    while user in users or not re.search(r'[A-Za-z]', user) or user.isdigit():
        if user in users:
            print("Usuario ya existente. Por favor elige otro usuario.")
        elif user.isdigit():
            print("El nombre de usuario no puede ser solo números. Debe contener letras.")
        elif not re.search(r'[A-Za-z]', user):
            print("El nombre de usuario debe contener al menos una letra.")
        user = input("Ingresa otro usuario: ")
    return user

def validacion_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    while not re.match(pattern, email):
        print("Correo inválido. Intenta de nuevo.")
        email = input("Ingresa un correo electrónico válido: ")
    return email

def login():
    print("Ingresa usuario:")
    user = input()
    if user in users:
        print(f'\nBienvenido a Gordiburg {user}\n')
        opciones()
    else:
        print("Usuario no encontrado.")
        login()

def signup():
    print("Ingresa usuario:")
    user = input()
    user = validacion_user(user)
    print("Ingresa correo electrónico:")
    email = input()
    email = validacion_email(email)
    users[user] = email
    print("Usuario registrado exitosamente.")
    selector()

def opciones():
    print("1. Menú")
    print("2. Salir")
    opcion = input("Elige una opción: ")
    if opcion == "1":
        menu()
    elif opcion == "2":
        exit()
    else:
        print("Opción inválida")
        opciones()

def menu():
    total_carrito = 0.0
    while True:
        print("\n---------- Menú ----------")
        for i, (item, precio) in enumerate(menu_items.items(), start=1):
            print(f"{i}. {item} - ${precio}")
        print("0. Pagar")
        opcion = input("Elige una opción: ")
        try:
            opcion = int(opcion)
            if opcion == 0:
                print("\nRealizando pago...")
                print(f"Total a pagar: ${total_carrito:.2f}")
                break
            elif 1 <= opcion <= len(menu_items):
                selected_item = list(menu_items.keys())[opcion - 1]
                precio_item = float(menu_items[selected_item])
                total_carrito += precio_item
                print(f"Has agregado {selected_item} por ${precio_item:.2f} al carrito.")
                print(f"Total acumulado: ${total_carrito:.2f}")
            else:
                print("Opción inválida.")
        except ValueError:
            print("Opción inválida. Ingresa un número.")
    print("Gracias por tu orden. Vuelve pronto.")
    exit()

print("=======================================")
print("    ¡Bienvenido a Gordiburg! 🍔🌭🥤    ")
print("=======================================")

selector()
