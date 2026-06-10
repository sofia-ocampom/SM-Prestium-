import funciones as f
 
LOGO = r"""
  / ____|                               | | (_)                 
 | (___  _ __ ___    _ __  _ __ ___  ___| |_ _ _   _ _ __ ___  
  \___ \| '_ ` _ \  | '_ \| '__/ _ \/ __| __| | | | | '_ ` _ \ 
  ____) | | | | | | | |_) | | |  __/\__ \ |_| | |_| | | | | | |
 |_____/|_| |_| |_| | .__/|_|  \___||___/\__|_|\__,_|_| |_| |_|
                     | |                                        
                     |_|                                        
"""
 
while True:
        f.limpiar()
        print(LOGO)
        f.separador("SM PRESTIUM")
        print("  1. Registrar usuario")
        print("  2. Registrar item")
        print("  3. Registrar prestamo")
        print("  4. Registrar devolucion")
        print("  5. Consultar items vencidos")
        print("  6. Consultar articulos prestados")
        print("  7. Administrador")
        print("  8. Salir")
        f.separador()
 
        op = input("Seleccione opcion: ").strip()
        if op == "1":
            f.registrar_usuario()
        elif op == "2":
            f.registrar_item()
        elif op == "3":
            f.registrar_prestamo()
        elif op == "4":
            f.registrar_devolucion()
        elif op == "5":
            f.consultar_items_vencidos()
        elif op == "6":
            f.consultar_articulos_prestados()
        elif op == "7":
            f.administrador()
        elif op == "8":
            print("Hasta luego.")
            break
        else:
            print("Opcion invalida.")
            f.pausa()