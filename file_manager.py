#lets create a simple file manager 

import os  #working with os
import shutil

def list_items():
    items = os.listdir()
    if not items:
        print("No files or folders found.")
    else:
        for item in items:
            print(item)

def create():
    choice = input("Type 'file' to create a file or 'folder' to create a folder: ")
    try: 
        if choice.lower() == "file":
            name = input("Enter the file name (e.g., notes.txt): ")
            with open(name, "w") as f:
                pass  
            print(f"File '{name}' created successfully.")
        elif choice.lower() == "folder":
            name = input("Enter the folder name: ")
            os.mkdir(name)
            print(f"Folder '{name}' created successfully.")
        else: 
            print("Invalid input")
    except FileNotFoundError:
        print("Some error has occured.")


def delete():
    choice = input("Do you want to delete a 'file' or 'folder'? ").lower()
    try:
        if choice == "file":
            name = input("Enter the name of the file you want to delete: ")
            if os.path.isfile(name):
                os.remove(name)
                print(f"File '{name}' deleted successfully.")
            else:
                print("File does not exist.")
        elif choice == "folder":
            name = input("Enter the name of the folder you want to delete: ")
            if os.path.isdir(name):
                # This only deletes empty folders
                try:
                    os.rmdir(name)
                    print(f"Folder '{name}' deleted successfully.")
                except OSError:
                    confirm = input("Folder is not empty. Delete all contents? (yes/no): ").lower()
                    if confirm == "yes":
                        shutil.rmtree(name)
                        print(f"Folder '{name}' and all its contents deleted.")
                    else:
                        print("Delete cancelled.")
            else:
                print("Folder does not exist.")
        else:
            print("Invalid input.")
    except Exception as e:
        print(f"Error: {e}")

def rename():
    choice = input("Do you want to rename a 'file' or a 'folder'? ")
    old_name = input("Enter the current name: ")
    new_name = input("Enter the new name: ")
    try:
        
        if choice in ['file', 'folder']:
            if not os.path.exists(old_name):
                print(f"{choice.capitalize()} '{old_name}' does not exist.")
            elif os.path.exists(new_name):
                print(f"A file/folder with the name '{new_name}' already exists.")
            else:
                os.rename(old_name, new_name)
                print(f"{choice.capitalize()} renamed successfully from '{old_name}' to '{new_name}'.")
        else:
            print("Invalid input.")
    except Exception as e:
        print(f"Error: {e}")

    
def main():
    print('''Welcome to File Manager Tool

    [1] List files/folders
    [2] Create file/folder
    [3] Delete file/folder
    [4] Rename file/folder
    [5] Exit''')


    while True:
        op = input("What do you want to do?")
        if op =="1":
            list_items()
        elif op =="2":
            create()
        elif op =="3":
            delete()
        elif op =="4":
            rename()
        elif op =="5":
            exit()
            print("Exiting Program.")
        else: 
            print("Invalid option")


if __name__ == "__main__":
    start = input("Enter 'start' to begin: ").strip().lower()
    if start == "start":
        main()
    else:
        print("Program terminated.")



    



