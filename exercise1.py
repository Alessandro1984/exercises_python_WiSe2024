def cagr_berechnung(AK, EK, t):
    AK_abs = abs(AK)
    cagr = ((EK/AK_abs)**(1/t) - 1)
    return cagr

print(cagr_berechnung(AK = 100, 
                      EK = 700, 
                      t = 30))

rendite = cagr_berechnung(AK = 100, EK = 700, t = 30)

print(120 * (1 + rendite)**30)

    
