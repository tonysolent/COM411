def display_ladder(steps):
    while steps > 0:
        print("| |")
        print("***")
        steps = steps - 1
    print("| |")
def create_ladder():
    st = int(input("How many steps remain?\n"))
    display_ladder(st)
create_ladder()