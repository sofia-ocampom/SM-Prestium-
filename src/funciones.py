from datetime import datetime, timedelta
from pathlib import Path
usuarios = {}
inventario = {}
CATEGORIAS = {
    "1": ("VD", "Videojuegos"),
    "2": ("LB", "Libros"),
    "3": ("EL", "Electronica"),
    "4": ("HD", "Hogar"),
    "5": ("OT", "Otros"),
}

ADMIN_USUARIO   = "admin"
ADMIN_CONTRASENA = "prestium2026"

def limpiar():
    """
    Hace: imprime saltos de linea para simular limpieza de pantalla.
    Recibe: nada.
    Retorna: nada.
    """
    print("\n" * 3)

def pausa():
    """
    Hace: detiene la ejecucion hasta que el usuario presione ENTER.
    Recibe: nada.
    Retorna: nada.
    """
    input("\nPresione ENTER para continuar...")

def separador(titulo=""):
    """
    Hace: imprime una linea decorativa de separacion, con titulo opcional.
    Recibe: titulo (str) -- texto a mostrar en el separador, por defecto vacio.
    Retorna: nada.
    """
    linea = "=" * 50                                     
    if titulo:
        print("\n" + linea)
        print("  " + titulo)
        print(linea)
    else:
        print(linea)

def validar_nombre(texto):
    """
    Hace: verifica que el nombre tenga al menos 3 caracteres y no contenga digitos.
    Recibe: texto (str) -- nombre a validar.
    Retorna: True si el nombre es valido, False si no lo es.
    """
    if len(texto) < 3:
        return False
    for c in texto:
        if c.isdigit():
            return False
    return True

def validar_documento(doc):
    """
    Hace: verifica que el documento contenga solo digitos y tenga entre 3 y 15 caracteres.
    Recibe: doc (str) -- numero de documento a validar.
    Retorna: True si el documento es valido, False si no lo es.
    """
    if not doc.isdigit():
        return False
    if len(doc) < 3 or len(doc) > 15:
        return False
    return True

def validar_correo(correo):
    """
    Hace: verifica que el correo contenga '@' y termine en '.com'.
    Recibe: correo (str) -- direccion de correo a validar.
    Retorna: True si el correo es valido, False si no lo es.
    """
    if "@" not in correo:
        return False
    return True

def validar_precio(precio):
    """
    Hace: verifica caracter por caracter que el precio sea un numero decimal
          positivo valido, sin usar try/except.
    Recibe: precio (str) -- valor de precio a validar.
    Retorna: True si el precio es valido, False si no lo es.
    """
    es_valido = True
    tiene_punto = False

    if not precio:
        es_valido = False

    i = 0
    while i < len(precio) and es_valido:
        caracter = precio[i]
        if caracter == ".":
            if tiene_punto:
                es_valido = False
            else:
                tiene_punto = True
        elif not caracter.isdigit():
            es_valido = False
        i += 1

    if es_valido:
        if float(precio) < 0:
            es_valido = False

    return es_valido

def registrar_usuario():
    """
    Hace: solicita los datos de un nuevo usuario, los valida y los guarda en el
          diccionario global 'usuarios'.
    Recibe: nada (lee entradas del usuario por consola).
    Retorna: nada.
    """
    limpiar()
    separador("REGISTRAR USUARIO")

    nombre = input("Nombre: ").strip()
    if not validar_nombre(nombre):
        print("Nombre invalido (minimo 3 letras, sin numeros).")
        pausa()
        return
    if nombre in usuarios:
        print("El usuario ya existe.")
        pausa()
        return

    apellido  = input("Apellido: ").strip()
    documento = input("Documento: ").strip()
    if not validar_documento(documento):
        print("Documento invalido (solo digitos, 3-15 caracteres).")
        pausa()
        return

    correo = input("Correo: ").strip()
    if not validar_correo(correo):
        print("Correo invalido (debe contener @ y terminar en .com).")
        pausa()
        return

    print("Dias de prestamo permitidos: 5 | 10 | 15 | 30")
    dias_str = input("Dias prestamo: ").strip()
    if dias_str not in ("5", "10", "15", "30"):
        print("Opcion de dias invalida.")
        pausa()
        return
    dias = int(dias_str)

    usuarios[nombre] = [[apellido, documento, correo, dias]]
    print("\nUsuario '" + nombre + "' registrado correctamente.")
    pausa()

