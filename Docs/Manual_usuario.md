# Manual de usuario
Este es el manual de usuario, diseñado para ayudarte a comprender y utilizar el programa de una forma fácil, para entenderlo de la mejor manera.
Describiremos paso a paso las acciones que podrás realizar en el programa.
## Menú principal
Al iniciar el programa aparecerá un menú como este:

![logo]Image/Inicio.png

Escribe el **número** de la opción que desees y presiona **Enter**.


---
## 1. Registrar Usuario

Esta opción guarda la información de una persona, es obligatorio registrar un usuario para poder realizar tu prestamo.

### Pasos:

1. Selecciona la opción **1** en el menú.
2. El programa pedira los siguientes datos:

| Campo | Reglas |
|-------|--------|
| **Nombre** | Mínimo 3 letras. No puede contener números. |
| **Apellido** | Mínimo 3 letras. No puede contener números. |
| **Documento** | Solo números. Entre 3 y 15 dígitos. |
| **Correo electrónico** | Debe contener `@` y terminar en `.com` |
| **Tiempo de préstamo** | Solo se permiten: `5`, `10`, `15` o `30` días |

3. Si ingresas un dato incorrecto, el programa se reiniciará y podras comenzar de nuevo.
4. Cuando todos los datos sean correctos, tu usuario quedará registrado correctamente.

### Ejemplo de ingreso correcto:

-Nombre: Laura

-Apellido: Gomez

-Documento: 1020304050

-Correo: laura@gmail.com

-Dias prestamo: 15

---

## 2. Registrar Ítem

Agrega un objeto al inventario para que pueda ser prestado.

### Pasos:

1. Selecciona la opción **2**.
2. Deberas escoger la categoria a la que pertenecera el item:
   -   Videojuegos
   -   Libros
   -   lectronica
   -   Hogar
   -   Otros

4. Ingresa los datos del ítem:

| Campo | Reglas |
|-------|--------|
| **Nombre del ítem** | No puede estar vacío. Puede contener números. |
| **Precio** | Número positivo. |
| **Estado (1-10)** | Número entero entre 1 y 10. |

4. El programa asigna automáticamente una calidad y un ID único:

| Puntaje | Calidad asignada |
|---------|-----------------|
| 1 – 3 | Malo |
| 4 | Regular |
| 5 – 7 | Bueno |
| 8 – 10 | Excelente |

### Ejemplo:

Seleccione categoria: Video Juegos 

Nombre del item: casa

Precio: 4000

Estado (1-10): 9


Si realizas todos los pasos correctamente, te aparecerá esto:

Item registrado correctamente en 'Videojuegos'.
ID      : VD001
Calidad : Excelente

---

## 3. Registrar Préstamo

Vincula un ítem disponible con un usuario registrado.

> IMPORTANTE: Tanto el usuario como el ítem deben existir previamente en el sistema.

### Pasos:

1. Selecciona la opción **3**.
2. Ingresa el **nombre del usuario**.
3. Ingresa el **ID del ítem** (ej: `VD001`).
4. El programa verifica que el ítem esté disponible y registra el préstamo con la fecha actual y la fecha límite según el plan del usuario.
   
### Ejemplo:

Nombre usuario: Sara
ID del item: VD001


- Prestamo registrado correctamente.

  Item        : casa  (ID: VD001)
  
  Inicio      : 2026-06-07
  
  Fecha limite: 2026-06-12  (5 dias)

---

## 4. Registrar Devolución

Registra que un usuario devolvió un ítem y genera un certificado.

> IMPORTANTE:  Solo se pueden registrar devoluciones de préstamos activos. Si el usuario no tiene préstamos activos, el programa lo informará.

### Pasos:

1. Selecciona la opción **4**.
2. Ingresa el **nombre del usuario**.
3. Ingresa el **ID del ítem** a devolver.
4. El programa actualiza el estado del ítem a `disponible` y genera el certificado.

### Certificado generado:

El archivo se crea automáticamente en la misma carpeta del programa con el nombre:

NombreUsuario_FechaDevolución_IDitem_certificado.txt


**Ejemplo:** `Sara_2026-06-20_VD001_certificado.txt`

El certificado contiene: nombre y documento del usuario, datos del ítem, fechas del préstamo y días utilizados.

---

## 5.  Consultar Ítems Vencidos

Muestra todos los préstamos activos cuya fecha límite ya fue superada.

### Pasos:

1. Selecciona la opción **5**.
2. El programa lista automáticamente los ítems vencidos con el número de días de exceso.

### Ejemplo de salida:

==================================================

ITEMS VENCIDOS (MAS DE 30 DIAS)

Sara            | FIFA 25              | ID: VD001 | Vencido hace 8 dia(s)

Carlos          | Taladro              | ID: HD002 | Vencido hace 3 dia(s)

> IMPORTANTE: Los ítems vencidos generarán una **factura de venta** automáticamente cuando se acceda al módulo de administrador (opción 7 → Estadísticas generales).

---

## 6. Consultar Artículos Prestados

Muestra todos los ítems que actualmente están en préstamo activo.

### Pasos:

1. Selecciona la opción **6**.
2. El programa lista usuario, nombre del ítem, ID y fecha límite de cada préstamo activo.


### Ejemplo de salida:
==================================================

ARTICULOS PRESTADOS ACTUALMENTE

Sara            | FIFA 25              | ID: VD001 | Limite: 2026-06-22

Carlos          | Don Quijote          | ID: LB001 | Limite: 2026-06-17


---

## 7. Administrador

Aqui encontraras el panel de acceso restringido con reportes y estadísticas del sistema.

### Cómo ingresar:

1. Selecciona la opción **7**.
2. Ingresa el usuario y contraseña de administrador.
3. Si las credenciales son incorrectas, el programa regresa al menú principal.

> NOTA:  Las credenciales de administrador son proporcionadas por el equipo de desarrollo.

### Submenú de administración:

==================================================


PANEL DE ADMINISTRACION

1 Estadisticas generales 

2 Listas de usuarios

3 Usuario con mayor y menor prestamos

4 Estado general de prestamos (reporte)

5 Volver al menu principal

==================================================


### Descripción de cada opción:

**1. Estadísticas generales**
Procesa automáticamente las ventas pendientes (ítems vencidos) y muestra:

| Dato | Descripción |
|------|-------------|
| Total préstamos registrados | Todos los préstamos del sistema |
| Total ítems devueltos | Préstamos con devolución registrada |
| Total ventas realizadas | Ítems que pasaron a venta por vencimiento |
| Total pago realizado | Suma total cobrada incluyendo impuesto del 23% |

Al procesar una venta, se genera automáticamente una **factura** en archivo `.txt`.

**2. Lista de usuarios**
Muestra nombre, apellido, documento, correo, plan de días y cantidad de préstamos de cada usuario registrado.

**3. Usuario con mayor y menor préstamos**
Indica qué usuario ha realizado más préstamos y cuál menos.

**4. Estado general de préstamos (reporte)**
Muestra todos los préstamos ordenados de mayor a menor días transcurridos, con estadísticas completas. Guarda el reporte en un archivo `.txt` con la fecha y hora de generación.


---

## 8. 🚪 Salir

Selecciona la opción **8** para cerrar SM Prestium.
Hasta luego.

> IMPORTANTE: Los datos se almacenan en memoria mientras el programa está abierto. Al cerrarlo, los datos no se conservan entre sesiones a menos que el programa haya generado archivos `.txt` de reportes.
