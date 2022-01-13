def  observed():
    a = 0
    my_list = []
    while (a < 5):
        b = input("Please enter an observation:")
        my_list.append(b)
        a += 1
    return(my_list)
def remove_observations(my_list):
    decision = "yes"
    while(decision != "no"):
        decision = input("Do you wish to remove an observation (yes/no)?")
        if (decision == "yes"):
            remove = input("What observation do you wish to remove?")
            my_list.remove(remove)

def run():
    my_list = observed()
    remove_observations(my_list)
    my_set = set()
    for a in my_list:
        data = (a,my_list.count(a))
        my_set.add(data)
    for data in my_set:
        print(f"{data[0]} observed {data[1]} times.")

run()