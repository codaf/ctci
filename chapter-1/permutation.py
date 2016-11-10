
from collections import Counter


def isPermutation_SortingMethod(s1,s2):
    if len(s1) != len(s2):
        return False
    if ''.join(sorted(s1)) == ''.join(sorted(s2)):
        return True
    else:
        return False

def isPermutation_counterMethod(s1,s2):
    count = Counter()
    for char in s1:
        count[char] += 1
    for char in s2:
        if count[char] == 0:
            return False
        count[char] -= 1
    return True

if __name__=="__main__":
    s1= "aac"
    s2="cbb"
    result = isPermutation_SortingMethod(s1,s2)
    result1 = isPermutation_counterMethod(s1,s2)
    print result, result1
