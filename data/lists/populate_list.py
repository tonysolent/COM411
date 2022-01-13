def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left" , "Turn Right"]
    return (directions)
def menu():
    tr = directions()
    b = 0
    print("Please select a direction:")
    while (b <= 3):
        print(f"{b}: {tr[b]}")
        b = b + 1
    c = int(input("insert a number: "))
    return (tr[(c - 1)])
def run():
    print("Working out escape route...")
    a = 0
    route = []
    while (a <= 3):
        route.append(menu())
        a = a + 1
    print(f"{route}")

run ()