def generar_id(prefijo):
    """
    Hace: cuenta cuantos items del inventario comienzan con el prefijo dado
          y genera un ID unico incrementando ese conteo.
    Recibe: prefijo (str) -- codigo de categoria (ej: 'VD', 'LB').
    Retorna: id_item (str) -- nuevo ID unico con el prefijo y numero de 3 digitos.
    """
    contador = 0
    for item in inventario:
        if item.startswith(prefijo):
            contador += 1
    return prefijo + str(contador + 1).zfill(3)

def registrar_item():
    """
    Hace: solicita los datos de un nuevo item, lo valida y lo guarda en el
          diccionario global 'inventario' con un ID generado automaticamente.
    Recibe: nada (lee entradas del usuario por consola).
    Retorna: nada.
    """
    limpiar()
    separador("REGISTRAR ITEM")

    print("Categorias disponibles:")
    for clave in CATEGORIAS:
        nombre_cat = CATEGORIAS[clave][1]
        print("  " + clave + ". " + nombre_cat)

    opc = input("Seleccione categoria: ").strip()
    if opc not in CATEGORIAS:
        print("Categoria invalida.")
        pausa()
        return
    prefijo    = CATEGORIAS[opc][0]
    nombre_cat = CATEGORIAS[opc][1]

    nombre_item = input("Nombre del item: ").strip()
    if not nombre_item:
        print("El nombre no puede estar vacio.")
        pausa()
        return

    precio_str = input("Precio: ").strip()
    if not validar_precio(precio_str):
        print("Precio invalido.")
        pausa()
        return
    precio = float(precio_str)

    try:
        estado = int(input("Estado (1-10): ").strip())
        if not (1 <= estado <= 10):
            raise ValueError
    except ValueError:
        print("Estado invalido (debe ser un entero entre 1 y 10).")
        pausa()
        return

    if estado <= 3:
        calidad = "Malo"
    elif estado == 4:
        calidad = "Regular"
    elif estado <= 7:
        calidad = "Bueno"
    else:
        calidad = "Excelente"

    id_item = generar_id(prefijo)
    inventario[id_item] = [nombre_item, precio, calidad, "disponible", nombre_cat]

    print("\nItem registrado correctamente en '" + nombre_cat + "'.")
    print("  ID      : " + id_item)
    print("  Calidad : " + calidad)
    pausa()

def registrar_prestamo():
    """
    Hace: registra un prestamo activo vinculando un usuario con un item disponible,
          calcula la fecha limite segun el plan del usuario y actualiza el estado
          del item a 'prestado'.
    Recibe: nada (lee entradas del usuario por consola).
    Retorna: nada.
    """
    limpiar()
    separador("REGISTRAR PRESTAMO")

    nombre = input("Nombre usuario: ").strip()
    if nombre not in usuarios:
        print("Usuario no existe.")
        pausa()
        return

    id_item = input("ID del item: ").upper().strip()
    if id_item not in inventario:
        print("Item no encontrado.")
        pausa()
        return
    if inventario[id_item][3] != "disponible":
        print("El item '" + id_item + "' no esta disponible (estado actual: " + inventario[id_item][3] + ").")
        pausa()
        return

    hoy          = datetime.now()
    fecha_inicio = hoy.strftime("%Y-%m-%d")
    dias         = usuarios[nombre][0][3]
    fecha_limite = (hoy + timedelta(days=dias)).strftime("%Y-%m-%d")

    usuarios[nombre].append([id_item, inventario[id_item][0], "activo", fecha_inicio, fecha_limite])
    inventario[id_item][3] = "prestado"

    print("\nPrestamo registrado correctamente.")
    print("  Item        : " + inventario[id_item][0] + "  (ID: " + id_item + ")")
    print("  Inicio      : " + fecha_inicio)
    print("  Fecha limite: " + fecha_limite + "  (" + str(dias) + " dias)")
    pausa()

