with open("file1.txt",'r')as f:
    # print(f.tell()) #it return current position of file pointer or cursor
    print(f.readline())
    # f.seek(0) # it reset the file pointer
    print(f.readline())
    print(f.read(10))
    