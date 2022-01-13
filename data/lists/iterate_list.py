def movements():
    directions = [ "Move Forward", "Move Backward", "Turn Left" ,"Turn Right"]
    return (directions)
def menu():
    str = movements()
    a = 0;
    while(a <= 3):
        print(f"{a}: {str[a]}")
        a = a + 1
    a = int(input("Please select a direction:"))
def run():
    menu()

if __name__ == "__main__":
    run()