def registrar_devolucion():
    """
    Hace: registra la devolucion de un item prestado, actualiza su estado a
          'disponible' y genera un certificado de devolucion en archivo de texto.
    Recibe: nada (lee entradas del usuario por consola).
    Retorna: nada.
    """
    limpiar()
    separador("REGISTRAR DEVOLUCION")

    nombre = input("Nombre usuario: ").strip()
    if nombre not in usuarios:
        print("Usuario no existe.")
        pausa()
        return

    hay_activo = False
    for p in usuarios[nombre][1:]:
        if p[2] == "activo":
            hay_activo = True
            break

    if not hay_activo:
        print("No se puede registrar la devolucion: '" + nombre + "' no tiene prestamos activos.")
        pausa()
        return

    id_item = input("ID del item a devolver: ").upper().strip()

    for prestamo in usuarios[nombre][1:]:
        if prestamo[0] == id_item and prestamo[2] == "activo":
            prestamo[2]            = "devuelto"
            inventario[id_item][3] = "disponible"
            hoy                    = datetime.now()
            fecha_dev              = hoy.strftime("%Y-%m-%d")
            fecha_inicio           = prestamo[3]
            fecha_limite           = prestamo[4]
            dias_usados = (hoy - datetime.strptime(fecha_inicio, "%Y-%m-%d")).days
            info        = usuarios[nombre][0]

            contenido = (
                "CERTIFICADO DE DEVOLUCION\n"
                "==================================================\n"
                "Prestador        : " + nombre + " " + info[0] + "\n"
                "Documento        : " + info[1] + "\n"
                "Correo           : " + info[2] + "\n"
                "--------------------------------------------------\n"
                "Item             : " + prestamo[1] + "\n"
                "ID item          : " + id_item + "\n"
                "Categoria        : " + inventario[id_item][4] + "\n"
                "Calidad          : " + inventario[id_item][2] + "\n"
                "--------------------------------------------------\n"
                "Fecha de prestamo: " + fecha_inicio + "\n"
                "Fecha limite     : " + fecha_limite + "\n"
                "Fecha devolucion : " + fecha_dev + "\n"
                "Dias utilizados  : " + str(dias_usados) + "\n"
                "==================================================\n"
                "Devolucion realizada antes del vencimiento.\n"
                "Gracias por usar SM Prestium.\n"
            )

            ruta = Path(nombre + "_" + fecha_dev + "_" + id_item + "_certificado.txt")
            ruta.write_text(contenido, encoding="utf-8")

            print("\nDevolucion registrada correctamente.")
            print("  Certificado generado: " + str(ruta))
            pausa()
            return

    print("No se encontro un prestamo activo con el ID '" + id_item + "' para '" + nombre + "'.")
    pausa()

