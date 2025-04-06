with open("file.txt" , "r") as file:
    data = file.read()


with open("file2.txt", "w") as file:
    file.write("Hello, I am file2 a simple modified version of file.")



def read_file_safely():
    filename = input("📂 Enter the name of the file to read: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    
    except FileNotFoundError:
        print("❌ Error: File not found. Please make sure the filename is correct.")
    
    except PermissionError:
        print("❌ Error: You don't have permission to read this file.")
    
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

read_file_safely()
