import re

class gordiburg:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    def __init__(self):
        if hasattr(self, "users"):
            return
        self.users = {
            "admin": "admin@example.com"
        }

        self.menu_items = {
            "hamburguesa": "35.00",
            "hot dog": "25.00",
            "refresco": "20.00",
            "agua fresca": "20.00"
        }

    def selector(self):
        print("\nBienvenido a Gordiburger - ¡Tu lugar favorito para comer!\n")
        print("¿Tiene cuenta? [S/N]")
        respuesta = input().upper().strip()
        if respuesta == "S":
            self.login()
        elif respuesta == "N":
            self.signup()
        else:
            print("Opción inválida")
            self.selector()

    def validacion_user(self, user):
        while user in self.users or not re.search(r'[A-Za-z]', user) or user.isdigit():
            if user in self.users:
                print("Usuario ya existente. Por favor elige otro usuario.")
            elif user.isdigit():
                print("El nombre de usuario no puede ser solo números. Debe contener letras.")
            elif not re.search(r'[A-Za-z]', user):
                print("El nombre de usuario debe contener al menos una letra.")
            user = input("Ingresa otro usuario: ")
        return user

    def validacion_email(self, email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        while not re.match(pattern, email):
            print("Correo inválido. Intenta de nuevo.")
            email = input("Ingresa un correo electrónico válido: ")
        return email

    def login(self):
        print("Ingresa usuario:")
        user = input()
        if user in self.users:
            print(f'\nBienvenido a Gordiburg {user}\n')
            self.opciones()
        else:
            print("Usuario no encontrado.")
            self.login()

    def signup(self):
        print("Ingresa usuario:")
        user = input()
        user = self.validacion_user(user)
        print("Ingresa correo electrónico:")
        email = input()
        email = self.validacion_email(email)
        self.users[user] = email
        print("Usuario registrado exitosamente.")
        self.selector()

    def opciones(self):
        print("1. Menú")
        print("2. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            self.menu()
        elif opcion == "2":
            exit()
        else:
            print("Opción inválida")
            self.opciones()

    def menu(self):
        total_carrito = 0.0
        while True:
            print("\n---------- Menú ----------")
            for i, (item, precio) in enumerate(self.menu_items.items(), start=1):
                print(f"{i}. {item} - ${precio}")
            print("0. Pagar")
            opcion = input("Elige una opción: ")
            try:
                opcion = int(opcion)
                if opcion == 0:
                    print("\nRealizando pago...")
                    print(f"Total a pagar: ${total_carrito:.2f}")
                    break
                elif 1 <= opcion <= len(self.menu_items):
                    selected_item = list(self.menu_items.keys())[opcion - 1]
                    precio_item = float(self.menu_items[selected_item])
                    total_carrito += precio_item
                    print(f"Has agregado {selected_item} por ${precio_item:.2f} al carrito.")
                    print(f"Total acumulado: ${total_carrito:.2f}")
                else:
                    print("Opción inválida.")
            except ValueError:
                print("Opción inválida. Ingresa un número.")
        print("Gracias por tu orden. Vuelve pronto.")
        self.selector()

print("=======================================")
print("    ¡Bienvenido a Gordiburg! 🍔🌭🥤    ")
print("=======================================")

sistema = gordiburg()
sistema.selector()