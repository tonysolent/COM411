import os
def cwd():
    path = os.getcwd()
    print(f"The current working directory is {path}")
    print("The directory contains the following files:")
    for file in os.listdir(path):
        print(file)
def main():
    print("Processing...")
    cwd()
main()