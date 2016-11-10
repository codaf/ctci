

def isRotation(s1,s2):
    if len(s1) == len(s2) and len(s1) !=0:
        newS =s1+s1
        print newS.find(s2)
        if newS.find(s2)>-1:
            print True
        else:
            print False

    else:
        print "False Not same length"

if __name__ == "__main__":
    s1 = "helloworld"
    s2="oworldhellp"
    isRotation(s1,s2)