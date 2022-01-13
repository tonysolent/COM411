def observed():
    a = 0
    my_list = []
    while(a < 7):
        numb = input("Please enter an observation:")
        my_list.append(numb)
        a += 1
    return(my_list)

def run():
    print("Counting observations...")
    my_data = observed()
    print(my_data)
    my_set = set()
    for a in my_data:
        data = (a, my_data.count(a))
        my_set.add(data)
    for data in my_set:
        print(f"{data[0]} observed {data[1]} times.")
run()