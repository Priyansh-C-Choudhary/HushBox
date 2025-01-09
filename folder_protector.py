import os
import sys
import hashlib
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QLabel,
    QLineEdit,
    QMessageBox,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QFrame,
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class FolderProtector(QMainWindow):
    def __init__(self, folder_path=None, mode="lock"):
        super().__init__()
        self.folder_path = folder_path
        self.mode = mode
        self.setWindowTitle("Folder Protector")
        self.setGeometry(300, 200, 400, 300)
        self.setStyleSheet(self.load_styles())
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.setSpacing(20)

        # Title
        self.title_label = QLabel("\ud83d\udd12 Lock Folder" if self.mode == "lock" else "\ud83d\udd13 Unlock Folder")
        self.title_label.setFont(QFont("Arial", 18, QFont.Bold))
        self.title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.title_label)

        # Password and Action Buttons
        password_layout = QHBoxLayout()
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setFixedHeight(40)
        password_layout.addWidget(self.password_input)

        self.show_password_button = QPushButton("\ud83d\udc41")
        self.show_password_button.setFixedSize(40, 40)
        self.show_password_button.setCheckable(True)
        self.show_password_button.clicked.connect(self.toggle_password_visibility)
        password_layout.addWidget(self.show_password_button)

        layout.addLayout(password_layout)

        self.action_button = QPushButton("\ud83d\udd12 Lock Folder" if self.mode == "lock" else "\ud83d\udd13 Unlock Folder")
        self.action_button.setFixedHeight(40)
        self.action_button.clicked.connect(self.lock_folder if self.mode == "lock" else self.unlock_folder)
        layout.addWidget(self.action_button)

        # Set main container
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


    def toggle_password_visibility(self):
        if self.show_password_button.isChecked():
            self.password_input.setEchoMode(QLineEdit.Normal)
            self.show_password_button.setText("\ud83d\ude48")  # Change icon/text for "hide password"
        else:
            self.password_input.setEchoMode(QLineEdit.Password)
            self.show_password_button.setText("\ud83d\udc41")  # Change icon/text for "show password"

    def lock_folder(self):
        password = self.password_input.text().strip()
        if not password:
            self.show_message("Error", "Password cannot be empty.")
            return

        lock_file = os.path.join(self.folder_path, ".lock")
        password_hash = hashlib.sha256(password.encode()).hexdigest()

        # Save the password hash
        with open(lock_file, "w") as f:
            f.write(password_hash)

        # Restrict folder access
        os.system(f'icacls "{self.folder_path}" /deny Everyone:F')
        self.show_message("Success", f"The folder '{self.folder_path}' has been locked.")

    def unlock_folder(self):
        password = self.password_input.text().strip()
        if not password:
            self.show_message("Error", "Password cannot be empty.")
            return

        lock_file = os.path.join(self.folder_path, ".lock")
        if not os.path.exists(lock_file):
            self.show_message("Error", "This folder is not locked.")
            return

        with open(lock_file, "r") as f:
            stored_hash = f.read().strip()

        entered_hash = hashlib.sha256(password.encode()).hexdigest()
        if stored_hash != entered_hash:
            self.show_message("Error", "Incorrect password.")
            return

        # Restore folder access
        os.system(f'icacls "{self.folder_path}" /grant Everyone:F')
        os.remove(lock_file)
        self.show_message("Success", f"The folder '{self.folder_path}' has been unlocked.")

    def show_message(self, title, message):
        msg = QMessageBox(self)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.exec_()

    def load_styles(self):
        return """
            QMainWindow {
                background-color: #1c1c1c;  /* Dark background */
                color: #ffffff;  /* Text color */
            }
            QLabel {
                color: #e0e0e0;  /* Slightly lighter text */
            }
            QPushButton {
                background-color: #333333;  /* Button background */
                color: #ffffff;  /* Button text */
                border: 1px solid #555555;
                border-radius: 10px;
                padding: 10px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #444444;  /* Hover effect */
            }
            QLineEdit {
                background-color: #2e2e2e;  /* Input background */
                color: #ffffff;
                border: 1px solid #555555;
                border-radius: 10px;
                padding: 10px;
            }
            QFrame {
                background-color: #252525;
                border: 1px solid #555555;
                border-radius: 10px;
            }
        """

# Run the application
if __name__ == "__main__":
    folder_to_process = None
    mode = "lock"

    # Parse command-line arguments
    if len(sys.argv) > 1:
        mode = sys.argv[1]  # "lock" or "unlock"
        if len(sys.argv) > 2:
            folder_to_process = sys.argv[2]

    app = QApplication([])
    window = FolderProtector(folder_path=folder_to_process, mode=mode)
    window.show()
    app.exec_()
