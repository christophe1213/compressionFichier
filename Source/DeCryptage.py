from Crypt2 import *
# f=open("../Output2.txt","r")
# a=f.read()
# f.close()
def getCleCommpression():
    fcle=open("../cle.txt","r")
    # print(fcle.read())
    sCle=fcle.read()
    print(sCle)
    d={0:''}
    i=1
    for char in sCle:
        d[i]=char
        i+=1
    return d

def getLigne():
    fLine=open("ligne.txt",'r')
    l=[]
    s=fLine.read()
    a=''
    for char in s:
        if char=='\n':
            x=int(a)
            l.append(x)
            a=''
        else:a+=char
    return l


def convertionBinaire():
    f=open("../Output2.txt","r")
    a=f.read()
    print(a)
    r=''
    print("convertion en binaire")
    print("=====================")
    for char in a:
        print(f'{ord(char):07b}')
        r+=f'{ord(char):07b}'
    print("=====================")
    return r

def covertionTextInit():
    c=''
    l=getLigne()
    s=''
    x=''
    d=getCleCommpression()
    r=convertionBinaire()
    print(r)
    print("=====================")
    for char in r:
        c+=char
        x+=char
        # print(c,":",len(c))
        if len(x) in l:
            # print(d[1])
            s+=d[1]
            print("caractère en 1 bit :"+c)
            c=''
        if len(c)==4:
            print("caractère en 4 bit :"+c)
            s+=d[int(c,2)]
            c=''    
    return s
    
def deCompression():
    f=open("../fichierDecrypte.txt",'w')
    f.write(crypt(covertionTextInit()))

# print(getCleCommpression())
