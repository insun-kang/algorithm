from collections import Counter

def solution(str1, str2):
    answer = 0
    check=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    str1set=[]
    str2set=[]
    intersection=[]
    union=[]
    for i in range(len(str1)-1):
        if str1[i].lower() in check and str1[i+1].lower() in check:
            str1set.append(str1[i:i+2].lower())
            
    for i in range(len(str2)-1):
        if str2[i].lower() in check and str2[i+1].lower() in check:
            str2set.append(str2[i:i+2].lower())
    
    if len(str1set)==0 and len(str2set)==0:
        return 65536
    
    cset1=Counter(str1set)
    cset2=Counter(str2set)
    print(str1set,str2set)
    print(cset1, cset2)
    
    intersection=list((cset1 & cset2).elements())
    union=list((cset1 | cset2).elements())
    print(intersection, union)
    return int((len(intersection)/len(union))*65536)