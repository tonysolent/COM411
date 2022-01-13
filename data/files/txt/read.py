import os
def display_chars(path,n):
    file = open(path)
    data = file.read(n)
    file.close()
    print(f"{data}")

def display_line(path):
    with open(path) as file:
        line = file.readline().strip()
    file.close()
    print(f"{line}")
def display_text(path):
    with open(path) as file:
        data = file.read()
    file.close()
    print(f"{data}")
def run():
    display_chars("library.txt", 5)
    display_line("library.txt")
    display_text("library.txt")

if __name__ == "__main__":
    run()