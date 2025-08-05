from pystray import Icon, Menu, MenuItem
from PIL import Image
import threading
from src.services.mover import MouseMover
import os

class TrayApp:
    def __init__(self):
        self.mover = MouseMover()
        self.thread = None
        self.icon = Icon("MouseAFK", title="VifCafe")
        self.icon.icon = Image.open(os.path.join("assets", 'icon.png'))
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

           
        