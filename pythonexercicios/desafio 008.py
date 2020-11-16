medida = float(input('Digite um valor em metro: '))
cm = float(medida * 100)
mm = float(medida * 1000)
km = float(medida * 0.001)
hm = float(medida * 0.01)
dam = float(medida * 0.1)
dm = float(medida * 10)
print('-'*12)
print(' {:.2f}m \n {:.2f}cm \n {:.2f}mm \n {:.2f}km \n {:.2f}hm \n {:.2f}dam \n {:.2f}dm'.format(medida, cm, mm, km,
                                                                                                     hm, dam, dm))
print('-'*12)





