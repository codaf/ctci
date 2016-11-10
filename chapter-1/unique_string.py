



def unique_string(s):
    if len(s) >256:
        return False
    a = set()
    for i in s:
        if i in a:
            return False
        else:
            a.add(i)
    return True

if __name__=="__main__":
    s = "Hh"
    result = unique_string(s)
    print result