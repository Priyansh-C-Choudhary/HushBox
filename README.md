# HushBox

## Overview
**HushBox** is a user-friendly tool designed to secure your personal folders with password protection. It provides a sleek GUI for locking/unlocking folders and integrates seamlessly with the Windows context menu, offering quick and efficient access. Built with PyQt5, HushBox ensures your private data stays private using secure password hashing.

## Features
- 🔒 **Lock Folders**: Restrict access to selected folders with a password.
- 🔓 **Unlock Folders**: Restore access to locked folders with the correct password.
- 🛡️ **Password Protection**: Uses SHA-256 hashing for secure password storage.
- 🎨 **User-Friendly GUI**: Built with PyQt5, featuring password visibility toggle and feedback messages.
- 📂 **Context Menu Integration**: Adds "Lock Folder" and "Unlock Folder" options to the Windows Explorer context menu.
- 🚀 **Standalone Executable**: Generate a `.exe` file with PyInstaller for standalone use.

## How It Works

1. **Folder Protection**:
   - **Lock a folder**: Deny access using Windows' `icacls` command and store a hashed password.
   - **Unlock a folder**: Verify the password and restore access permissions.

2. **Context Menu Integration**:
   - Adds "Lock Folder" and "Unlock Folder" options to the Windows Explorer context menu.
   - Directly apply security actions to selected folders.

## Getting Started

### Prerequisites
- Python 3.x
- PyQt5: Install using the following command:
  ```bash
  pip install PyQt5
  ```
### Installation and Setup
   1. **Install Required Python Packages**
   Run the following command to install all required dependencies:

```bash
pip install -r requirements.txt
```
   2. **Generate the Executable**
To create a standalone executable, run:

```bash
pyinstaller --onefile --noconsole folder_protection.py
```
3. Add Context Menu Options
Run the RegistryScript.py to add "Lock Folder" and "Unlock Folder" options to the Windows context menu:

```bash
python RegistryScript.py
```
## Usage
### Using the GUI
1. Run the executable or script:
```bash
python folder_protection.py
```
OR
```bash
dist/folder_protection.exe
```
2. Enter the folder path and choose to lock or unlock it.
3. Provide a password to secure or unlock the folder.
### Using the Context Menu
1. Right-click on any folder in Windows Explorer.
2. Select "Lock Folder" or "Unlock Folder" from the menu.
3. Follow the prompts to lock/unlock the folder.

## Registry Script

RegistryScript.py manages the context menu entries for Windows Explorer.

Add or remove "Lock Folder" and "Unlock Folder" options as needed.

## File Structure

The project structure is as follows:

```
HushBox/
├── folder_protection.py    # Main folder locking/unlocking application
├── RegistryScript.py       # Script to manage Windows registry entries
├── icons/
│   ├── lock.ico            # Icon for "Lock Folder"
│   ├── unlock.ico          # Icon for "Unlock Folder"
├── info.txt                # PyInstaller and registry setup instructions
```
## Contributing
Feel free to fork the repository and submit pull requests for improvements or bug fixes. Contributions are always welcome!


## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Author
Priyansh C. Choudhary

## Acknowledgments
Built with ❤️ to keep your private folders safe!
