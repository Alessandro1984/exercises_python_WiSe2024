def vokon_zählen(x):
    vokale = "aeiou"
    x_lower = x.lower()
    
    b = [i for i in x_lower if i.isalpha()]
    v = [i for i in b if i in vokale]
    
    print(f"Es gibt {len(v)} Vokale und {len(b)-len(v)} Konsonanten.")

vokon_zählen("HallO,&%/ BerliN!!")