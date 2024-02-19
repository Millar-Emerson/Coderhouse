usuarios={"usuario":"contra","usuario1":"1234","usuario2":"12345"}


def registro():
    usuario=input("ingrese usuario")
    if usuario in usuarios:
        print("El usuario ya existe. Por favor, elige otro.")
        return
    contraseña=input("ingrese contraseña")
    usuarios[usuario]=contraseña
    print("Usuario registrado exitosamente.")

def login():
    intentos=3
    while intentos > 0:
        usuario=input("ingrese usuario")
        contraseña=input("ingrese contraseña")
        if usuario in usuarios and usuarios[usuario] == contraseña:
            print("¡Inicio de sesión exitoso!")
            return
        else:
            intentos-=1
            print("¡usuario y contraseña incorrecto! Por favor, inténtalo nuevamente.")
    print("Se agotaron los intentos. Por favor, contacta al administrador.")
    
def borrar_usuario():
    usuario_a_borrar = input("Ingresa el nombre de usuario que deseas borrar: ")
    if usuario_a_borrar in usuarios:
        del usuarios[usuario_a_borrar]
        print("Usuario eliminado exitosamente.")
    else:
        print("El usuario ingresado no existe.")
        
        
def ver_usuarios():
    print("Usuarios registrados:")
    for usuario in usuarios:
        print(usuario)
        
def seleccionar_opcion(opcion):
    if opcion == "1":
        registro()
    elif opcion == "2":
        login()
    elif opcion == "3":
        borrar_usuario()
    elif opcion=="4":
        ver_usuarios()
    else:
        print("Opción no válida.")
        
        
while opcion!="0":
    opcion=input("ingrese una opcion")
    seleccionar_opcion(opcion)