from pystray import Icon, Menu, MenuItem
from PIL import Image
import threading
from src.services.mover import MouseMover
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)  

class TrayApp:
    def __init__(self):
        self.mover = MouseMover()
        self.thread = None
        self.icon = Icon("MouseAFK", title="VigiCafe")
        self.icon.icon = Image.open(resource_path("assets/icon.png"))
        self.icon.menu = Menu(
            MenuItem("Iniciar", self.start),
            MenuItem("Detener", self.stop),
            MenuItem("Salir", self.quit_app)
        )

    def start(self, icon, item):
        if not self.mover.running:
            self.thread = threading.Thread(target=self.mover.start)
            self.thread.daemon = True
            self.thread.start()

    def stop(self, icon, item):
        self.mover.stop()

    def quit_app(self, icon, item):
        self.mover.stop()
        icon.stop()

    def run(self):
        self.icon.run()
         
        