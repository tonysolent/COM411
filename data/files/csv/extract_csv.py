import csv

def extract(file):
    print("Extracting...")
    with open(file) as my_file:
        read = csv.reader(my_file)
        header = next(read)
        print("Done!")
        print("The extracted names are:")
        for names in read:
            print(names[1])
def main():
    extract("bots.csv")
if __name__ == "__main__":
    main()