code = {1:'@', -1:'_'}

def printshape(obraz, heigth, widht):
    
    for_print = ''.join([code[a] for a in obraz])
    for i in range(heigth):
       print(for_print[i*widht: i*widht+widht])
    print('')

