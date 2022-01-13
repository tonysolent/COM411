def cross_bridge(steps):
    n = 0
    while(steps > n):
        n = n + 1
        print("Crossed step.")
    if (n > 5):
        print("The bridge is collapsing!")
    else :
        print("We must keep going!")

cross_bridge(3)
cross_bridge(6)