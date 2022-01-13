def likelihood():
    likelihood = (50, 38, 27, 99, 4)
    return (min(likelihood), max(likelihood))
def  main():
    values = likelihood()
    print(f"Minimum likelihood of falling: {values[0]}")
    print(f"Maximum likelihood of falling: {values[1]}")
main()