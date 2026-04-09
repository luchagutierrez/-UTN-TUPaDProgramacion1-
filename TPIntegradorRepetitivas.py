#Ejercicio 1
# Pedir nombre
nombre = input("Ingresá tu nombre: ")
#validar que no este vacío y que sean solo letras
while nombre == "" or not nombre.isalpha():
    print("Nombre inválido. Ingresá solo letras y que no esté vacío.")
    nombre = input("Ingresá tu nombre: ")

#pedir cantidad de productos
cantidad_de_productos = input("Ingrese cantidad de productos: ")
#Validar que sea numero y que sea positivo 
while not cantidad_de_productos.isdigit() or int(cantidad_de_productos) <= 0:
    print("Cantidad inválida. Ingrese un número mayor a cero")
    cantidad_de_productos= input("Ingrese cantidad de productos: ")
cantidad_de_productos = int(cantidad_de_productos)

#Generar contadores en 0, para devolver precio con y sin descuentos
total_sin_descuento = 0
total_descuentos = 0 

#For para cada producto
for i in range(cantidad_de_productos):
    print(f"Producto {i+1}")
#Precio de cada producto
    precio_producto=input("Ingrese precio del producto: ")
    while not precio_producto.isdigit() or int(precio_producto)<=0: #Validar que sea entero y que sea un número
        print("Ingresá solo números enteros")
        precio_producto=input("Ingrese precio del producto: ")
    precio = int (precio_producto)
    descuento = input("¿Tiene descuento? S/N: ")  #Preguntar si tiene descuento (S/N) y validar: uso lower para convertir a minuscula y not in para que valide solo con esas variables
    while descuento.lower() not in ["s", "n"]:
        print("Error. Ingrese S/N")
        descuento=input("¿Tiene descuento? S/N: ")
    if descuento.lower() == "s": #Aplicar descuento si corresponde, sino dejarlo igual
        precio_final= precio*0.90
    else:
        precio_final=precio
    total_sin_descuento = total_sin_descuento + precio   #Parte final, conseguir totales con y sin descuento, ahorro y promedio. retomamos contadores y sumamos precio y precio_final a variables 
    total_descuentos = total_descuentos + precio_final
#Para ahorro, le restamos al total sin descuento (el nuevo valor que llegamos sumando) y los productos que si tenian
ahorro = total_sin_descuento - total_descuentos
#para promedio, retomamos la cantidad de productos y por ese numero dividimos el total_descuento. 
promedio = total_descuentos/cantidad_de_productos
#Mostrar resultados, usar :.2f para mostrar solo dos decimales en promedio
print(f"Cliente {nombre}")
print(f"Total sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_descuentos}")
print(f"Total ahorrado: ${ahorro}")
print(f"Promedio por productos: ${promedio:.2f}")

#Ejercicio 2
usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0
acceso = False

while intentos <3:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == usuario_correcto  and clave == clave_correcta: 
        print("Acceso concedido")
        acceso = True
        break
    else: 
        intentos = intentos + 1
        print(f"Usuario y/o clave incorrecta. te quedan {3 - intentos} intentos")
if not acceso:
    print("Acceso bloqueado")         
if acceso:
    while True:
        print("1) Estado 2) Cambiar clave 3) Mensaje 4) Salir")
        opcion = input("Opción: ")
        if not opcion.isdigit():
            print("Error: ingrese un número válido")
            continue

        opcion = int(opcion)

        if opcion < 1 or opcion > 4: 
            print("Error: opcion fuera de rango")
            continue
        
        if opcion == 1:
            print("Inscripto")

        elif opcion == 2:
            nueva = input("Nueva clave: ")
            confirmar = input("Confirmar clave: ")
            if len(nueva) < 6:
                print("Error: la clave debe tener al menos 6 caracteres")
            elif nueva != confirmar: 
                print("Error: las claves no coinciden")
            else:
                clave_correcta = nueva
                print("Clave actualizada correctamente")

        elif opcion == 3:
            print("¡Dale, que vos podes!")

        elif opcion == 4:
            print("Salir del sistema")
            break

#Ejercicio3
#Agenda de turnos con nombre

#Días - Turnos
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

#Operador
operador = input("Ingrese su nombre: ")

while not operador.isalpha():
    print("Ingrese solo letras")
    operador = input("Ingrese su nombre: ")

