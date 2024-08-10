from DeCryptage import *
i=0
while i!=1 and i!=2:
    print("Bonjour :\n1-Pour compresser \n2-pour de compresser")
    i=int(input("valeur: "))
    if i==1:compression()
    elif i==2:deCompression()
    else:print("erreur")
