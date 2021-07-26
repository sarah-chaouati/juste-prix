import random

selectNb = random.randint(1,100)
nbEntre = 0
startPoint = 100


while startPoint > 0:

    if nbEntre != selectNb:
        print("Votre proposition ? : ")
        nbEntre = int(input()) # la proposition à comparer

        if nbEntre < selectNb: #si la propo est inferieur au nb à deviner
            startPoint = startPoint - 5 #update pts
            print("C'est plus")

        elif nbEntre > selectNb: #si la propo est superieur au nb à deviner
            startPoint = startPoint - 5 #update pts
            print("C'est moins")


        elif nbEntre == selectNb:
            print("NICE")
            print(startPoint)

    if startPoint <= 0:
        print("Et c'est perdu")