#Menu
while True:
    opcion = input("Elija una opción: 1)Reservar 2)Cancelar 3)Ver agenda 4)Resumen 5)Salir ") 
    if not opcion.isdigit():
        print("Ingrese un número")
        continue
    opcion = int(opcion)
    if opcion < 1 or opcion > 5:
        print("Opción inválida")
        continue
    if opcion == 1:
        dia = input("Lunes = 1, Martes = 2: ")
        if not dia.isdigit():
            print("Opción inválida")
            continue
        dia = int(dia)
        if dia != 1 and dia != 2:
            print("Opción inválida")
            continue
        dia = int(dia)
        nombre = input("Nombre del paciente")
        if not nombre.isalpha():
            print("Ingrese solo letras")
            continue
        if dia == 1:
            if lunes1.lower() == nombre.lower() or lunes2.lower() ==nombre.lower() or lunes3.lower() == nombre.lower() or lunes4.lower() == nombre.lower():
                print("Usted ya tiene turno")
            elif lunes1 == "":
                lunes1 == nombre
                print(f"Turno 1 del lunes reservado para", {nombre})
            elif lunes2 == "":
                lunes2 == nombre
                print(f"Turno 2 del lunes reservado para", {nombre})
            elif lunes3 == "":
                lunes3 == nombre
                print(f"Turno 3 del lunes reservado para", {nombre})
            elif lunes4 == "":
                lunes4 == nombre
                print(f"Turno 4 del lunes reservado para", {nombre})
            else:
                print("No hay turnos disponibles para el lunes")
        else:
            if martes1.lower() == nombre.lower() or martes2.lower() == nombre.lower() or martes3.lower() == nombre.lower():
                print("Usted ya tiene turno")
            elif martes1 == "":
                martes1 == nombre
                print(f"Turno 1 del martes reservado para", {nombre})
            elif martes2 == "":
                martes2 == nombre
                print(f"Turno 2 del martes reservado para", {nombre})
            elif martes3 == "":
                martes3 == nombre
                print(f"Turno 3 del martes reservado para", {nombre})
            else:
                print("No hay turnos disponibles para el martes")
    elif opcion == 2:
        dia = input("Elegí día (lunes=1, martes=2): ")
        if not dia.isdigit():
            print("Opción inválida")
            continue
        dia = int(dia)
        if dia != 1 and dia != 2:
            print("Opción inválida")
            continue
        nombre = input("Nombre del paciente: ")
        if not nombre.isalpha():
            print("Solo letras.")
            continue
        if dia == 1:
            if lunes1.lower() == nombre.lower():
                lunes1 = ""
                print(f"Turno de", {nombre}, "en lunes cancelado.")
            elif lunes2.lower() == nombre.lower():
                lunes2 = ""
                print(f"Turno de", {nombre}, "en lunes cancelado.")
            elif lunes3.lower() == nombre.lower():
                lunes3 = ""
                print(f"Turno de", {nombre}, "en lunes cancelado.")
            elif lunes4.lower() == nombre.lower():
                lunes4 = ""
                print(f"Turno de", {nombre}, "en lunes cancelado.")
            else:
                print(nombre, "no tiene turno el lunes.")
        else:
            if martes1.lower() == nombre.lower():
                martes1 = ""
                print(f"Turno de", {nombre}, "en martes cancelado.")
            elif martes2.lower() == nombre.lower():
                martes2 = ""
                print(f"Turno de", {nombre}, "en martes cancelado.")
            elif martes3.lower() == nombre.lower():
                martes3 = ""
                print(f"Turno de", {nombre}, "en martes cancelado.")
            else:
                print(nombre, "no tiene turno el martes.")
    elif opcion == 3:
        dia = input("Elegí día (lunes=1, martes=2): ")
        if not dia.isdigit():
            print("Opción inválida")
            continue
        dia = int(dia)
        if dia != 1 and dia != 2:
            print("Opción inválida")
            continue
        if dia == 1:
            print("Agenda Lunes")
            if lunes1 == "":
                print("  Turno 1: (libre)")
            else:
                print("  Turno 1:", lunes1)
            if lunes2 == "":
                print("  Turno 2: (libre)")
            else:
                print("  Turno 2:", lunes2)
            if lunes3 == "":
                print("  Turno 3: (libre)")
            else:
                print("  Turno 3:", lunes3)
            if lunes4 == "":
                print("  Turno 4: (libre)")
            else:
                print("  Turno 4:", lunes4)
        else:
            print("── Agenda Martes ──")
            if martes1 == "":
                print("  Turno 1: (libre)")
            else:
                print("  Turno 1:", martes1)
            if martes2 == "":
                print("  Turno 2: (libre)")
            else:
                print("  Turno 2:", martes2)
            if martes3 == "":
                print("  Turno 3: (libre)")
            else:
                print("  Turno 3:", martes3)
    elif opcion == 4:
        turnos_ocupados_lunes = 0
        if lunes1 != "":
            turnos_ocupados_lunes = turnos_ocupados_lunes + 1
        if lunes2 != "":
            turnos_ocupados_lunes = turnos_ocupados_lunes + 1
        if lunes3 != "":
            turnos_ocupados_lunes = turnos_ocupados_lunes + 1
        if lunes4 != "":
            turnos_ocupados_lunes = turnos_ocupados_lunes + 1
        turnos_ocupados_martes = 0
        if martes1 != "":
            turnos_ocupados_martes = turnos_ocupados_martes + 1
        if martes2 != "":
            turnos_ocupados_martes = turnos_ocupados_martes + 1
        if martes3 != "":
            turnos_ocupados_martes = turnos_ocupados_martes + 1
        
        turnos_libres_lunes = 4 - turnos_ocupados_lunes
        turnos_libres_martes = 3 - turnos_ocupados_martes
        print(f"Turnos ocupados lunes : {turnos_ocupados_lunes}, turnos disponibles lunes: {turnos_libres_lunes}")
        print(f"Turnos ocupados martes : {turnos_ocupados_martes}, turnos disponibles martes: {turnos_libres_martes}")
        
        if turnos_ocupados_lunes > turnos_ocupados_martes:
            print("Día con más turnos: Lunes")
        elif turnos_ocupados_martes > turnos_ocupados_lunes:
            print("Día con más turnos: Martes")
        else:
            print("Empate entre Lunes y Martes")

    
    elif opcion == 5:
        print(f"Hasta luego,", {operador})
        break

