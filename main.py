import keyboard
import time
from datetime import datetime
try:
    print("Comenzando grabación de teclas, presiona 'esc' para terminar")
    keyboard.start_recording()
    while True:
        if keyboard.is_pressed('esc'):
            break
        time.sleep(0.1)
    events = keyboard.stop_recording()
    print("Grabación finalizada!")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"teclas_grabadas_{timestamp}.txt"
    

    with open(filename, "w", encoding="utf-8") as f:
        for event in events:
            if event.event_type == "down":
                if event.name == "space":
                    f.write(" ")
                elif event.name == "enter":
                    f.write("\n")
                elif len(event.name) == 1: 
                    f.write(event.name)
    
    print(f"Teclas guardadas en el archivo: {filename}")
except Exception as e:
    print(f"Ocurrió un error: {e}")