import random
import math
#mohsen sharifi pooya / 97440148 / python cod _seri7
zojha=[]
dokhtarha = ["sara","zari","neda","homa","eli","goli","mary","mina"]
pesarha = ["ali","reza","yasin","benyamin","mehrdad","sajjad","aidin","shahin"]

def search(zojha,pesar,dokhtar):
    zoj=[]
    for j in zojha:
        if j[0]==pesar:
            return 1
        if j[1]==dokhtar:
            return 1
    else:
        return 0
while True :
    g=random.choice(pesarha)
    pesar=str(g)
    b=random.choice(dokhtarha)
    dokhtar=str(b)
    n=search(zojha,pesar,dokhtar)
    if n==0:
        zojha.append((pesar,dokhtar))
        if len(zojha)==8:
            print(zojha)
            break