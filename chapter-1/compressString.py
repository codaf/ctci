


def compressString(s):
    list=[]
    last = s[0]
    count = 0
    for char in s:
        if char == last:
            count+=1
        else:
            list.append(last)
            list.append(str(count))
            last=char
            count=1
    list.append(last)
    list.append(str(count))
    new_string = ''.join(list)
    print len(new_string), new_string
    print len(s), s

    if len(new_string) > len(s):
        print new_string
    else:
        print s


if  __name__ =="__main__":
    s = "abcdef"
    compressString(s)