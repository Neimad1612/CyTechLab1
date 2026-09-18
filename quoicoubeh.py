def apagnan():
    mot = input("Mot code\n")
    while mot != str.casefold("Quoi"):
        mot = input("Réessayer\n")
    print("Quoicoubeh")

apagnan()