import csv

def read(file):
    with open(file) as my_file:
        csv_read = csv.reader(my_file)
        headings = next(csv_read)
        print(f"the heding is:\n{headings}\n")
        print("values:")
        for a in csv_read:
            print(a)

def main():
    read("bots.csv")

main()