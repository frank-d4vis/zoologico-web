contMasc = 0
contFem = 0
contTotal = 0
acumTotalPago = 0
nombresVisitantes = []

def salir():
    print("Gracias por visitar el zoológico. ¡Hasta pronto!")

def reportar():
    print("\n======== REPORTE GENERAL ========\n")
    print("Cantidad total de visitantes:\t\t", contTotal)
    print("Cantidad de visitantes masculinos:\t", contMasc)
    print("Cantidad de visitantes femeninos:\t", contFem)
    print("Monto total recaudado:\t\t\t", acumTotalPago)
    print("Nombres de los visitantes:")
    for nombre in nombresVisitantes:
        print("-", nombre)

def guardar_en_archivo(nombre, edad, genero, tipoEntrada, precio):
    with open("registro_zoologico.txt", "a") as archivo:
        archivo.write(f"Nombre: {nombre}, Edad: {edad}, Género: {genero}, Tipo Entrada: {tipoEntrada}, Monto: S/.{precio}\n")

def procesar():
    global contMasc, contFem, contTotal, acumTotalPago, nombresVisitantes

    nombre = input("Ingrese su nombre:\t\t")
    nombresVisitantes.append(nombre)

    while True:
        edad = int(input("Ingrese su edad:\t\t"))
        if edad <= 0:
            print("ERROR, vuelva a ingresar una edad válida")
        else:
            break
