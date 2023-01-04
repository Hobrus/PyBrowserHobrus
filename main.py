import sys

from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QTextEdit,
    QVBoxLayout,
    QWidget,
    QLineEdit,
    QPushButton,
    QHBoxLayout,
)
from PyQt5.QtWebEngineWidgets import QWebEngineView


class Browser(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create the QWebEngineView
        self.view = QWebEngineView(self)
        self.view.load(QUrl("https://www.google.com"))

        # Create the address bar
        self.address_bar = QLineEdit(self)
        self.address_bar.returnPressed.connect(self.load_url)

        # Create the back and forward buttons
        self.back_button = QPushButton("<", self)
        self.back_button.clicked.connect(self.view.back)
        self.forward_button = QPushButton(">", self)
        self.forward_button.clicked.connect(self.view.forward)

        # Create the refresh button
        self.refresh_button = QPushButton("R", self)
        self.refresh_button.clicked.connect(self.view.reload)

        # Create the layout
        layout = QVBoxLayout(self)
        nav_bar = QHBoxLayout(self)
        nav_bar.addWidget(self.back_button)
        nav_bar.addWidget(self.forward_button)
        nav_bar.addWidget(self.refresh_button)
        nav_bar.addWidget(self.address_bar)
        layout.addLayout(nav_bar)
        layout.addWidget(self.view)

        # Set the layout as the central widget
        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def load_url(self):
        url = QUrl(self.address_bar.text())
        self.view.load(url)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = Browser()
    browser.show()
    sys.exit(app.exec_())
