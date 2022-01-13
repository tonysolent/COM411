def box(str, counter2):
    counter = len(str)
    while (counter2 <  counter + 2):
        print("-", end ="")
        counter2= counter2 + 1
    print("\n|", end =""),
    print(f"{str}", end =""),
    print("|")
    counter2 = 0
    while (counter2 < counter + 2):
        print("-", end="")
        counter2 = counter2 + 1
def lowercase(str):
    print(str.lower())


def upercase(str):
    print(str.upper())


def mirrored(str, counter):
    print(str[::-1])
    # mid = (len(str)/2)
    # size = len (str)
    # while counter != mid :
    # str[counter] = str[(size - 1) - counter]
    # counter = counter + 1
    # return(str1)


def repeat(number, counter, str):
    while (counter < number):
        counter = counter + 1
        upercase(str)
        if (counter < number):
            lowercase(str)
            counter = counter + 1


def main():
    counter = 0
    str = input("please enter a word")
    n = int(input("plese enter a number betwen 1-5: \n"))
    if n == 1:
        box(str, counter)
    if n == 2:
        lowercase(str)
    if n == 3:
        upercase(str)
    if n == 4:
        mirrored(str, counter)
    if n == 5:
        my_number = int(input("how many times to display the word ?"))
        repeat(my_number, counter, str)


main()