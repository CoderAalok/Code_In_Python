
import string
print(string.ascii_letters)

ascii_Cap = [chr(i) for i in range(65, 91)]
ascii_Smll = [chr(j) for j in range(97,123)]

print(''.join(ascii_Smll + ascii_Cap))

