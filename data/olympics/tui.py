def started(msg=""):
    print("-------------------------------------------------------------------------------------")
    print(f"Operation started:{msg} ...\n")
def completed():
    print("Operation completed.\n-------------------------------------------------------------------------------------")
def error(msg):
    print(f"Error! {msg}")
def menu():
    option = input(" [years]     List unique years\n[tally]      Tally up medals\n[ctally]    Tally up medals for each team\n[exit]       Exit the program")