def procesar_ventas():
    """
    Hace: recorre todos los prestamos activos, detecta los vencidos, los marca
          como 'vendido', actualiza el inventario y genera una factura en archivo
          de texto con impuesto del 23%.
    Recibe: nada.
    Retorna: generadas (int) -- cantidad de ventas procesadas en la ejecucion.
    """
    hoy       = datetime.now()
    generadas = 0

    for nombre in usuarios:
        for prestamo in usuarios[nombre][1:]:
            if prestamo[2] != "activo":
                continue
            fecha_limite = datetime.strptime(prestamo[4], "%Y-%m-%d")
            if hoy <= fecha_limite:
                continue

            prestamo[2]            = "vendido"
            id_item                = prestamo[0]
            inventario[id_item][3] = "vendido"

            precio    = inventario[id_item][1]
            impuesto  = precio * 0.23
            total     = precio + impuesto
            fecha_str = hoy.strftime("%Y-%m-%d")
            info      = usuarios[nombre][0]

            dias_excedidos = (hoy - fecha_limite).days

            contenido = (
                "FACTURA DE VENTA\n"
                "==================================================\n"
                "Comprador        : " + nombre + " " + info[0] + "\n"
                "Documento        : " + info[1] + "\n"
                "Correo           : " + info[2] + "\n"
                "--------------------------------------------------\n"
                "Item             : " + inventario[id_item][0] + "\n"
                "ID item          : " + id_item + "\n"
                "Categoria        : " + inventario[id_item][4] + "\n"
                "--------------------------------------------------\n"
                "MOTIVO DE VENTA:\n"
                "  El item supero el tiempo maximo de prestamo\n"
                "  (" + str(dias_excedidos) + " dia(s) de exceso). Segun politica\n"
                "  de SM Prestium, el item pasa a ser vendido\n"
                "  al prestador con impuesto por conchudez del 23%.\n"
                "--------------------------------------------------\n"
                "Fecha prestamo   : " + prestamo[3] + "\n"
                "Fecha limite     : " + prestamo[4] + "\n"
                "Fecha de venta   : " + fecha_str + "\n"
                "Dias excedidos   : " + str(dias_excedidos) + "\n"
                "--------------------------------------------------\n"
                "Subtotal         : $" + str(round(precio, 2)) + "\n"
                "Impuesto (23%)   : $" + str(round(impuesto, 2)) + "\n"
                "TOTAL A PAGAR    : $" + str(round(total, 2)) + "\n"
                "==================================================\n"
            )

            ruta = Path(nombre + "_" + id_item + "_factura.txt")
            ruta.write_text(contenido, encoding="utf-8")
            print("  Venta procesada -> " + str(ruta))
            generadas += 1

    return generadas

def consultar_items_vencidos():
    """
    Hace: muestra por consola todos los prestamos activos cuya fecha limite
          ya fue superada, indicando cuantos dias llevan vencidos.
    Recibe: nada.
    Retorna: nada.
    """
    limpiar()
    separador("ITEMS VENCIDOS (MAS DE 30 DIAS)")

    hoy         = datetime.now()
    encontrados = 0

    for nombre in usuarios:
        for prestamo in usuarios[nombre][1:]:
            if prestamo[2] != "activo":
                continue
            fecha_limite = datetime.strptime(prestamo[4], "%Y-%m-%d")
            if hoy > fecha_limite:
                encontrados += 1
                dias_exc = (hoy - fecha_limite).days
                print("  " + nombre.ljust(15) + " | " + prestamo[1].ljust(20) +
                      " | ID: " + prestamo[0] + " | Vencido hace " + str(dias_exc) + " dia(s)")

    if encontrados == 0:
        print("  No hay items vencidos actualmente.")
    pausa()

def consultar_articulos_prestados():
    """
    Hace: muestra por consola todos los items que se encuentran actualmente
          en estado de prestamo activo, con su usuario y fecha limite.
    Recibe: nada.
    Retorna: nada.
    """
    limpiar()
    separador("ARTICULOS PRESTADOS ACTUALMENTE")

    encontrados = 0
    for nombre in usuarios:
        for prestamo in usuarios[nombre][1:]:
            if prestamo[2] == "activo":
                encontrados += 1
                print("  " + nombre.ljust(15) + " | " + prestamo[1].ljust(20) +
                      " | ID: " + prestamo[0] + " | Limite: " + prestamo[4])

    if encontrados == 0:
        print("  No hay articulos prestados actualmente.")
    pausa()

