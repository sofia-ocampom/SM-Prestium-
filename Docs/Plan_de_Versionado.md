# Plan de versionado
 ## Dia 1: V0.1.0
Iniciamos el proyecto, elegimos el nombre, creamos el archivo funciones.py y programamos cómo guardar usuarios y artículos en los diccionarios del programa y escribimos las reglas de validación básicas como la parte de que el código revise carácter por carácter para el precio. Todavia no está hecho el menú y todo se probó ejecutando funciones directo en spyder.
 ## Dia 2: V0.2.0
Nos pusimos a trabajar en el manejo del tiempo. Logramos que la computadora sepa qué día es hoy y calcule exactamente qué día se le vence el plazo al cliente ya sea en 5, 10, 15 o 30 días.
Además, dejamos listo algo muy importante dentro de la función de ventas que es que si el sistema detecta que a alguien se le venció el tiempo y no ha devuelto el artículo, el programa escribe automáticamente un archivo que sería la factura que da el artículo por "vendido" y le cobra a la persona el precio del producto más un 23% extra como penalización por no haberlo traído a tiempo. 
## Dia 3: V0.5.0
Este dia organizamos la biblioteca en dos partes, una que es oculta que es en donde se guardan los registros y se hacen las cuentas, y otra que es el menú principal que dice el nombre de la empresa y tira un menú donde están las 8 opciones que se pueden elegir según lo que la persona quiera hacer y ahora “main.py” llama a “funciones.py”.
## Dia 4: V0.8.0
Acá organizamos la parte del administrador, creamos el acceso con la contraseña y el usuario, y programamos las funciones matemáticas para que estas calculen quién ha pedido mas cosas y quién menos, el promedio de días que duran los prestamos y cuanto dinero en total se ha ganado gracias a las multas que se cobran.
## Dia 5: V0.9.0
Este dia nos pusimos a mirar que posibles errores podían ocurrir como con los correos vimos que no habíamos puesto que se tenía que poner el “.com” al final del correo sino que solo habíamos puesto el “@” como obligatorio para dejar registrar correctamente y también eliminamos el menú principal que lo teníamos en dos archivos repetidos y lo eliminamos de “funciones.py” .
## Dia 6: V1.0.0
Este dia hicimos principalmente pruebas del código, registramos diferentes usuarios, hicimos simulaciones de devoluciones y nos aseguramos de que las facturas se imprimieran correctamente, también vimos que la parte del administrador funcionara bien con la clave que era y nos aseguramos que cuando le diéramos “salir” se saliera del todo del código y se despidiera correctamente.
