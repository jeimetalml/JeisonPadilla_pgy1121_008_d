import numpy
lista_rut = []
lista_nombres = []
lista_platinum = []
lista_gold = []
lista_silver = []
lista_fila = []
lista_columna = []
cantidad_platinum = 0
cantidad_gold = 0
cantidad_silver = 0
valor_platinum = 120000
valor_gold = 80000
valor_silver = 50000
total_platinum = cantidad_platinum * valor_platinum
total_gold = cantidad_gold * valor_gold
total_silver = cantidad_silver * valor_silver
total_cantidades = cantidad_platinum + cantidad_gold + cantidad_silver
total = total_platinum + total_gold + total_silver

asientos_evento = numpy.zeros((10,10), int)



def validar_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opción:"))
            if opcion in (1,2,3,4,5):
                return opcion
            else:
                print("ERROR! La opcion debe ser entre 1 y 5!")
        except:
            print("ERROR! Debes ingresar un número entero!")


def validar_nombre():
    while True:
        nombre = input("Ingrese su nombre:")
        if len(nombre) >= 3 and nombre not in lista_nombres:
            return nombre
        else:
            print("ERROR! Intentalo de nuevo!")


def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese su rut:"))
            if rut >=1000000 and rut <= 90000000:
                return rut
            elif rut in lista_rut:
                print("El rut ya tiene una entrada asociada!")
            else:
                print("ERROR! Opción incorrecta!")
        except:
            print("ERROR! Debes ingresar números enteros!")


def validar_entradas():
    while True:
        try:
            entradas = int(input("¿Cuántas entradas desea comprar?"))
            if entradas in (1,2,3):
                return entradas
            else:
                print("ERROR! La cantidad de entradas debe ser entre 1 y 3!")
        except:
            print("ERROR! Debes escribir un número entero!")


def mostrar_asientos():
    for x in range(1):
        for y in range(1):
            print(asientos_evento, end=" ")
            print()


def validar_fila():
    while True:
        try:
            fila = int(input("Seleccione una fila:"))
            if fila in(1,2,3,4,5,6,7,8,9,10):
                return fila
            elif fila in lista_fila:
                print("NO ESTÁ DISPONIBLE!")
            elif fila in(1,2):
                cantidad_platinum = cantidad_platinum + 1
            elif fila in(3,4,5):
                cantidad_gold = cantidad_gold + 1
            elif fila in(6,7,8,9,10):
                cantidad_silver = cantidad_silver + 1
            else:
                print("ERROR! Opcion incorrecta!")
        except:
            print("ERROR! Debes escribir un número entero:")


def validar_columna():
    while True:
        try:
            columna = int(input("Seleccione una columna:"))
            if columna in(1,2,3,4,5,6,7,8,9,10):
                return columna
            elif columna in lista_columna:
                print("NO ESTÁ DISPONIBLE!")
            else:
                print("ERROR! Opcion incorrecta!")
        except:
            print("ERROR! Debes escribir un número entero:")


def asientos_disponibles():
    for x in range(1):
        for y in range(1):
            print(asientos_evento, end=" ")
            print()


def mostrar_lista():
    print(lista_rut.append, lista_nombres.append)


def ganancias_totales():
    print("TOTAL GANANCIAS:")
    print("-------TIPO ENTRADA-------------CANTIDAD----------TOTAL")
    print("PLATINUM $",valor_platinum,"-----------",cantidad_platinum,"--------","$",total_platinum)
    print("GOLD $",valor_gold,"------------",cantidad_gold,"--------","$",total_gold)
    print("SILVER $",valor_silver,"------------",cantidad_silver,"--------","$",total_silver)
    print()
    print("TOTAL------------------------", total_cantidades, "---------------","$",total)


def mensaje_Salida():
    print("Muchas gracias, vuelva pronto!")
    print("Jeison Padilla Suarez")
    print("11/07/2023")