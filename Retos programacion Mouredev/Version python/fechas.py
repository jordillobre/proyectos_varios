# EJERCICIO:
# Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
# · Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
# · Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).

# Calcula cuántos años han transcurrido entre ambas fechas.

# DIFICULTAD EXTRA (opcional):
# Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de 10 maneras diferentes. Por ejemplo:
# · Día, mes y año.
# · Hora, minuto y segundo.
# · Día de año.
# · Día de la semana.
# · Nombre del mes.
#  (lo que se te ocurra...)

# https://github.com/mouredev/roadmap-retos-programacion/blob/main/Roadmap/14%20-%20FECHAS/ejercicio.

# ayuda con datetime: https://docs.python.org/es/3/library/datetime.html#

from datetime import datetime

def fechas():
    nacimiento = datetime(1993, 4, 6, 2, 15, 0)
    hoy = datetime.now()

    print (hoy)

    print (nacimiento)

    transcurrido = hoy - nacimiento

    print(f"Actualmente tengo {transcurrido.days // 365} años")

    print (nacimiento.strftime("%c"))
    # %c Representación apropiada de fecha y hora de la configuración regional

    print (nacimiento.strftime("%x"))
    # %x Representación de fecha apropiada de la configuración regional.

    print (nacimiento.strftime("%X"))
    # %X Representación de la hora apropiada de la configuración regional.

    print (nacimiento.strftime("%d %B %y"))
    # %d Día del mes como un número decimal rellenado con ceros
    # %B Mes como nombre completo según la configuración regional.
    # %yAño sin siglo como un número decimal rellenado con ceros.

    print (nacimiento.strftime("%A %d %B %Y"))
    # %A Día de la semana como nombre completo de la localidad.
    # %Y Año con siglo como número decimal.

    print (nacimiento.strftime("%a %d %b %Y"))
    # %a Día de la semana como nombre abreviado según la configuración regional
    # %b Mes como nombre abreviado según la configuración regional.
    
    print (nacimiento.strftime("Naci el dia %j del año"))
    # %j Día del año como un número decimal rellenado con ceros.

    print (nacimiento.strftime("Naci dentro de la %W semana del año"))
    # %W Número de semana del año (lunes como primer día de la semana) como un número decimal con ceros. Todos los días de un nuevo año que preceden al primer lunes se consideran en la semana 0.

    print (nacimiento.strftime("%I:%M:%S"))
    # %I Hora (reloj de 12 horas) como un número decimal rellenado con ceros
    # %M Minuto como un número decimal rellenado con ceros.
    # %S Segundo como un número decimal rellenado con ceros.

    print (nacimiento.strftime("%H %p : %M : %S"))
    # %H Hora (reloj de 24 horas) como un número decimal rellenado con ceros.
    # %p El equivalente de la configuración regional de AM o PM.

fechas()