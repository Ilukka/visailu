def countdown2():
    import time

    for i in range(10, -1, -1):
        print(i)
        time.sleep(1)  # Hidastaa tulostusta yhdellä sekunnilla

    print("Se oli vitsi! Selvitä vielä viimeinen tehtävä koodien perusteella:")
    import lopetus
countdown2()
