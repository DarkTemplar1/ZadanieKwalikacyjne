import sys
import subprocess
import time
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl



class PESELGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Walidator PESEL")
        self.setGeometry(100, 100, 800, 600)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://127.0.0.1:8000/"))

        layout = QVBoxLayout()
        layout.addWidget(self.browser)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


def run_django():
    subprocess.Popen(["python", "manage.py", "runserver"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(2)  # Poczekaj, aż serwer się uruchomi


if __name__ == "__main__":
    run_django()

    app = QApplication(sys.argv)
    window = PESELGUI()
    window.show()
    sys.exit(app.exec())