#Ejercicio 4
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_seguidas = 0


nombre = input("Ingrese su nombre de agente: ")
while not nombre.isalpha():
    print("Ingrese letras")
    nombre = input("Ingrese su nombre de agente: ")

print("Bienvenido, agente", nombre)
print("Tu misión: abrir las 3 cerraduras de la bóveda.")


while cerraduras_abiertas < 3 and energia > 0 and tiempo > 0:

    if alarma and tiempo <= 3:
        print("SISTEMA BLOQUEADO: la alarma está activa. El tiempo es crítico.")
        print("Boveda sellada permanentemente. Misión fallida.")
        break

    print("\n─────────────────────────────────")
    print("Estado del agente", nombre)
    print("  Energía:            ", energia)
    print("  Tiempo restante:    ", tiempo)
    print("  Cerraduras abiertas:", cerraduras_abiertas, "/ 3")
    print("  Código parcial:     ", codigo_parcial, "(" + str(len(codigo_parcial)) + " caracteres)")
    if alarma:
        print("ALARMA ACTIVADA")
    print("─────────────────────────────────")
    print("1) Forzar cerradura  (-20 energía, -2 tiempo)")
    print("2) Hackear panel     (-10 energía, -3 tiempo)")
    print("3) Descansar         (+15 energía, -1 tiempo)")

    opcion = input("Elegí una acción: ")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        print("Opción inválida. Ingresá 1, 2 o 3.")
        opcion = input("Elegí una acción: ")
    opcion = int(opcion)

    if opcion == 1:
        energia = energia - 20
        tiempo = tiempo - 2
        forzar_seguidas = forzar_seguidas + 1

        # Regla anti-spam
        if forzar_seguidas >= 3:
            print("Forzaste demasiadas veces seguidas. ¡La cerradura se trabó!")
            alarma = True
            print("Alarma activada automáticamente.")

        else:
            # Riesgo de alarma si energía baja
            if energia < 40:
                print("\nEnergía baja. Riesgo de alarma al forzar.")
                numero = input("Ingresá un número del 1 al 3: ")
                while not numero.isdigit() or int(numero) < 1 or int(numero) > 3:
                    print("Número inválido.")
                    numero = input("Ingresá un número del 1 al 3: ")
                numero = int(numero)
                if numero == 3:
                    alarma = True
                    print("Alarma activada.")
                else:
                    cerraduras_abiertas = cerraduras_abiertas + 1
                    print("Cerradura abierta! Total:", cerraduras_abiertas, "/ 3")
            else:
                cerraduras_abiertas = cerraduras_abiertas + 1
                print("Cerradura forzada y abierta! Total:", cerraduras_abiertas, "/ 3")

    elif opcion == 2:
        forzar_seguidas = 0
        energia = energia - 10
        tiempo = tiempo - 3

        print("\nHackeando panel...")
        for paso in range(1, 5):
            codigo_parcial = codigo_parcial + "A"
            print("  Paso", paso, "de 4 — Código parcial:", codigo_parcial)

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas = cerraduras_abiertas + 1
            print("Código completo. ¡Cerradura abierta! Total:", cerraduras_abiertas, "/ 3")

    elif opcion == 3:
        forzar_seguidas = 0
        tiempo = tiempo - 1

        if alarma:
            energia = energia - 10
            print("\n Descansás, pero la alarma te drena energía. -10 energía extra.")
        else:
            energia = energia + 15
            if energia > 100:
                energia = 100
            print("\nDescansaste. Energía recuperada.")

    # Chequeo de energía mínima
    if energia <= 0:
        energia = 0


