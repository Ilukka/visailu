


def uudestaan():
    jatkot = input("Haluatko kokeilla uudestaan? (k)yllä vai (e)i: ")
    if jatkot == "k" or jatkot == "K":
        import alku
        alku
    else:
        from countdown import countdown
        countdown

uudestaan()