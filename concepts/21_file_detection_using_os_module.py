#OS module = provides functions to interact with the operating system
# functions include os.getcwd(), os.chdir(), os.listdir(), os.mkdir(), os.rmdir(), 
# os.remove(), os.path.exists(), os.path.isfile(), os.path.isdir(), os.path.join(), etc



import os
# get current working directory
current_dir = os.getcwd()
print("Current Directory:", current_dir)

dir = "concepts"
file  = '01_variables.py'  # Correct filename

if(not os.path.exists(dir)):
    print("Concept directory does not exist.")
else:
    print("Concept directory exists.")
    if(os.path.exists(os.path.join(dir, file))):
        print(f"{os.path.join(dir, file)} Path exists in the directory.")
        if(os.path.isfile(os.path.join(dir, file))):
            print("File exists in the directory.")
        else:
            print("File does not exist in the directory.")
    else:
        print("path does not exist in the directory.")