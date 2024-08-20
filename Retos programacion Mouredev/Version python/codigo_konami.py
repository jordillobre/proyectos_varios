# Crea un programa que detecte cuando el famoso "Código Konami" se ha introducido correctamente desde el teclado. Si sucede esto, debe notificarse mostrando un mensaje en la terminal.

# https://github.com/mouredev/retos-programacion-2023/blob/main/Retos/Reto%20%2325%20-%20EL%20C%C3%93DIGO%20KONAMI%20%5BMedia%5D/ejercicio.md

import keyboard as kb
import time

konami =    ["flecha arriba", "flecha arriba",
            "flecha abajo", "flecha abajo",
            "flecha izquierda", "flecha derecha", 
            "flecha izquierda", "flecha derecha", 
            "b", "a"]

position = 0

def cod_konami():
    global position, konami

    while True:
        event = kb.read_event()
        
        if event.event_type == kb.KEY_UP:
            key_name = event.name
            
            if key_name == konami[position]:
                print("Has introducido el valor correcto, continúa")
                position += 1
                
                if position == len(konami):
                    print("Has introducido el código Konami correctamente")
                    time.sleep(2)
                    break
            else:
                print(f"Has fallado, tenias que haber introducido la tecla: '{konami[position]}'")
                time.sleep(2)
                break

cod_konami()