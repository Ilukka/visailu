def countdown():
    import time

    for i in range(10, -1, -1):
        print(i)
        time.sleep(1)  # Hidastaa tulostusta yhdellä sekunnilla

    print("BOOM!")
countdown()
