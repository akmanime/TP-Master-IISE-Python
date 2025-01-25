from conversion import dollars_to_dirhams as dtd
from conversion import meters_to_kilometers as mtk

dollar = int(input('entrer le montant en dollar : '))
meters = int(input('entrer le metrage : '))

print(dtd(dollar))
print(mtk(meters))