def estado_general_prestamos():
    """
    Hace: recopila todos los prestamos del sistema, los ordena por dias
          transcurridos de mayor a menor, calcula estadisticas generales
          y guarda un reporte en archivo de texto plano.
    Recibe: nada.
    Retorna: nada.
    """
    limpiar()
    separador("ESTADO GENERAL DE PRESTAMOS")

    hoy = datetime.now()

    registros = []
    for nombre in usuarios:
        for prestamo in usuarios[nombre][1:]:
            fecha_inicio       = datetime.strptime(prestamo[3], "%Y-%m-%d")
            fecha_limite       = datetime.strptime(prestamo[4], "%Y-%m-%d")
            dias_transcurridos = (hoy - fecha_inicio).days
            dias_restantes     = (fecha_limite - hoy).days
            estado_prestamo    = prestamo[2]

            if estado_prestamo == "activo":
                if hoy > fecha_limite:
                    estado_display = "VENCIDO (+" + str(abs(dias_restantes)) + " dias)"
                else:
                    estado_display = "Activo (" + str(dias_restantes) + " dia(s) restante(s))"
            elif estado_prestamo == "devuelto":
                estado_display = "Devuelto"
            else:
                estado_display = "Vendido"

            registros.append({
                "usuario"       : nombre,
                "item"          : prestamo[1],
                "id_item"       : prestamo[0],
                "estado"        : estado_prestamo,
                "estado_display": estado_display,
                "inicio"        : prestamo[3],
                "limite"        : prestamo[4],
                "dias_trans"    : dias_transcurridos,
            })

    if not registros:
        print("  No hay prestamos registrados en el sistema.")
        pausa()
        return

    n = len(registros)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if registros[j]["dias_trans"] < registros[j + 1]["dias_trans"]:
                registros[j], registros[j + 1] = registros[j + 1], registros[j]

    total     = len(registros)
    activos   = 0
    devueltos = 0
    vendidos  = 0
    suma_dias = 0

    for r in registros:
        suma_dias += r["dias_trans"]
        if r["estado"] == "activo":
            activos += 1
        elif r["estado"] == "devuelto":
            devueltos += 1
        elif r["estado"] == "vendido":
            vendidos += 1

    promedio_dias = suma_dias / total

    max_rec = registros[0]
    min_rec = registros[0]
    for r in registros:
        if r["dias_trans"] > max_rec["dias_trans"]:
            max_rec = r
        if r["dias_trans"] < min_rec["dias_trans"]:
            min_rec = r

    print("\n  " + "USUARIO".ljust(15) + " " + "ITEM".ljust(20) + " " +
          "ID".ljust(8) + " " + "INICIO".ljust(12) + " " + "LIMITE".ljust(12) +
          " " + "DIAS".rjust(5) + "  ESTADO")
    print("  " + "-" * 15 + " " + "-" * 20 + " " + "-" * 8 + " " +
          "-" * 12 + " " + "-" * 12 + " " + "-" * 5 + "  " + "-" * 30)

    for r in registros:
        print("  " + r["usuario"].ljust(15) + " " + r["item"].ljust(20) + " " +
              r["id_item"].ljust(8) + " " + r["inicio"].ljust(12) + " " +
              r["limite"].ljust(12) + " " + str(r["dias_trans"]).rjust(5) +
              "  " + r["estado_display"])

    print("\n  -- Estadisticas ------------------------------------------")
    print("  Total prestamos   : " + str(total))
    print("  Activos           : " + str(activos))
    print("  Devueltos         : " + str(devueltos))
    print("  Vendidos          : " + str(vendidos))
    print("  Promedio de dias  : " + str(round(promedio_dias, 1)))
    print("  Mayor duracion    : " + max_rec["item"] + " (" + str(max_rec["dias_trans"]) + " dias) -- " + max_rec["usuario"])
    print("  Menor duracion    : " + min_rec["item"] + " (" + str(min_rec["dias_trans"]) + " dias) -- " + min_rec["usuario"])

    fecha_reporte = hoy.strftime("%Y-%m-%d_%H-%M")
    ruta = Path("estado_prestamos_" + fecha_reporte + ".txt")

    lineas = []
    lineas.append("REPORTE DE ESTADO GENERAL DE PRESTAMOS\n")
    lineas.append("==================================================\n")
    lineas.append("Generado: " + hoy.strftime("%Y-%m-%d %H:%M") + "\n")
    lineas.append("--------------------------------------------------\n")
    lineas.append("USUARIO".ljust(15) + " " + "ITEM".ljust(20) + " " +
                  "ID".ljust(8) + " " + "INICIO".ljust(12) + " " +
                  "LIMITE".ljust(12) + " " + "DIAS".rjust(5) + "  ESTADO\n")
    lineas.append("-" * 15 + " " + "-" * 20 + " " + "-" * 8 + " " +
                  "-" * 12 + " " + "-" * 12 + " " + "-" * 5 + "  " + "-" * 30 + "\n")

    for r in registros:
        lineas.append(r["usuario"].ljust(15) + " " + r["item"].ljust(20) + " " +
                      r["id_item"].ljust(8) + " " + r["inicio"].ljust(12) + " " +
                      r["limite"].ljust(12) + " " + str(r["dias_trans"]).rjust(5) +
                      "  " + r["estado_display"] + "\n")

    lineas.append("--------------------------------------------------\n")
    lineas.append("Total prestamos   : " + str(total) + "\n")
    lineas.append("Activos           : " + str(activos) + "\n")
    lineas.append("Devueltos         : " + str(devueltos) + "\n")
    lineas.append("Vendidos          : " + str(vendidos) + "\n")
    lineas.append("Promedio de dias  : " + str(round(promedio_dias, 1)) + "\n")
    lineas.append("Mayor duracion    : " + max_rec["item"] + " (" + str(max_rec["dias_trans"]) + " dias) -- " + max_rec["usuario"] + "\n")
    lineas.append("Menor duracion    : " + min_rec["item"] + " (" + str(min_rec["dias_trans"]) + " dias) -- " + min_rec["usuario"] + "\n")
    lineas.append("==================================================\n")

    ruta.write_text("".join(lineas), encoding="utf-8")
    print("\n  Reporte guardado en: " + str(ruta))
    pausa()

