def combination(cb,nb,ssf,sb,asf):
    if cb>nb:
        if ssf==sb:
            print(asf)
        return

    combination(cb+1,nb,ssf+1,sb,asf+"i")
    combination(cb+1,nb,ssf+0,sb,asf+"-")


n=int(input())
k=int(input())
combination(1,n,0,k,"")