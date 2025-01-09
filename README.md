# HushBox

**HushBox** is a simple and efficient tool designed to secure your personal folders with password protection. Whether you want to keep prying eyes away from your private data or simply add an extra layer of security, HushBox is here to help. It offers a sleek GUI for folder locking/unlocking and integrates seamlessly with the Windows context menu for quick access.

---

## Features

- 🔒 **Lock Folders**: Restricts access to selected folders with a password-protected mechanism.
- 🔓 **Unlock Folders**: Restores access to locked folders after verifying the correct password.
- 🛡️ **Password Protection**: Uses SHA-256 hashing to securely store passwords.
- 🎨 **User-Friendly GUI**: Built with PyQt5, featuring password visibility toggle and clear feedback messages.
- 📂 **Context Menu Integration**: Adds "Lock Folder" and "Unlock Folder" options to the Windows Explorer context menu for easy access.
- 🚀 **Standalone Executable**: Generate a `.exe` file using PyInstaller to use the tool without requiring Python.

---

## How It Works

1. **Folder Protection**:
   - **Lock a folder**: Deny access to everyone using Windows' `icacls` command and store a hashed password.
   - **Unlock a folder**: Verify the password and restore folder access permissions.

2. **Context Menu**:
   - Adds "Lock Folder" and "Unlock Folder" options to the right-click menu in Windows Explorer.
   - Directly apply security actions on selected folders.

---

## Getting Started

### Prerequisites

- Python 3.x
- PyQt5: Install using `pip install PyQt5`

---

### Installation

1. Install required Python packages:
   ```bash
   pip install -r requirements.txt
Generate the executable:

bash
Copy code
pyinstaller --onefile --noconsole folder_protection.py
Add context menu options:
Run the RegistryScript.py to add "Lock Folder" and "Unlock Folder" to the Windows context menu:

bash
Copy code
python RegistryScript.py
Usage
Using the GUI
Run the executable or script:

bash
Copy code
python folder_protection.py
OR

bash
Copy code
dist/folder_protection.exe
Enter the folder path and choose to lock or unlock it.

Provide a password to secure the folder or unlock it.

Using the Context Menu
Right-click on any folder in Windows Explorer.
Select "Lock Folder" or "Unlock Folder" from the menu.
Follow the prompts to lock/unlock the folder.
Registry Script
RegistryScript.py manages the context menu entries for Windows Explorer.

Add or remove "Lock Folder" and "Unlock Folder" options as needed.
File Structure
bash
Copy code
HushBox/
├── folder_protection.py    # Main folder locking/unlocking application
├── RegistryScript.py       # Script to manage Windows registry entries
├── icons/
│   ├── lock.ico            # Icon for "Lock Folder"
│   ├── unlock.ico          # Icon for "Unlock Folder"
├── info.txt                # PyInstaller and registry setup instructions
Contributing
Feel free to fork the repository and submit pull requests for improvements or bug fixes. Contributions are always welcome!

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Author
Priyansh C. Choudhary
Built with ❤️ to keep your private folders safe!

vbnet
Copy code

This is the polished version of your README in markdown format. You can directly save it as `README.
