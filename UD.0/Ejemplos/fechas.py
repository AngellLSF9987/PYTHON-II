from datetime import date, time, datetime, timedelta

"""date(año, mes, dia) : Devuelve un objeto de tipo date que representa la fecha con el año, mes y dia indicados.
time(hora, minutos, segundos, microsegundos) : Devuelve un objeto de tipo time que representa un tiempo la hora,
minutos, segundos y microsegundos indicados.
datetime(año, mes, dia, hora, minutos, segundos, microsegundos) : Devuelve un objeto de tipo datetime que representa una 
fecha y hora con el año, mes, dia, hora, minutos, segundos y microsegundos indicados"""
time(13,30,5)
print(time(13,30,5))

datetime(2024, 12, 25, 13, 30, 5)

print(datetime(2024, 12, 25, 13, 30, 5))

"""date.today() : Devuelve un objeto del tipo date la fecha del sistema en el momento en el que se ejecuta.
datetime.now(): Devuelve un objeto del tipo datetime con la fecha y la hora del sistema en el momento exacto en el que se ejecuta.
d.year : Devuelve el año de la fecha d, puede ser del tipo date o datetime.
d.month : Devuelve el mes de la fecha d, que puede ser del tipo date o datetime.
d.day : Devuelve el día de la fecha d, que puede ser del tipo date o datetime.
d.weekday() : Devuelve el día de la semana de la fecha d, que puede serpuede ser del tipo date o datetime.
t.hour : Devuelve las horas del tiempo t, que puede ser del tipo time o datetime.
t.hour : Devuelve los minutos del tiempo t, que puede ser del tipo time o datetime.
t.second : Devuelve los segundos del tiempo t, que puede ser del tipo time o datetime.
t.microsecond : Devuelve los microsegundos del tiempo t, que puede ser del tipo time o datetime."""

print(date.today())

dt = datetime.now()

print(dt.year)

print(dt.month)

print(dt.day)

print(dt.hour)

print(dt.minute)

print(dt.second)

print(dt.microsecond)

"""Conversión de fechas en cadenas con diferentes formatos
d.strftime(formato) : Devuelve la cadena que resulta de transformar la fecha d con el formato indicado en la cadena formato.
"""

d = datetime.now()
print(d.strftime('%d-%m-%Y'))

print(d.strftime('%A, %d %B, %y'))

print(d.strftime('%H:%M:%S'))

print(d.strftime('%H horas, %M minutos y %S segundos'))

"""Conversión de cadenas en fechas
 Devuelve el objeto de tipo date, time o datetime que resulta de convertir la cadena s de acuerdo al formato indicado en la cadena formato.
"""

print(datetime.strptime('15/10/2024', '%d/%m/%Y'))

print(datetime.strptime('2024-10-15 20:50:30', '%Y-%m-%d %H:%M:%S'))

"""Aritmética de fechas
Para representar el tiempo transcurrido entre dos fechas se utiliza el tipo timedelta.

timedelta(dias, segundos, microsegundos) : Devuelve un objeto del tipo timedelta que representa un intervalo de tiempo con los dias, segundos y micorsegundos indicados.
d1 - d2 : Devuelve un objeto del tipo timedelta que representa el tiempo transcurrido entre las fechas d1 y d2 del tipo datetime.
d + delta : Devuelve la fecha del tipo datetime que resulta de sumar a la fecha d el intervalo de tiempo delta, donde delta es del tipo timedelta."""

d1 = datetime(2025, 1, 1)
print(d1)
print(d1 + timedelta(31, 3600))

print(datetime.now() - d1)

"""Formatero de fechas
%Y: Año con cuatro dígitos.
%m: Mes con dos dígitos (01-12).
%d: Día del mes con dos dígitos (01-31).
%H: Hora en formato 24 horas (00-23).
%M: Minutos (00-59).
%S: Segundos (00-59).
%A: Día de la semana en formato textual (lunes, martes, etc.).
%B: Mes en formato textual (enero, febrero, etc.).

%I: Hora en formato 12 horas (01-12).
%p: AM o PM.
%j: Día del año (1-366).
%w: Día de la semana como número (0-6, donde 0 es lunes)."""

fecha_cadena = "2024-11-22"
# Se utiliza datetime.datetime.strptime para convertir la fecha en formato string en formato datetime
fecha_objeto = datetime.strptime(fecha_cadena, "%Y-%m-%d")
# Se utiliza datetime.datetime.strftime para transformar una fecha (Y-M-D) a (D-M-Y) ambas tienen formato datetime
fecha = datetime.strftime(fecha_objeto,"%d-%m-%Y")
print(fecha)

# Para convertir una fecha introducida (int) por teclado en fecha
dia_nacimiento = int(input("Ingrese el día de nacimiento: "))
mes_nacimiento = int(input("Ingrese el mes de nacimiento (1-12): "))
año_nacimiento = int(input("Ingrese el año de nacimiento: "))
# Se crea la fecha utilizando datetime.date, como es en formato ingles, primero año, mes, dia
fecha_nac = date(año_nacimiento, mes_nacimiento, dia_nacimiento) #1992-01-31
# Para transformalo a nuestro formato: datetime.datetime.strftime
fecha_nacimiento = datetime.strftime(fecha_nac,"%d/%m/%Y")
print(fecha_nacimiento)

# Para sacar la fecha del dia de hoy
hoy = date.today()
print(hoy) 
# Como el formato esta cambiado lo volvemos a formatear, si esta en formato datetime se le pueden pasar las funciones directamente
hoy_formateado = hoy.strftime("%d-%m-%Y")
print(hoy_formateado)

# Obtener la fecha y hora actual
ahora = datetime.now()
print(ahora)

# Formatear la fecha y hora
fecha_formateada_simple = ahora.strftime("%d-%m-%Y")
fecha_formateada_larga = ahora.strftime("%d-%m-%Y %H:%M:%S")

print(fecha_formateada_simple) 
print(fecha_formateada_larga) 
