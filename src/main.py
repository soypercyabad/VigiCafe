import pystray
import pystray._win32
from src.ui.tray import TrayApp

if __name__ == "__main__":
    app = TrayApp()
    app.run()