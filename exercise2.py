def teilbar(x, y):
    if y == 0:
        print("Es ist nicht möglich durch 0 zu teilen!")
    else:
        if y == x:
            print("x und y sind gleich")
        elif x%y == 0:
            print("x ist durch y teilbar")
        else:
            print("x ist nicht durch y teilbar")
            
teilbar(x = 4, y = 4)
            
