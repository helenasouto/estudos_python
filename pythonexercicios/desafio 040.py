n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
#m = (n1 + n2)/2
s = n1 + n2
m = s/2
if m < 5:
    print('\033[0;31mREPROVADO')
if 5 <= m < 6.9:
    print('\033[0;35mRECUPERAÇÃO')
if m >= 7:
    print('\033[0;32mAPROVADO')
print('\033[0;34mSua média foi {}'.format(m))

