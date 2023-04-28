# km
# hm
# dam
# m
# dm
# cm
# mm
medida = float(input('Uma distância em metros:' ))
cm = medida * 100
mm = medida * 1000
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
print('A medida de {:.1f}m corresponde a {:.0f}cm, {:.0f}mm, {:.1f}km, {:.1f}dam, {:.1f}hm'.format(medida, cm, mm, km, dam, hm))

