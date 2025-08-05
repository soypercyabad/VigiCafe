import pyautogui
import time

class MouseMover:
    # Clase para mover el ratón automáticamente
    # Cada intervalo de tiempo, mueve el ratón un píxel a la derecha y luego
    def __init__(self, intervalo=30):
        self.running = False
        self.intervalo = intervalo

    # Iniciar el movimiento del ratón
    def start(self):
        self.running = True
        while self.running:
            pyautogui.moveRel(1, 0, duration=0.1)
            pyautogui.moveRel(-1, 0, duration=0.1)
            time.sleep(self.intervalo)

    # Detener el movimiento del ratón
    def stop(self):
        self.running = False