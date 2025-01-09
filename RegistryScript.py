
import os
import subprocess


def add_registry_entries(executable_path):
    lock_command = f'"{executable_path}" lock "%1"'
    unlock_command = f'"{executable_path}" unlock "%1"'

    # Add "Lock Folder" to context menu
    subprocess.run(
        [
            "REG",
            "ADD",
            r"HKCU\Software\Classes\Directory\shell\Lock Folder",
            "/v",
            "Icon",
            "/t",
            "REG_SZ",
            "/d",
            r"D:\Projects\File Locker\icons\lock.ico",  # Update with your icon path
            "/f",
        ],
        shell=True,
    )
    subprocess.run(
        [
            "REG",
            "ADD",
            r"HKCU\Software\Classes\Directory\shell\Lock Folder\command",
            "/t",
            "REG_SZ",
            "/d",
            lock_command,
            "/f",
        ],
        shell=True,
    )

    # Add "Unlock Folder" to context menu
    subprocess.run(
        [
            "REG",
            "ADD",
            r"HKCU\Software\Classes\Directory\shell\Unlock Folder",
            "/v",
            "Icon",
            "/t",
            "REG_SZ",
            "/d",
            r"D:\Projects\File Locker\icons\unlock.ico",  # Update with your icon path
            "/f",
        ],
        shell=True,
    )
    subprocess.run(
        [
            "REG",
            "ADD",
            r"HKCU\Software\Classes\Directory\shell\Unlock Folder\command",
            "/t",
            "REG_SZ",
            "/d",
            unlock_command,
            "/f",
        ],
        shell=True,
    )
    print("Registry entries added successfully.")


def remove_registry_entries():
    # Remove "Lock Folder" and "Unlock Folder" from context menu
    subprocess.run(
        [
            "REG",
            "DELETE",
            r"HKCU\Software\Classes\Directory\shell\Lock Folder",
            "/f",
        ],
        shell=True,
    )
    subprocess.run(
        [
            "REG",
            "DELETE",
            r"HKCU\Software\Classes\Directory\shell\Unlock Folder",
            "/f",
        ],
        shell=True,
    )
    print("Registry entries removed successfully.")


if __name__ == "__main__":
    print("1. Add registry entries")
    print("2. Remove registry entries")
    choice = input("Enter your choice: ")

    if choice == "1":
        executable_path = input("Enter the path to the folder_protector.exe: ").strip()
        if not os.path.exists(executable_path):
            print("Invalid path. Ensure the executable exists.")
        else:
            add_registry_entries(executable_path)
    elif choice == "2":
        remove_registry_entries()
    else:
        print("Invalid choice.")
