# def rotate(strr):
#     if not strr:
#         return None
#     d = 5
#     # return [strr[d:] + strr[:d], strr[-d:] + strr[:-d]]
#     print("AnticlockWise:", strr[d:] + strr[:d])
#     print("ClockWise:", strr[-d:] + strr[:-d])
    
# (rotate([1,2,3,4,5,0]))
# # (rotate('122356790'))


def StringSlicing(strr):
    if not strr:
        return None

    seen = False
    slic = strr[-4:] +strr[:-4]
    for i in strr:
        if i in slic:
            seen = True

    if seen:
        if slic != strr:
            print(f" Original: {strr}\n Sliced: {slic}\n The string is already sliced!")

StringSlicing('Prototype')
# print(all(i in 'asd' for i in 'asd'))
