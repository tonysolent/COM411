import csv

def export(file,n):
    print("Exporting...")
    a = 1
    with open(file,"at") as my_file:
        while(a < n + 1):
            bot_id =int(input("Please enter the bot id:"))
            bot_name = input("Please enter the bot name:")
            bot_paint =input("Please enter the bot paint:")
            data = f"{bot_id},{bot_name},{bot_paint}\n"
            my_file.write(data)
            a += 1
def main():
    n = int(input(" how many bots are to be exported?"))
    export("exported_bots.csv", n)

main()