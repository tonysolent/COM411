import csv

records = []
headings = []

def load_data(file_path):
    print("Loading data...")
    b = 0
    with open(file_path) as my_file:
        read = csv.reader(my_file)
        headings = next(read)
        for info in read:
            records.append(info)

    print("done!")

def display_menu():
    print("Please select one of the following options:")
    print("[1] Display the names of all passengers\n[2] Display the number of passengers that survived\n[3] Display the number of passengers per gender\n[4] Display the number of passengers per age group\n[5] Display the number of survivors per age group\n")
    a = int(input())
    return(a)
def display_passenger_names():
    print("The names of the passengers are...")
    for a in records:
        print(f"{a[3]}")
def display_passengers_per_age_group():
    children = adults = elderly = 0
    for a in records:
        if (a[5] != ""):
            if(a[5] < '18'):
                children += 1
            elif(a[5] < '65'):
                adults += 1
            else:
                elderly =+ 1
    print(f"children: {children}, adults: {adults}, elderly: {elderly}")
    return(children,adults,elderly)

def display_passengers_per_gender():
    males = females = 0
    for a in records:
        if(a[4] != ""):
            if(a[4] == "male"):
                males += 1
            else:
                females += 1

    print(f"females: {females}, males: {males}")

def display_num_survivors():
    num_survived = 0
    for a in records:
        if (a[1] == '1'):
            num_survived += 1
    print(f"{num_survived} passengers survived")

def display_survivors_per_age_group():
    c_srv = a_srv = old_srv = 0
    type = display_passengers_per_age_group()
    for a in records:
        if(a[5] != ""):
            if(a[1] ==  '1' and a[5] < '18'):
                c_srv += 1git pu
            elif (a[1] == '1' and a[5] < '65'):
                a_srv += 1
            elif(a[1] == 1):
                old_srv += 1
    print(f"children: {c_srv}/{type[0]}, adults: {a_srv}/{type[1]}, elderly: {old_srv}/{type[2]}")


def run():
   load_data("titanic.csv")
   len_info = len(records)
   print(f"Successfully loaded {len_info} records.")
   selected_option = display_menu()
   print(f"You have selection option: {selected_option}")
   if(selected_option == 1):
       display_passenger_names()
   elif (selected_option == 2):
        display_num_survivors()
   elif (selected_option == 3):
        display_passengers_per_gender()
   elif (selected_option == 4):
       display_passengers_per_age_group()
   elif (selected_option == 5):
       display_survivors_per_age_group()