def _admin_estadisticas():
    """
    Hace: procesa ventas pendientes, luego muestra el conteo total de prestamos,
          devoluciones, ventas y el monto total cobrado con impuesto.
    Recibe: nada.
    Retorna: nada.
    """
    limpiar()
    separador("ESTADISTICAS GENERALES")

    generadas = procesar_ventas()
    if generadas:
        print("  (Se procesaron " + str(generadas) + " venta(s) pendiente(s).)\n")

    total_prestamos = 0
    total_devueltos = 0
    total_ventas    = 0
    total_pago      = 0.0

    for n in usuarios:
        for p in usuarios[n][1:]:
            total_prestamos += 1
            if p[2] == "devuelto":
                total_devueltos += 1
            if p[2] == "vendido":
                total_ventas += 1
                total_pago   += inventario[p[0]][1] * 1.23

    print("  Total prestamos registrados : " + str(total_prestamos))
    print("  Total items devueltos       : " + str(total_devueltos))
    print("  Total ventas realizadas     : " + str(total_ventas))
    print("  Total pago realizado        : $" + str(round(total_pago, 2)))
    pausa()

def _admin_lista_usuarios():
    """
    Hace: muestra por consola la informacion completa de todos los usuarios
          registrados junto con su cantidad de prestamos.
    Recibe: nada.
    Retorna: nada.
    """
    limpiar()
    separador("LISTA DE USUARIOS")

    if not usuarios:
        print("  No hay usuarios registrados.")
        pausa()
        return

    for nombre in usuarios:
        info       = usuarios[nombre][0]
        nprestamos = len(usuarios[nombre]) - 1
        print("  " + nombre + " " + info[0] + " | Doc: " + info[1] +
              " | Correo: " + info[2] + " | Dias plan: " + str(info[3]) +
              " | Prestamos: " + str(nprestamos))
    pausa()

