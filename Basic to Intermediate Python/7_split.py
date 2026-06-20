def split_str(strr):
    words = strr.split()
    
    #Method-I 
    for i in words:
        print(i,end=' ')
        
    #Method-II
    com = ' '.join(words)
    print(com)
    
split_str('HTTP is refers to protocal.')