strr = 'pneomonoultramicroscopicsilivolcanococious Volcano supertaious'.split()
vol = 'aeiou'
rel = [i for i in strr if all(v in i for v in vol)]
print(rel)