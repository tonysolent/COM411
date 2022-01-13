def sum_weights(bot1, bot2):
    return (bot1 + bot2)
def  calc_avg_weight(bot1, bot2):
    final = ((bot1 + bot2) / 2)
    return (final)
def main():
    bot1 = int(input("What is the weight of Beep?"))
    bot2 = int(input("What is the weight of Bop?"))
    calc = str(input("What would you like to calculate (sum or average)?"))
    if calc == "sum":
        sum_weights(bot1, bot2)
        print(f"The sum of Beep and Bop's weight is {sum_weights(bot1, bot2)}")

    if calc == "average":
        calc_avg_weight(bot1, bot2)
        print(f"The average of Beep and Bop's weight is {calc_avg_weight(bot1, bot2)}")
main()
