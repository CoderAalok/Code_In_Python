def uncommon(strr1,strr2):
    if strr1 == '' or strr2 == '':
        print("String is blank")
    words = []
    words_1 = set(strr1.split())
    words_2 = set(strr2.split())
    # re = words_1 ^ words_2
    # words.append(re)
    for w in words_1:  
        if w not in words_2:  #Which words are not present in strr2
            words.append(w)
    return words
strr1 = "Protocol is rulebook for communication between devices on in internet"
strr2 = "HTTP is a Protocol , which communication to the server in such a way"
print(f"#-> In string_1 -> These words  {uncommon(strr1,strr2)} are uncommon in string_2." )