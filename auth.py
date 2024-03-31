m = 'aa'
e = ''
s = 1
for i in range(len(m)):
    e += chr(ord(m[i]) + s)
    print(e)