print("\n═════════════════════════════════")
if cerraduras_abiertas == 3:
    print("¡VICTORIA! Abriste la bóveda, agente", nombre + "!")
elif alarma and tiempo <= 3:
    print("DERROTA por bloqueo de alarma.")
elif energia <= 0:
    print("DERROTA: te quedaste sin energía.")
elif tiempo <= 0:
    print("DERROTA: se acabó el tiempo.")
print("  Cerraduras abiertas:", cerraduras_abiertas, "/ 3")
print("  Energía final:      ", energia)
print("  Tiempo final:       ", tiempo)

#Ejercicio 5 

print("BIENVENIDO/a A LA ARENA")


nombre = input("Nombre del/de la Gladiador/a: ")
while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del/ de la Gladiador/a: ")


vida_jugador = 100
vida_enemigo = 100
pociones = 3
danio_pesado = 15
danio_enemigo = 12
turno_gladiador = True

print("\n=== INICIO DEL COMBATE ===")

while vida_jugador > 0 and vida_enemigo > 0:

    
    print("\n" + nombre, "(HP:", str(vida_jugador) + ")", "vs Enemigo (HP:", str(vida_enemigo) + ") | Pociones:", pociones)
    print("Elige acción:")
    print("  1. Ataque Pesado")
    print("  2. Ráfaga Veloz")
    print("  3. Curar")

    opcion = input("Opción: ")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        print("Error: Ingrese un número válido.")
        opcion = input("Opción: ")
    opcion = int(opcion)

    
    if opcion == 1:
        if vida_enemigo < 20:
            danio_final = danio_pesado * 1.5
            print("¡GOLPE CRÍTICO! Atacaste al enemigo por", danio_final, "puntos de daño!")
        else:
            danio_final = danio_pesado
            print("¡Atacaste al enemigo por", danio_final, "puntos de daño!")
        vida_enemigo = vida_enemigo - int(danio_final)

    
    elif opcion == 2:
        print(">> ¡Inicias una ráfaga de golpes!")
        for golpe in range(3):
            vida_enemigo = vida_enemigo - 5
            print("  > Golpe conectado por 5 de daño")

    # Curar
    elif opcion == 3:
        if pociones > 0:
            vida_jugador = vida_jugador + 30
            if vida_jugador > 100:
                vida_jugador = 100
            pociones = pociones - 1
            print("¡Te curaste! +30 HP. Pociones restantes:", pociones)
        else:
            print("¡No quedan pociones!")

    # Turno del enemigo (si sigue vivo)
    if vida_enemigo > 0:
        vida_jugador = vida_jugador - danio_enemigo
        print(">> ¡El enemigo contraataca por", danio_enemigo, "puntos!")

    # Chequeo para no mostrar "nuevo turno" si el juego terminó
    if vida_jugador > 0 and vida_enemigo > 0:
        print("\n=== NUEVO TURNO ===")

#Fin del juego
print("\n══════════════════════════════")
if vida_jugador > 0:
    print("¡VICTORIA!", nombre, "ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")
print("  HP final:", nombre + ":", vida_jugador, "| Enemigo:", vida_enemigo)
print("══════════════════════════════")