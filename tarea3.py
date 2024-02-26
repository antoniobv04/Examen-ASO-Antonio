import os

def create_folders_and_files():
    for i in range(1, 6):
        folder_name = f"folder{i}"
        os.makedirs(folder_name, exist_ok=True)
        
        for j in range(1, 11):
            file_name = f"{folder_name}/fichero{j}.txt"
            with open(file_name, "w") as f:
                f.write("Este es el contenido del fichero 1\n")

def main():
    create_folders_and_files()
    print("Carpetas y archivos creados exitosamente.")

if __name__ == "__main__":
    main()
