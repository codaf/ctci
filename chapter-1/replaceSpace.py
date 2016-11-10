

def replace(s):
    list =[]
    for c in s:
        if c == " ":
            list.append("%20")
        else:
            list.append(c)

    print ''.join(list)


if __name__=="__main__":
    s = "hello world how you doing..???     "
    replace(s.rstrip(" "))