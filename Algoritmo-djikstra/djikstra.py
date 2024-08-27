nos = [
    'RSL',
    'AUR',
    'ITU',
    'VID',
    'MIR',
    'TAI',
    'ATA',
    'PGE',
    'IBI',
    'PET',
    'AGR',
    'LON',
    'PNE',
    'STA',
    'ROE',
    'CHAP', 
    'POU',
    'RDO'
]

distancias = {
    'RSL': {'AUR': 13, 'ITU': 78, 'RDO': 176},
    'AUR': {'RSL': 13, 'AGR': 45},
    'AGR': {'AUR': 45, 'VID': 316.8, 'IBI': 123, 'MIR': 138},
    'VID': {'AGR': 316.8, 'IBI': 123, 'TAI': 201, 'PGE': 244.2},
    'IBI': {'AGR': 123, 'VID': 123, 'PGE': 87},
    'MIR': {'AGR': 138, 'ROE': 62, 'PET': 55.5},
    'ROE': {'MIR': 62, 'PET': 217.8, 'CHAP': 184.5},
    'PET': {'MIR': 55.5, 'ROE': 217.8, 'CHAP': 60, 'POU': 83.6, 'STA': 132},
    'CHAP': {'ROE': 184.5, 'PET': 60, 'POU': 43},
    'POU': {'CHAP': 43, 'PET': 83.6, 'STA': 78},
    'STA': {'POU': 78, 'PET': 132},
    'RDO': {'RSL': 176, 'PGE': 168, 'TAI': 16},
    'PGE': {'RDO': 168, 'PNE': 42, 'ATA': 39, 'VID': 244.2, 'IBI': 87},
    'PNE': {'ITU': 84, 'LON': 80, 'ATA': 363, 'TAI': 120, 'PGE': 42},
    'LON': {'PNE': 80},
    'ATA': {'PNE': 363, 'PGE': 39, 'VID': 201, 'RDO': 16},
    'TAI': {'PNE': 120, 'VID': 201, 'RDO': 16, 'PGE': 198}
}

naoVisitados = [
    'RSL',
    'AUR',
    'ITU',
    'VID',
    'MIR',
    'TAI',
    'ATA',
    'PGE',
    'IBI',
    'PET',
    'AGR',
    'LON',
    'PNE',
    'STA',
    'ROE',
    'CHAP',
    'POU',
    'RDO'
]


"""
Métodos de decisão da origem e destino
"""

"""
origem = input('origem:')
while origem not in nos:
    origem = input('origem: ')

destino = input('destino:')
while destino not in nos:
    destino = input('destino: ')

print(naoVisitados)
naoVisitados.remove(origem)
print(naoVisitados)
"""
"print(distancias[0])"

origem = input('origem:')
atual  = origem
menorValor = 0

for i in distancias[atual]:
    if menorValor == 0:
        menorValor = distancias[atual].get(i)
    elif menorValor > distancias[atual].get(i):
        menorValor = distancias[atual].get(i)

print(menorValor) 
     