#Pour chercher l'index du chaine
def cherche(l,c):
    i=0
    while  i<len(l) and c!=l[i]:
        i+=1
    return i
#Pour crypter le chaine
def crypt(original):
    list1=['a','b','c','d','e','f','g','h','i','j','k','l','m']
    list2=['n','o','p','q','r','s','t','u','v','w','x','y','z']
    #pour chaine pour la valeur de retour
    r=""
    for char in original :
        if char in list1:
            r=r+list2[12-cherche(list1,char)]
        elif char in list2 :
            r=r+list1[12-cherche(list2,char)]
        else:
            r+=char
    return r

#Pour calcule le caractère qui à beaucoup ouccurence
def LettreBeaucoupOccurence(caractere):
    d={}
    for c in caractere:
        if c not in d:
            d[c]=1
        else :
            d[c]+=1
   
    return d

#Pour retourner le charatère qui a beaucoup occurence
def CharMaxValue(d):
    m=0
    s=''
    for char in d:
        m=max(m,d[char])
    for char in d:
        if d[char]==m:
            s=char
            break
    return s

#Pour creer un dictionnaire de compression
def dicoCompression(d,c):
    
    dCompress={c:1}
    f=c
    i=2
    fcle=open("../cle.txt",'+w')
    for char in d:
        if char!=c:
            dCompress[char]=i
            i+=1
            f+=char
    fcle.write(f)
    return dCompress

def outpout(f,dCompress):
    fout=''

    lg=''
    #le variable lg pour memoriser les lignes qui se trouvent le caractère qui a beacoup d'occurence
    for char in f:
        if dCompress[char]==1:
            fout+=f'{dCompress[char]:01b}'
            print("caractère en 1 bit :"+f'{dCompress[char]:01b}')
            lg+=str(len(fout))+'\n'
        else:
            print("caractère en 4 bit :"+f'{dCompress[char]:04b}')
            fout+=f'{dCompress[char]:04b}'
    #sauvegarder les lignes
    flg=open('ligne.txt','w')
    flg.write(lg)
    flg.close()
    a=''
    f=''
    print("le compression en binaire "+fout)

    print("=====================")
    for char in fout:
        a+=char
        if len(a)==7:
            f+=chr(int(a,2))
            # print("f:"+f) 
            print(a)        
            a=''
        
    print("=====================")
    if len(a)<7:
        print("condition si a <7"+f)
        # print("a avant:"+str(int(a,2)))
        a=a+'0'*(7-len(a))
        f+=chr(int(a,2))
        print("a:"+a) 
        print("a après"+str(int(a,2)))
    elif  len(a)==7: 
        f+=chr(int(a,2))
        print("si a ==7")
    print("fichier outpout "+f)
    fo=open("../Output2.txt",'w')
    fo.write(f)
    # fcle=open("../cle.txt",'+w')
    # fcle.write(str(dCompress))
    # fcle.write(str(ligne))  

def compression():
    
    fog=open("../fichierOriginal.txt","r")
    chaine=fog.read()
    chaineCrypte=crypt(chaine)
    dico=LettreBeaucoupOccurence(chaineCrypte)
    print("dico :"+str(dico))
    char=CharMaxValue(dico)
    print("le caractère qui a beaucoup d'occurance "+char)
    cle=dicoCompression(dico,char)
    print("cle de compression :"+str(cle))
    outpout(chaineCrypte,cle)


# a='00111111'
# o=int(a,2)
# print(chr(int(a,2)))

# fog=open("../fichierOriginal.txt","r")
# chaine=fog.read()
# chaineCrypte=crypt(chaine)
# print("chaine crypté: "+chaineCrypte)
#     # print(chaineCrypte)
# compression(chaineCrypte)
# f=open("../Output2.txt","r")
# a=f.read()
# fcle=open("../cle.txt")
# print(fcle.read())
# print("Feuille de sortie")
# for char in a:
#     c=ord(char)
#     print(c)