def _admin_mayor_menor_prestamos():
    """
    Hace: recorre todos los usuarios y determina cual tiene la mayor y menor
          cantidad de prestamos registrados.
    Recibe: nada.
    Retorna: nada.
    """
    limpiar()
    separador("USUARIO CON MAYOR Y MENOR PRESTAMOS")

    if not usuarios:
        print("  No hay usuarios registrados.")
        pausa()
        return

    primer_nombre = None
    for n in usuarios:
        primer_nombre = n
        break

    maximo     = primer_nombre
    minimo     = primer_nombre
    max_conteo = len(usuarios[primer_nombre]) - 1
    min_conteo = len(usuarios[primer_nombre]) - 1

    for n in usuarios:
        conteo = len(usuarios[n]) - 1
        if conteo > max_conteo:
            max_conteo = conteo
            maximo     = n
        if conteo < min_conteo:
            min_conteo = conteo
            minimo     = n

    print("  Mayor cantidad : " + maximo + " (" + str(max_conteo) + " prestamo(s))")
    print("  Menor cantidad : " + minimo + " (" + str(min_conteo) + " prestamo(s))")
    pausa()

def administrador():
    """
    Hace: solicita credenciales de administrador y, si son correctas, muestra
          el panel de administracion con opciones de estadisticas y reportes.
    Recibe: nada (lee entradas del usuario por consola).
    Retorna: nada.
    """
    limpiar()
    separador("ACCESO ADMINISTRADOR")

    usuario = input("Usuario: ").strip()
    clave   = input("Contrasena: ").strip()
    if usuario != ADMIN_USUARIO or clave != ADMIN_CONTRASENA:
        print("Acceso denegado.")
        pausa()
        return

    while True:
        limpiar()
        separador("PANEL DE ADMINISTRACION")
        print("  1. Estadisticas generales")
        print("  2. Lista de usuarios")
        print("  3. Usuario con mayor y menor prestamos")
        print("  4. Estado general de prestamos (reporte)")
        print("  5. Volver al menu principal")
        separador()

        op = input("Seleccione opcion: ").strip()
        if op == "1":
            _admin_estadisticas()
        elif op == "2":
            _admin_lista_usuarios()
        elif op == "3":
            _admin_mayor_menor_prestamos()
        elif op == "4":
            estado_general_prestamos()
        elif op == "5":
            break
        else:
            print("Opcion invalida.")
            pausa()

def menu_principal():
    """
    Hace: muestra el menu principal en bucle y redirige al usuario a cada
          funcionalidad del sistema segun la opcion seleccionada.
    Recibe: nada.
    Retorna: nada.
    """
    while True:
        limpiar()
        separador("SM PRESTIUM")
        print("  1. Registrar usuario")
        print("  2. Registrar item")
        print("  3. Registrar prestamo")
        print("  4. Registrar devolucion")
        print("  5. Consultar items vencidos")
        print("  6. Consultar articulos prestados")
        print("  7. Administrador")
        print("  8. Salir")
        separador()

        op = input("Seleccione opcion: ").strip()
        if op == "1":
            registrar_usuario()
        elif op == "2":
            registrar_item()
        elif op == "3":
            registrar_prestamo()
        elif op == "4":
            registrar_devolucion()
        elif op == "5":
            consultar_items_vencidos()
        elif op == "6":
            consultar_articulos_prestados()
        elif op == "7":
            administrador()
        elif op == "8":
            print("Hasta luego.")
            break
        else:
            print("Opcion invalida.")
            pausa()