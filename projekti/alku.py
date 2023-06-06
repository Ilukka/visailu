
def alku():

    print ("Koneeseesi on iskenyt viheliäinen viirus ja sinun pitää vastata muutamiin tehtäviin oikein,")
    print ("niin saat koneesi taas haltuun. Väärästä vastauksesta kone laskee kymmenestä alaspäin ja räjähtää")

    lahto = input("lähdetkö ratkaisemaan mysteeriä? (k)yllä vai (e)i: ")
    if lahto == "k" or lahto == "K":
        jatko = input("Anna nimesi:")
        if jatko == jatko:
            from countdown1 import countdown1
            countdown1
            import kysymys1
            kysymys1
        
    else:
        from countdown import countdown
        countdown
        from jatketaanko import uudestaan
        uudestaan
alku()






