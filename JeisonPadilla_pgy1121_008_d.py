
import funciones as fn




print("""MENÚ
1. Comprar entradas
2. Mostrar ubicaciones disponibles
3. Ver listado de asistentes
4. Mostrar ganancias totales
5. Salir""")

opcion = fn.validar_opcion()

if opcion == 1:
   entradas = fn.validar_entradas()
   if entradas >=1 and entradas <= 3:
       fn.mostrar_asientos()
       fn.validar_fila()
       fn.validar_columna()
       fn.validar_rut()
       fn.validar_nombre()
       print("Compra realizada con éxito!")
elif opcion == 2:
    fn.asientos_disponibles()
elif opcion == 3:
    fn.mostrar_lista()
elif opcion == 4:
    fn.ganancias_totales()
else:
    fn.mensaje_Salida()
