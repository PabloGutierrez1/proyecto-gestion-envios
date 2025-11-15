#Pablo Gutierrez: 21550852-8 
codigo_envio = 1
envios = []
repartidores = []

def calc_cost(peso):
    base = 1800
    adicional = 1000
    descuento = 0.05
    peso = float(peso)

    if peso <= 1:
        return base
    else:
        costo = base + adicional * (peso - 1)
        descuento_total = min(int(peso / 10) * descuento, 1)
        costo *= (1 - descuento_total)
        return costo

def ingresar_repartidor():
    repartidor = {
        "nombre_completo": input("Ingrese el nombre completo del repartidor: "),
        "rut": input("Ingrese el rut del repartidor: "),
        "fecha_nacimiento": input("Ingrese la fecha de nacimiento del repartidor: "),
        "direccion": input("Ingrese la dirección del repartidor: "),
        "correo_electronico": input("Ingrese el correo electrónico del repartidor: "),
        "telefono": input("Ingrese el numero telefónico del repartidor: "),
        "estado_civil": input("Ingrese el estado civil del repartidor: "),
        "comuna": input("Ingrese la comuna del repartidor: "),
        "region": input("Ingrese la region de residencia del repartidor: ")
    }
    repartidores.append(repartidor)
    print("El repartidor fue ingresado correctamente.")

def mod_envio():
    codigo = int(input("Ingrese el código del envio que quiere modificar el estado: "))
    for envio in envios:
        if envio['codigo'] == codigo:
            while True:
                print("Cargando...\n"
                    f"Envió encontrado: {envio}\n"
                    "Seleccione el nuevo estado del envio:\n"
                    "1. En transito\n"
                    "2. Entregado\n"
                    "3. No entregado\n"
                    "4. Sin registro")
                opcion_estado = int(input("Ingrese el numero del nuevo estado del envio: "))
                
                if opcion_estado == 1:
                    nuevo_estado = "En transito"
                    break
                elif opcion_estado == 2:
                    nuevo_estado = "Entregado"
                    break
                elif opcion_estado == 3:
                    nuevo_estado = "No entregado"
                    break
                elif opcion_estado == 4:
                    nuevo_estado = "Sin registro"
                    break
                else:
                    print("Opción invalida. Inténtelo nuevamente")

            envio['estado'] = nuevo_estado
            if nuevo_estado == "Entregado":
                envio['fecha_entrega'] = input("Ingresar la fecha de la entrega: ")
            print("Envió modificado correctamente.")
            return
    print("Código de envio no encontrado.")

def listar_envios():
    for envio in envios:
        print("****************************************************************\n"
            f"Codigo: {envio['codigo']}\n"
            f"Remitente: {envio['remitente']}\n"
            f"Receptor: {envio['receptor']}\n"
            f"Fecha de envio: {envio['fecha_envio']}\n"
            f"Fecha de entrega: {envio['fecha_entrega']}\n"
            f"Peso del paquete: {envio['peso']}\n"
            f"Costo del envio: {envio['costo']}\n"
            f"Estado del envio: {envio['estado']}\n"
            f"Repartidor: {envio['repartidor']}\n"
            "*****************************************************************")

def ingresar_envio(codigo_envio):
    remitente = {
        "rut": input("Ingrese el rut del remitente: "),
        "nombre_completo": input("Ingrese el nombre completo del remitente: "),
        "direccion": input("Ingrese la dirección del remitente: "),
        "pais": input("Ingrese el país del remitente: "),
        "comuna": input("Ingrese la comuna del remitente: ")
    }
    
    receptor = {
        "rut": input("Ingrese el rut del receptor: "),
        "nombre_completo": input("Ingrese el nombre completo del receptor: "),
        "direccion": input("Ingrese la dirección del receptor: "),
        "pais": input("Ingrese el país del receptor: "),
        "comuna": input("Ingrese la comuna del receptor: ")
    }
    
    fecha_envio = input("Ingrese la fecha de envío: ")
    peso = float(input("Ingrese el peso del paquete en kilogramos: "))
    
    print("Repartidores disponibles:")
    for i, repartidor in enumerate(repartidores):
        print(f"{i + 1}. {repartidor['nombre_completo']}")
    
    repartidor_idx = int(input("Seleccione un repartidor por su número: ")) - 1
    repartidor = repartidores[repartidor_idx]['nombre_completo']
    
    costo = calc_cost(peso)
    envio = {
        "codigo": codigo_envio,
        "remitente": remitente,
        "receptor": receptor,
        "fecha_envio": fecha_envio,
        "fecha_entrega": None,
        "peso": peso,
        "costo": costo,
        "estado": "en tránsito",
        "repartidor": repartidor,
        "encargado_despacho": None
    }
    envios.append(envio)
    print("El envío fue ingresado correctamente.")
    return codigo_envio + 1


while True:
    print("******¡Bienvenido a la aplicación de Envíos Instantáneos!******\n"
        "1.- Ingrese un repartidor\n"
        "2.- Ingrese un envió\n"
        "3.- Modifique un envió\n"
        "4.- Listar todos los envíos\n"
        "5.- Salir\n"
        "****************************************************************")
    opcion = input("Selecciones una opcion de las mencionadas: ")
    if opcion == "1":
        ingresar_repartidor()
    elif opcion == "2":
        codigo_envio = ingresar_envio(codigo_envio)
    elif opcion == "3":
        mod_envio()
    elif opcion == "4":
        listar_envios()
    elif opcion == "5":
        break
    else:
        print("Opción invalida. Inténtelo nuevamente.")
