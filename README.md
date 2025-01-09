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
