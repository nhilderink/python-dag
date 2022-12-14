def optellen(*args):
    som = 0
    for i in args:
        som += i
    print(som)


optellen(2, 3, 4, 5)

def rekenmachine(getal1, getal2, operatie):
    if operatie == "o":
        print(getal1 + getal2)

    if operatie == "v":
            print(getal1 * getal2)
        
    if operatie == "d":
            print(getal1 / getal2)
            
rekenmachine(1, 3, "o")
rekenmachine(1, 3, "v")
rekenmachine(1, 3, "d")